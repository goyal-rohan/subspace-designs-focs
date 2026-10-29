---
# Page metadata and event details. Keep quoted text quoted, especially titles with colons.
page_title: "Subspace Designs · FOCS 2026 Workshop"
description: "Subspace Designs: A Universal Tool for Derandomization. A FOCS 2026 workshop on November 8 at NYU, New York City."
title: "Subspace Designs:"
subtitle: "A Universal Tool for Derandomization"
conference: "FOCS 2026"
conference_url: "https://focs.computer.org/2026/"
date: "2026-11-08"
date_label: "Sunday, November 8, 2026"
location: "Warren Weaver Hall, Room 109"
address: "NYU · 251 Mercer Street, New York City"
time: "9:00–11:30 a.m. & 12:30–3:00 p.m."
timezone_note: "All times are New York local time (EST)."
registration_url: "https://focs.computer.org/2026/registration-2/"
venue_url: "https://focs.computer.org/2026/venue/"
schedule_caption: "Sunday, November 8, 2026 · All times EST"
footer: "Subspace Designs · FOCS 2026"

# Add or edit talks here. A nonempty abstract automatically gets an Abstract control.
# For paragraphs or LaTeX, use `abstract: |` followed by indented Markdown paragraphs.
program:
  - title: "Morning session"
    time: "9:00–11:30 a.m."
    talks:
      - id: tutorial
        time: "9:00–10:00 a.m."
        title: "Subspace Designs and Local Linear Properties: A Tutorial"
        speaker: "Venkat Guruswami"
        affiliation: "UC Berkeley; Simons Institute"
        url: "https://people.eecs.berkeley.edu/~venkatg/"
        abstract: |
          A subspace design is a collection of large linear subspaces whose members, on average, have small intersection dimension with every low-dimensional subspace. Originally introduced as a tool for constructing list-decodable codes, subspace designs have emerged as a useful primitive in linear-algebraic pseudorandomness, and a unifying derandomization tool in coding theory. 
        
          Intriguingly, near-optimal subspace designs are themselves constructed from algebraic codes such as folded Reed–Solomon or univariate multiplicity codes. Recent work reveals a powerful reverse connection: the subspace-design property explains why these highly structured codes admit optimal list-size bounds for list decoding and proximity gaps approaching the optimal radius. More broadly, near-optimal subspace-design codes inherit, up to an arbitrarily small loss in rate, the guarantees of random linear codes for local coordinate-wise linear (LCL) properties—a general framework encompassing list decoding and list recovery. Recent work has shown that by capturing bipartite perfect matching as a LCL property, one can obtain a deterministic NC algorithm for bipartite perfect matching using subspace designs.

          The talk will survey this circle of ideas. It will introduce the definitions, constructions, and connections pertaining to subspace designs, and set the stage for follow-up talks in the workshop on the various aspects mentioned above.
      - id: constructions
        time: "10:00–10:30 a.m."
        title: "Explicit Constructions of Subspace Designs"
        speaker: "Jun-Ting (Tim) Hsieh"
        affiliation: "MIT"
        url: "https://jthsieh.github.io/"
        abstract: ""
      - id: lms
        time: "10:30–11:00 a.m."
        title: "The LMS Framework: Equivalences Between Subspace Designs and Random Codes"
        speaker: "Jonathan Mosheiff"
        affiliation: "Ben-Gurion University"
        url: "https://mosheiff.carrd.co/"
        abstract: ""
      - id: matching
        time: "11:00–11:30 a.m."
        title: "Bipartite Matching in NC via Subspace Designs"
        speaker: "Roshan Raj"
        affiliation: "Ohio State University"
        url: "https://sites.google.com/view/roshan-raj"
        abstract: ""
  - title: "Lunch"
    time: "11:30 a.m.–12:30 p.m."
    break: true
  - title: "Afternoon session"
    time: "12:30–3:00 p.m."
    talks:
      - id: list-decoding
        time: "12:30–1:00 p.m."
        title: "Optimal List Decoding via Subspace Designs"
        speaker: "Rohan Goyal"
        affiliation: "MIT"
        url: "https://goyal-rohan.github.io/"
        abstract: |
          I will present Yeyuan Chen and Zihan Zhang's breakthrough results showing optimal list-decoding of folded Reed-Solomon and more generally subspace-design codes. I will connect their techniques to previous works in the area on optimal list-decoding of random linear and random Reed-Solomon codes due to Alrabiah, Guo, Guruswami, Li, and Zhang.
      - id: proximity-gaps
        time: "1:00–1:30 p.m."
        title: "A Local View of Proximity Gaps via Line Decoding"
        speaker: "Kimi Sun"
        affiliation: "Stanford University"
        url: "https://scholar.google.com/citations?hl=en&user=ZMNZ7x8AAAAJ"
        speaker_label: "Kimi Sun on Google Scholar"
        abstract: |
          When many points on an affine line are close to a linear code, must the entire line be close to the code? Proximity gaps capture this local-to-global phenomenon and play an important role in interactive oracle proofs and their cryptographic applications.

          In this talk, I will discuss how line decoding, a notion introduced by Goyal and Guruswami, connects proximity gaps to the framework of local properties and subspace designs. Rather than asking only whether each point has a nearby codeword, line decoding asks whether many of these codewords themselves lie on a line with the same parameterization. I will explain how to view line decoding as a local property and how to establish it via pruning arguments building on the work of Ashvinkumar, Habib, and Srivastava. Together, these ideas yield near-capacity proximity gaps for subspace-design codes and random codes.

          Based on joint work with Rohan Goyal, Venkatesan Guruswami, and Mary Wootters.  
      - id: list-recovery
        time: "1:30–2:00 p.m."
        title: "Discrete Brascamp–Lieb Inequalities and List Recovery"
        speaker: "Joshua Brakensiek"
        affiliation: "UC Berkeley"
        url: "https://jbrakensiek.github.io/"
        abstract: |
          In coding theory, the problem of list recovery asks one to find all codewords $c$ of a given code $C$ which such that at least $1 - \rho$ fraction of the symbols of $c$ lie in some predetermined set of $\ell$ symbols for each coordinate of the code. A key question is bounding the maximum possible list size $L$ of such codewords for the given code $C$.

          In this talk, I will present novel combinatorial upper bounds on the list recoverability of various families of linear and folded linear codes, including random linear codes, random Reed–Solomon codes, explicit folded Reed–Solomon codes, and explicit univariate multiplicity codes. In the zero-error regime our upper bound matches known lower bounds. The primary technique is a novel application of a discrete entropic Brascamp–Lieb inequality to the problem of list recovery, allowing us to relate the local structure of each coordinate with the global structure of the recovered list.

          Based on joint work with Yeyuan Chen, Manik Dhar, and Zihan Zhang
      - id: pseudorandomness
        time: "2:00–2:30 p.m."
        title: "Linear-Algebraic Pseudorandomness"
        speaker: "Dean Doron"
        affiliation: "Ben-Gurion University"
        url: "https://deandoron.github.io/"
        abstract: ""
      - id: open-problems
        time: "2:30–3:00 p.m."
        title: "Open Problems and Future Directions"
        speaker: "The organizers"
        url: "#organizers"
        speaker_note: "(moderators)"

