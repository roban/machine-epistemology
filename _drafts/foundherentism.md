---
layout: post
title: "Haak's Foundherentism and Bayesian Inference"
---

# Haak's Foundherentism and Bayesian Inference

Susan Haak says,

> How justified A is in believing that P ... depends on how well the
> belief in question is supported by his experiential evidence and
> reasons [supportiveness]; how justified his reasons are, independent
> of the belief in question [independent security]; and how much of
> the relevant evidence his evidence includes [comprehensiveness].
(square-bracketed phrases are in the original)

> Because quality of evidence is multi-dimensional, we should not
> necessarily expect a linear ordering of degrees of justification
> ... Nor ... does it look realistic to aspire to anything as
> ambitious as a numerical scale of degrees of justification.

I'll argue here that Bayesian inference can be seen as a way
of doing just that.

Supportiveness seems closely related to the likelihood (if we want to
clearly distinguish it for independent security), or perhaps the
posterior (if we don't).

Independent security seems relates to the prior (internally). From an
external perspective, we might debate the justification of the prior
(the specification of the likelihood function, itself, can be seen as
part of the prior).

Comprehensiveness is addressed naturally in Bayesian models
(internally). As long as all explanations and observations are
included in the model, then the posterior of a given explanation
naturally depends on something that might be thought of as the
"comprehensiveness" of that explanation. Of course, externally we can
argue about evidence that was not included as observation or prior in
any given model. In principle this is resolved by forming an
overarching model that accepts *all* the evidence as observation, but
there are often practical difficulties there.

### Contrived Scenario

Consider the following scenario: we are handed the following
description of 100 coin tosses:

1. The tosses ended up 63% heads.

2. The last 25 tosses are all heads (while the first 75 are a mixture
of heads and tails).

Consider a model containing the following *explanations*:

1. A fair coin was used for the first N flips, then a two-headed coin
was flipped for the remainder.

2. A weighted coin was used, with $$p(head) \ne 50\%$$.

3. A fair coin was used throughout, with $$p(head) = 50\%$$.


### Comprehensiveness

If we only considered the first piece of evidence, then explanations 1
and 2 have (almost) equal posterior probability, assuming equal prior
probabilities. In other words, assuming equal "independent security",
they have equal "supportiveness".

But what about comprehensiveness? Explanation 2 could be considered
less "comprehensive" than explanation 1 because it "ignores" or is
indifferent to the second piece of evidence. And indeed, the Bayesian
model will assign a higher likelihood (and higher posterior, given
equal priors) to explanation 1.



### To Do

Check my assertion about the likelihood and posterior of the explanations.

Find that article on the impossibility of a "weighted" coin.

Find discussions of this phenomenon as an expression of Occam's Razor.
