---
layout: post
title: "Responsible Machine Learning is like Security"
---

# The analogy: RML and Security
I recently started using an analogy between responsible machine learning and information security to argue for the importance of investing in centralized teams dedicated to controlling the potential harms of automated decisions. After I saw [Salesforce’s Ethical AI Principal Architect Kathy Baxter make a similar point](https://www.zdnet.com/article/ai-ethics-should-be-hardcoded-like-security-by-design/) (via [a tweet from Margaret Mitchell](https://twitter.com/robanhk/status/1544734684101443584)), I thought I’d share my argument.

Responsible machine learning (RML) is like data security because investments in either are motivated (at least partly) by tail risk — the risk of rare, but costly, reputation-damaging incidents. Both security and RML require every team at a company act to responsibly, but also benefit from centralized support in the form of standards, monitoring, tools, expert consultation. 

### The stakes

It’s any company’s obligation to secure the sensitive information that users entrust to it (and obviously in its interest to protect trade secrets or other information that would be damaging if exposed). A company has a similar responsibility to understand and control the adverse impacts of automated, model-based decisions. Failing to take responsibility for either data security or the harms of automated decisions is not only an ethical lapse, but can damage a company’s reputation, draw attention from regulators, carry financial penalties, and hurt future growth.

### The need for a centralized team

Responsible ML, like security or compliance, is difficult for individual teams to prioritize because

- Incidents are seen as tail risks ([though see below](#are-model-harms-really-a-tail-risk)): from a short-term financial, any individual team is unlikely to pay the cost of a security incident or a public revelation of harmful model bias.
- Start-up costs are high: Both responsible ML and security require investments in tools and expertise. It’s inefficient for each team to duplicate that effort when much of it can be generalized and shared across teams.

It’s hard to fit tail risks into a team’s typical framework for metrics and goals. While RML improvements are important for a company’s growth in the long term, they are not necessarily the quickest and surest ways to move existing team metrics in aggregate, especially given that even auditing for gaps in security or model safety requires an initial investment in expertise and tools.

Therefore, just as every company beyond a certain scale has a centralized Security org, any company using machine learning will eventually need a centralized Responsible ML group that, like their Security team: 

- performs risk assessments, 
- define standards, 
- develops tools and best practices, and
- supports individual teams in implementing improvements. 

Individual teams may still be responsible for bringing their systems up to company-wide standards, but they can do so more efficiently with the guidance of a central team. 

# Responsible Machine Learning

Beyond the analogy with security, what are the motivations for funding a Responsible ML team, and sooner rather than later?

### Automation risks

In "responsible ML" (synonymous or overlapping with terms like "ethical AI", "fair ML", "ML fairness, accountability, and transparency", "algorithmic bias"), the risks to be addressed include:

- **Ethical risk** — companies have an obligation to address the well-known risk that machine-learning-driven systems can perpetuate existing patterns of economic and social inequality (or even [create new ones](https://arxiv.org/abs/2205.01166)).
- **Reputational risk** — companies need to be prepared to evaluate and respond to inquiries from users, journalists, and regulators about patterns of bias in automated decisions, which are becoming increasingly common across a variety of industries.
- **Policy risk** — an increasing appetite for regulation means that companies have an interest in demonstrating to policy makers that they use machine learning responsibly, for instance actively monitoring and improving models to avoid harms like the exacerbation of economic inequality.

These risks are not hypothetical: increasing media coverage of irresponsible applications of machine learning is leading to regulatory scrutiny and actions like [the draft legislation on AI currently being considered in the EU](https://www.brookings.edu/research/the-eu-ai-act-will-have-global-impact-but-a-limited-brussels-effect/), and [the FTC’s warnings in the US](https://www.ftc.gov/business-guidance/blog/2021/04/aiming-truth-fairness-equity-your-companys-use-ai). The many categories of potential harm covered by such regulation span multiple demographic and social axes, and require nuanced and context-specific work to enumerate, evaluation, and mitigate (while avoiding unintended consequences common to naive, stop-gap solutions).

### Are model harms really a tail risk?

RML-related incidents seem like a tail risk from a short-term financial perspective because the rate at which these harms come to the attention of regulators or the public is very low today (though increasing). The consensus in the field, however, is that any model trained on real-world data is likely to reproduce patterns of bias and inequity without active intervention. So the underlying risk of harm to already-disadvantaged groups is, in fact, pervasive, even if today the rate of immediate consequences to the company is relatively low. I’ve nonetheless framed this document around tail risks because those are more easily understood to fall under the fiduciary duties of company leadership, while responsibility for long-term societal impacts can seem less clear (e.g. something to be left to regulators).

### Long-term Growth and Other Benefits

Investing in Responsible ML tools and practices has benefits on top of mitigating the above risks:

- **Growing the user base** – small segments of users tend to disappear in the aggregate metrics by which any company measures model and product performance, but groups that are underrepresented in your metrics today are often the biggest opportunities for growing your user base in the future. RML tools that help find and improve small pockets of poor model performance are therefore a key to sustained long-term growth.
- **Supporting strategic users segments** – similarly, it can be a struggle to balance global model performance with ensuring consistently high performance for a small number of high-priority users. RML techniques for achieving performance improvements on targeted user subpopulations can also be applied to this problem.
- **Recruiting** – ML engineers are increasingly aware of the potential ethical complexity and reputational risk of deploying ML at scale and want reassurance that employers will prioritize the responsible use of the technology they build.


### Benefit of small, early investments

Responsible ML can suffer from letting the perfect be the enemy of the good. Because the surface area of potential risks is initially unclear, it can seem futile or dangerous to open that can of worms unless you can afford to fund a large, comprehensive project. And it’s true that a small team may not be able to mitigate every RML-related risk before any incident occurs. However targeted evaluation and improvement of your most public and impactful models can materially reduce the most salient risks and even unblock projects that would otherwise be deemed to pose too high a brand or compliance risk.

Perhaps the largest benefit of starting earlier with a small team (rather than waiting until you can fund a large effort) is that, when an incident does occur, you will be able to draw on that team’s existing infrastructure, tools, workflows, expertise, and external and internal personal networks to respond quickly, effectively, and credibly. The alternative is to start from scratch when an urgent need arises, resulting in less effective and slower incident response, and greater disruption to the timelines of other projects.
