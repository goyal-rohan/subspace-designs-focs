#!/usr/bin/env python3
"""Render the Markdown source and copy only public assets into dist/."""

from pathlib import Path
import shutil

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from latex2mathml.converter import convert as latex_to_mathml
from markdown.inlinepatterns import InlineProcessor
from markupsafe import Markup


ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "site"
OUTPUT = ROOT / "dist"

# Deliberately enumerate public assets. Never copy the repository or proposals.
PUBLIC_FILES = ("styles.css",)
SOURCE_FILES = ("index.md", "template.html") + PUBLIC_FILES
REQUIRED_SECTIONS = {
    "<!-- schedule -->": '<table class="schedule">',
    "<!-- organizers -->": '<ul class="organizers">',
}


class MathInlineProcessor(InlineProcessor):
    def handleMatch(self, match, data):
        display = "block" if match.group(1) == "$$" else "inline"
        mathml = latex_to_mathml(match.group(2).strip(), display=display)
        # Stash the result so Markdown cannot reinterpret TeX subscripts or escapes.
        return self.md.htmlStash.store(mathml), match.start(0), match.end(0)


def render_markdown(text):
    if any(ord(character) < 32 and character not in "\n\t" for character in text):
        raise ValueError("Invalid control character in Markdown. Use abstract: | for LaTeX.")
    renderer = markdown.Markdown(extensions=["extra", "sane_lists"])
    # After inline code (190), but before Markdown backslash escapes (180).
    renderer.inlinePatterns.register(
        MathInlineProcessor(r"(?<!\\)([$]{1,2})(?![$])(.+?)(?<!\\)\1(?![$])", renderer),
        "math",
        185,
    )
    return Markup(renderer.convert(text))


def render_page(source):
    parts = source.split("\n---\n", 1)
    if not source.startswith("---\n") or len(parts) != 2:
        raise ValueError("index.md must start with YAML metadata between --- lines.")
    metadata = yaml.safe_load(parts[0][4:])
    if not isinstance(metadata, dict):
        raise ValueError("The YAML metadata in index.md must contain named fields.")
    for marker in REQUIRED_SECTIONS:
        if parts[1].count(marker) != 1:
            raise ValueError(f"index.md must contain exactly one {marker} marker.")
    environment = Environment(
        loader=FileSystemLoader(SOURCE),
        autoescape=True,
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    environment.filters["markdown"] = render_markdown
    page = environment.get_template("template.html").render(
        **metadata, content=render_markdown(parts[1])
    ).lstrip()
    for marker, section in REQUIRED_SECTIONS.items():
        if marker in page or section not in page:
            raise ValueError(f"Failed to render {marker}; refusing to publish an incomplete page.")
    return page


def build():
    for name in SOURCE_FILES:
        source = SOURCE / name
        if not source.is_file() or source.is_symlink():
            raise SystemExit(f"Expected a regular public source file: {source}")

    # Render before replacing the last successful build, so editing errors preserve it.
    page = render_page((SOURCE / "index.md").read_text(encoding="utf-8"))

    if OUTPUT.is_symlink():
        raise SystemExit("Refusing to build into a symlinked dist directory.")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()

    (OUTPUT / "index.html").write_text(page, encoding="utf-8")
    for name in PUBLIC_FILES:
        shutil.copyfile(SOURCE / name, OUTPUT / name)
    (OUTPUT / ".nojekyll").touch()
    print(f"Built index.md → index.html and {len(PUBLIC_FILES)} public asset(s) in {OUTPUT}")


if __name__ == "__main__":
    build()
