> I would also like to reply to your comment in the response to the referee:
> The library was, is, and for some time will be under development and so we are
> hesitant to document a syntax which we know is temporary.

> It is normal for code to continue to evolve after publication in a journal.
> However, please also keep in mind EPJC's high standards for publication. If a
> code is in such a level of flux that it is not ready to be used in a stable way,
> then it would in most cases not be considered suitable for publication in EPJC.
> A typical level of readiness would normally be at least a 1.0.0 release. Many of
> the more successful codes have sought publication only when they were
> considerably more mature than that (e.g. APFEL was published at version 2.0.0).
> Exceptions can be made for codes that are pre-1.0.0, but generally they should
> have reached a stability that is comparable to 1.0.0.

Dear editor,

We agree with you that a desireable feature for a published code is to be sufficiently
stable.
The version of EKO we are proposing here is adequately good on its own,
and in this sense as stable as APFEL was at publication time.
Moreover, we believe this version has feature-parity with
PEGASUS, HOPPET, QCDNUM and APFEL (except QED evolution).

Indeed, the version numbering is relevant if its use is meaningful. APFEL v2 has
been released two weeks after v1 (see
https://github.com/scarrazza/apfel/tags?after=2.3.0), so the difference is not
that big. Instead: breaking compatibility in small number of weeks makes the
code _de facto_ unstable, regardless of the promises made by the numbering
scheme.
Critical features of APFEL like truncated evolution, used by
default by NNPDF, or completion of QED evolution (the main topic of the paper)
appeared after the paper release (v2.5.2 and v3.0.0, respectively). Also notice
that new features in point releases are not compliant with semantic versioning.

However, if we are using semantic versioning
in a meaningful way, instead of keep discussing a specific example, we need to provide a motivation to justify why
EKO is still v0.x at the time of publication.
Our idea of EKO is exposed in the paper: we want an evolution code that
implements some specific features (N-space, operators, ...) and is able to
perform the same job of the other available tools. This is our starting point,
the plain EKO that we are presenting: a different point of view, but as good as
other tools.

We could have called this v1.0, but we know immediately that we do not want to
stop here, and while achieving this "replacement" version, we are already
building some new features, e.g. N3LO QCD and QED evolution. Thus, we are aware that part of
the internal structure of EKO has to be modified for this.
More important, not being published we do not have yet a user base that tested
the usage (we tested ourselves of course, but that is different - as the referee
found out himself).
For this reason we can foresee breaking changes in the running development of the code:
especially taking into account
our first users, their feedback will require us to move in possibly unexpected
directions. Not having any user until now, we considered a more clever choice to
stay as free as possible to adapt to their needs and suggestions.

In any case, we benchmarked EKO and we used it to reproduce several
calculations, so we can tell that the version we are proposing (namely v0.8.5)
is a perfectly working and usable version.
We could have chosen to call it v1.0.0, we used it for months in our
work-in-progress framework, and we can maintain if needed (but with no external
user, there seems to be no need).

Maybe it was a poor choice, but definitely it is v1.0 comparable.
We plan to have a v1.0 release in the next few months.