organizers:
  - name: "Joshua Brakensiek"
    url: "https://jbrakensiek.github.io/"
    affiliations:
      - "University of California, Berkeley"
    email: "josh.brakensiek@berkeley.edu"
  - name: "Rohan Goyal"
    url: "https://goyal-rohan.github.io/"
    affiliations:
      - "Massachusetts Institute of Technology"
    email: "rohan_g@mit.edu"
  - name: "Venkatesan Guruswami"
    url: "https://people.eecs.berkeley.edu/~venkatg/"
    affiliations:
      - "University of California, Berkeley"
      - "Simons Institute for the Theory of Computing"
    email: "venkatg@berkeley.edu"
---

<section id="overview" aria-labelledby="overview-title" markdown="1">

## Overview {#overview-title}

Subspace designs are linear-algebraic objects that turn properties of random error-correcting codes into explicit constructions. Originally introduced for list decoding, they now connect coding theory, pseudorandomness, and combinatorial optimization, with applications ranging from dimension expanders to parallel algorithms for bipartite matching.

This workshop aims to introduce subspace designs to the broader theoretical computer science community and bring participants to the research frontier. We will explore their foundations and constructions, the local coordinate-wise linear (LCL) framework of Levi, Mosheiff, and Shagrithaya (LMS), and recent applications, with time for open problems and discussion.

Planned themes include:

- **Foundations and constructions:** intuition for weak and strong subspace designs, and explicit constructions.
- **A common framework:** local linear properties and connections between subspace designs and random codes.
- **Applications:** list decoding and list recovery, proximity gaps, linear-algebraic pseudorandomness, and bipartite matching.
- **Open problems:** directions for future research across these areas.

The morning is intended for a broad TCS audience; the afternoon will explore applications in greater depth.

</section>

<section id="program" aria-labelledby="program-title" markdown="1">

## Program {#program-title}

The schedule and talk titles below are tentative. Abstracts and the remaining speakers will be added as they are confirmed.

<!-- schedule -->

Both sessions take place in Warren Weaver Hall, Room 109. See the [FOCS workshop program](https://focs.computer.org/2026/workshop-program/) for the full day’s schedule.
{: .program-note}

</section>

<section id="organizers" aria-labelledby="organizers-title" markdown="1">

## Organizers {#organizers-title}

<!-- organizers -->

</section>
