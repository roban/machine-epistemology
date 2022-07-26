---
layout: post
title: "Haack's Foundherentism and Bayesian Inference"
---

Susan Haack, in discussing her epistemological theory that she
calls "Foundherentism", proposes that

> Because quality of evidence is multi-dimensional, we should not
> necessarily expect a linear ordering of degrees of justification
> ... Nor ... does it look realistic to aspire to anything as
> ambitious as a numerical scale of degrees of justification.

The three dimensions to evidential quality she proposes are
**supportiveness**, **independent security**, and
**comprehensiveness**:

> How justified $$A$$ is in believing that $$P$$ ... depends on
>
> * how well the belief in question is supported by his experiential
> evidence and reasons **[supportiveness]**;
>
> * how justified his reasons are, independent of the belief in question
> **[independent security]**;
>
> * and how much of the relevant evidence his evidence includes
>**[comprehensiveness]**.[^haack]

[^haack]: Haack, Susan. "A Foundherentist Theory of Empirical
    Justification" in Michael Huemer, ed., *Epistemology: Contemporary
    Readings* (2002). Square-brackets are in the original, bullets
    and bold are mine.

I'll argue here that Bayesian inference can be seen as a way of
providing just such a linear ordering and numerical scale in some
circumstances.

We can start by associating Haack's terms with the jargon of Bayesian
inference.

## beliefs and evidence

The belief $$P$$ might be identified with a statement about model
parameters that can be assigned a posterior probability,
e.g. "parameter $$x$$ has a value less than $$0.5$$ (though see
further discussion below). $$A$$'s "experiential evidence" seems
similar to the set of observables in a Bayesian model.

Haack uses a crossword analogy in which a $$P$$ is a proposal for a
given entry ("3 Down is 'onomatopoeia'") and the experiential evidence
is provided by the clue for the given entry.

## independent security

In the crossword analogy, the degree of **independent security** is
determined by how confident $$A$$ is in the other intersecting entries
that are already filled in (and thus provide part of the evidence for
a proposed value of the entry itself). This confidence is, in turn,
based on the clues for *those* entries plus entries that intersect
*them*, until eventually we reach bare clues.

In a Bayesian model of the whole crossword, I would normally consider
*all* the clues to be observables and *all* the entries to be random
variables. However, we could conceive of a model with a single entry
as the parameter of interest and the corresponding clue as the
observable. The intersecting entries could then be "nuisance"
parameters to be marginalized over. Our confidence in the intersecting
entries would be expressed as priors over their possible values.

Therefore, I propose that **independent security** is identified with
the prior. Note that the model itself can be considered to be part of
the prior: it can be conceived of as having been drawn from a larger
space of all possible models and assigned a prior of 1 (with all other
models assigned 0). Of course, this (and any) choice of prior can be
debated, just as an assessment of the independent security of $$A$$'s
belief that $$P$$ can be debated.

## supportiveness

Haack's **supportiveness** seems closely related to the likelihood
since it incorporates $$A$$'s "experiential evidence". In the
single-entry crossword example, the likelihood would be defined in
terms of how well a candidate entry fit the clue (the "experiential
evidence").

Haack also wants supportiveness to include $$A$$'s "reasons," which
seem to be non-experiential evidence or prior beliefs. In that case
we'd need to identify supportiveness with the posterior, which
incorporates the prior on intersecting entries (the "independent
security"). However, since we'd like a separate notion of
"supportiveness", I propose instead to stick with the likelihood,
which only depends on the "experiential evidence" contained in the
observables.

We are now free to identify the Bayesian posterior probability as our
scalar measure of justification.

## comprehensiveness

**Comprehensiveness** is addressed by model expansion in Bayesian
inference. Let's say $$A$$ proposes a model that incorporates a set of
observables $$y$$. Based on the posterior of this model $$A$$ assigns
a particular degree of justification $$p(P | y)$$ to belief
$$P$$. $$B$$ criticizes $$A$$ by suggesting that she overlooked some
"relevant evidence" $$z$$. How can $$A$$ reassess her justification
for believing $$P$$? Trivially, if $$z$$ simply consists of more
instances of the same type of observations as $$y$$, then they can
just be appended to $$y$$ to form $$y'$$ and the posterior
recalculated with the same model $$p(P | y')$$.

In the general case we might have to change not just the observables
but the entire specification of the model to non-trivially incorporate
new evidence. This points to the idea that the meaning of "belief"
might be context dependent. Within the framework of a given model it
might refer to statements like "parameter $$x < 0.5$$", which can be
assigned a posterior probability. When the model itself is called into
question, however, the "belief in question" expands to encompass the
whole model, prior, parameter-value complex. To assign a scalar degree
of justification to this expanded belief, we must define an
overarching model that includes all competing beliefs (sub-models) and
all relevant evidence.

Bayesian inference also naturally incorporates Haack's idea of
"degrees of relevance." Consider a (sub-)model that depends, in part,
on a type of observation that we don't posses. We have to marginalized
over the missing data, which will generally lower the likelihood of
the observed data. Therefore *adding* the missing data should increase
the likelihood of the sub-model and tend to increase its
"justification" (posterior probability), while leaving unchanged the
posterior of a sub-model that is indifferent to the extra evidence.

However, if the data is "irrelevant" -- if it adds no information to
the model and therefore fails to increase the likelihood of the
observed data under the model -- it will not increase the
likelihood. [^occam]

[^occam]: A closely related idea is that Bayesian inference naturally
    incorporates Occam's razor: models with more parameters or more
    diffuse priors on the same parameters are often "penalized"
    relative to "simpler" models (unless the increased quality of
    their match to the data outweights the increased complexity). See
    Zoubin and Ghahramani. ["A note on the evidence and Bayesian Occam’s
    razor"](http://mlg.eng.cam.ac.uk/zoubin/papers/05occam/occam.pdf)
    (2005).

There are certainly other approaches to model comparison besides model
expansion. Model comparison has a long and contentious history in
Bayesian and non-Bayesian contexts, which I won't discuss.

My argument here is that it is possible to use the Bayesian posterior
probability as the numerical scale Haack referred to with skepticism,
not that it is always possible to *agree* on the inputs to the
process. In other words, Bayesian inference gives us a procedure for
combining these dimensions, even if there's still room for argument
*about* each dimension.

### Notes
