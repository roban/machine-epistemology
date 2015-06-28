---
layout: post
title: "Haack's Foundherentism and Bayesian Inference"
---

Susan Haack[^haack] says,

[^haack]: Haack, Susan. "A Foundherentist Theory of Empirical
    Justification" in Michael Huemer, ed., *Epistemology: Contemporary
    Readings* (2002). Square-brackets are in the original, bullets
    and bold are mine.

> How justified $$A$$ is in believing that $$P$$ ... depends on
>
> * how well the belief in question is supported by his experiential
> evidence and reasons **[supportiveness]**;
>
> * how justified his reasons are, independent of the belief in question
> **[independent security]**;
>
> * and how much of the relevant evidence his evidence includes
>**[comprehensiveness]**.

She later states that,

> Because quality of evidence is multi-dimensional, we should not
> necessarily expect a linear ordering of degrees of justification
> ... Nor ... does it look realistic to aspire to anything as
> ambitious as a numerical scale of degrees of justification.

I'll argue here that Bayesian inference can be seen as a way of
providing just such a linear ordering and numerical scale.

## beliefs and evidence

We can start with a rough association between Haack's terms and
Bayesian modeling terms:

The "belief" in question $$P$$ (a given entry, e.g. 3 down, in the
crossword analogy) might be identified with a set of specific values
of a model's parameters (though see further discussion below).

$$A$$'s "experiential evidence" (the clue, in the crossword analogy)
is the set of observables in a Bayesian model.

## independent security

The notion of $$A$$'s "reasons", independent of her belief $$P$$ and
distinguished from her "evidence", is the concept I have the hardest
time pining down. This notion is closely tied to Haack's idea of
"independent security". In the crossword analogy, the degree of
independent security is determined by how confident $$A$$ is in the
other intersecting entries that are already filled in. This confidence
is, in turn, based on the clues for *those* entries plus entries that
intersect *them*, until eventually we reach bare clues.

In a Bayesian model of the whole crossword, I would consider *all* the
clues to be observables and *all* the entries to be random
variables. However, we could conceive of model with a single entry as
the parameter of interest and the corresponding clue as the
observable. The intersecting entries could then be "nuisance"
parameters to be marginalized over. Our confidence in the intersecting
entries (wherever it was derived from) would be expressed as priors
over their possible values.

Therefore, I propose that **independent security** is closely related
to the prior. Note that the model itself can be considered to be part
of the prior: it can be conceived of as having been drawn from a
larger space of all possible models and assigned a prior of 1 (with
all other models assigned 0, of course). Of course, this (and any)
choice of prior can be debated, just as an assessment of the
independent security of $$A$$'s belief that $$P$$ can be debated.

## supportiveness

Haack's **supportiveness** seems closely related to the posterior,
since it incorporates both $$A$$'s "experiential evidence" and
"reasons". In the single-entry crossword example, the likelihood would
be defined it terms of how well a candidate entry fit the clue (the
"experiential evidence"), while the posterior also incorporates the
prior on intersecting entries (the "independent
security"). Supportiveness, rather than being independent of
comprehensiveness (as we shall see) and independent security, in fact
becomes our sought-after numerical scale incorporating all three
"dimensions".

Since we'd like a separate notion of "supportiveness", I propose
instead to identify it with the likelihood, which only depends on the
"experiential evidence" contained in the observables.

## justification

Having cleaved supportiveness from the prior and identified it with
the likelihood, we are now free to identify the posterior as our
scalar measure of justification.

## comprehensiveness

**Comprehensiveness** is addressed naturally in Bayesian models, and
does not have to be separately specified or measured. Let's say $$A$$
proposes a model that incorporates a set of observables $$y$$. Based
on the posterior of this model $$A$$ assigns a particular degree of
justification $$p(P | y)$$ to belief $$P$$. $$B$$ criticizes $$A$$ by
suggesting that she overlooked some "relevant evidence" $$z$$. How can
$$A$$ reassess her justification for believing $$P$$? Trivially, if
$$z$$ simply consists of more instances of the same type of
observations as $$y$$, then they can just be appended to $$y$$ to form
$$y'$$ and the posterior recalculated with the same model $$p(P |
y')$$.

In the general case we might have to change not just the observables
but the entire specification of the model to non-trivially incorporate
new evidence. See the example discussed below. This points to the idea
that the meaning of "belief" might be context dependent. Within the
framework of a give model it might refer to statements like "parameter
$$x$$ has a value < 0.5$$, which can be assigned a posterior
probability. When the model itself is called into question, however,
the term "belief" in question expands to encompass the whole model,
prior, parameter-value complex. To assign a scalar degree of
justification to this expanded belief, we simply[^comparison] define
an overarching model that includes all competing beliefs (sub-models)
and all relevant evidence.

[^comparison]: Model comparison has a long and contentious history in
Bayesian and non-Bayesian contexts, which I won't discuss. My argument
here is that it is *sometimes* possible to use the Bayesian posterior
as the numerical scale Haack referred to with skepticism, not that it
is always possible to agree on a scale for ranking beliefs.

### example

Consider the following scenario. We are told a coin was tossed 100
times and landed on heads 63 times.

Now compare the following beliefs:

* $$P$$: A biased[^biased_coin] coin was used, with $$p(\textrm{head})
\ne 0.63$$.

[^biased_coin]: On the impossibility of such an unfair coin, see
    Gelman, Andrew.
    "[The Unicorn of Probability Theory](http://andrewgelman.com/2005/06/06/the_unicorn_of)"
    (2005).

* $$Q$$: A normal coin $$p(\textrm{head}) = 0.5$$ was used for the
first 74 flips, then a two-headed coin $$p(\textrm{head}) = 1.0$$ was
flipped for the remainder.

* $$R$$: A fair coin was used throughout, with $$p(\textrm{head}) =
0.5$$.


2. The last 25 tosses are all heads (while the first 75 are a mixture
of heads and tails).

If we only considered the first piece of evidence ("The tosses ended
up 63% heads."), then belief 1 (fair coin, then biased coin) and
2 (single, biased coin) have almost equal posterior probability,
assuming equal prior probabilities. In other words, assuming equal
"independent security", they have equal "supportiveness".










But what about comprehensiveness? Explanation 2 could be considered
less comprehensive than explanation 1 because it "ignores" or is
indifferent to the second piece of evidence (that the last 25 tosses
are all heads).

And indeed, the Bayesian model will assign a higher
likelihood (and higher posterior, given equal priors) to explanation
1.



## To Do

Check my assertion about the likelihood and posterior of the explanations.

Find discussions of this phenomenon as an expression of Occam's Razor.

Discuss the notion of testing or critiquing the model-prior complex.

Discuss how this highlights the incoherence of the concept of degree
of justification in a single belief independent of alternatives.

### Notes
