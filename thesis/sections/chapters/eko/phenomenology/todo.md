## Benchmarks

-   LHA benchmark
    -   paragraph "We match this and this, except for exceptions"
    -   plot?
-   APFEL
-   Pegasus
-   CT18
    -   through LHAPDF
    -   it has HOPPET inside (through xFitter?)
-   HERAPDF2.0
    -   through LHAPDF
    -   it has QCDNUM inside (through xFitter, at the time called
        HERAFitter)

Which kind of plot?

-   theory 200
    -   for CT18 and HERAPDF2.0 we need to adjust the settings
        accordingly
-   gluon, valence
-   usual eko report plot
    -   only middle one (no small-x, no large-x)
    -   do we want only differences? (bottom panel)

## Solutions

-   take `iterate-exact` (i.e. `EXA`) as reference
-   generate `truncated` (`TRN`), `iterate-expanded` (i.e. `EXP`),
    `perturbative-exact` (one change apart from `EXA`)
-   which conf?
    -   theory 200
-   which distributions?
    -   again `g` and `V`

## Interpolation

Compare 10, 15, 20, 50 against each other (assume 50 as the truth).

## Matching

-   take `EXA` (default) or `TRN` (biggest impact?) ?
-   which conf?
    -   theory 200
-   which distributions?
    -   again `g` and `V`
-   compare `mu_b=[.5, 1, 2.]`

Strong coupling evolution

-   plot strong coupling evolution through thresholds (LO, NLO, NNLO)
-   compare `mu_b=[.5, 1, 2.]`
-   make it an envelope
    -   center will be `mu_b=1.`
    -   the other two define a band

## MSbar masses

-   compute mass running (`mb(mub in [4,10])`)
-   plot decay
