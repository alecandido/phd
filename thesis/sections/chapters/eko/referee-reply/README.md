#  Reply to referee

Felix:

- **code advertisement** (first paragraph)
  - yes it is a code paper, it was just an oversight from our side not to put
    the correct "Type" in the web interface
- **lack of physics** (to be addressed mainly in the introduction) (second
    paragraph)
  0. this is meant to be a code paper, no surprise the lack of physics content
  1. most of the theory is known theory, so we decide not to repeat in this
     paper
    - but the code documentation is really expanded, even repeating (collecting)
      known theory, for user convenience and documentation completeness
    - point out at the beginning of the theory section that this is just a brief
      sketch, and a much more expanded version can be found in the online
      documentation, with pages corresponding 1-to-1 in submission
  2. we have new physics, and even more is coming
    - we are not implementing much new physics in the current version of EKO
    - but backward VFNS is relevant new physics
      - and it even includes backward intrinsic VFNS
    - we expect any new physics contribution to be easiest to be implemented in
      EKO than any other of the existing codes
      - e.g. N3LO (to be mentioned in the referee reply, since it's already in the
        paper)
- **interpolation** (third paragraph)
  - change 3.3
  - add explicit reference to documentation
  - add reference to whatever Wikipedia cites as a reference (paper or textbook)
  - chat a bit about the fact we do it block-wise, to avoid interpolation spikes
    (Runge phenomenon)
- **minor points** (sixth paragraph)
  - "introspection" -> "inspection (you can open the thing and look inside)"
  - define MHOU at the bottom of page 3 (just before "[6]")
  - "deserved" -> "needed"/"required"

Alessandro:

- **performances** (fourth paragraph)
  - "Python" -> "Python + numba" in Table 1
    - and briefly discuss in the text
  - write in the paper that numba is JIT compiled (restricted Python
    syntax, C-like back-end)
    - point out to the referee
  - stress the point that EKO best use case is really PDF fitting (and evolving
    several replicas)
  - the other tools are not bad, but we are just most suited for the task
  - since we target a different task (we are even delivering a different output,
    an operator in place of an evolved PDF) we are not providing an extensive
    comparison, because it is not much meaningful to quantitatively compare
    quantities with a different underlying meaning
    - since it's already expressed in the paper, we just need to make it more
      prominent, and point it out to the referee
    - re-sort section A.1, putting at the very beginning the statement that we
      can not compare and why

Giacomo:

- **Table 1**(fifth paragraph)
  - Pegasus delivery space:
    - it should be both x and N space
    - check that it is actually the case
  - add "input space"
    - PEGASUS rigid input space is discussed above:
      - let's make a pointer in the discussion, recalling to the reader
  - HOPPET, APFEL, QCDNUM, PEGASUS are all able to do backward FFNS (because
    it's trivial)
    - mention in the body that this is natural, since it comes from the solution
      of the differential equation (that works in both directions)
    - for matching is non-natural: it is a single matrix application, to go
      backward, you explicitly need to invert it
  - APFEL++
    - we are aware it exists, and it was meant to replace APFEL Fortran code
      with just a reimplementation in C++
    - it never reached feature-equality with APFEL (e.g. consider QED: this was
      the flag feature of APFEL, and never got into APFEL++)
    - it's currently developed mainly with GPD and TMD in mind
    - so APFEL++ has a different target, that's why we want to compare to the
      standard tools for the target we're addressing (PDF fitting), and those
      include APFEL, and not APFEL++
  - "LHAPDF" -> "produce LHAPDF"

Alessandro:

- **main points** (seventh paragraph)
  - point out even more the strengths of our code
  - **N space**
    - we need to elaborate on the reasons of the choice
    - availability of multiple solutions with a clean implementations (e.g.
      "truncated")
    - availability of splitting functions and matching conditions in N space
  - **backward VFNS**
  - **operators delivery**
    - best for PDF fitting
