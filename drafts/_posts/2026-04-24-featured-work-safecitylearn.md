title: "Featured project: SafeCityLearn - A benchmark for safety-constrained RL in distributed energy systems"
people:
- Amal Nammouchi
- Andreas Kassler
- Arunselvan Ramaswamy
- Andreas Theocharis
image: /images/posts/2026-04-24-featured-work-safecitylearn.png
summary: "When deploying reinforcement learning-based systems for adaptive control of distributed energy systems often ignore physical limits, such as battery discharge limits, thermal comfort limits, or grid import thresholds. SafeCityLearn introduces the first benchmark to ensure reinforcement learning agents respect safety constraints while optimizing for sustainability."
---

**Authors:** Amal Nammouchi, Andreas Kassler, Arunselvan Ramaswamy, and Andreas Theocharis.

**Project website:** [https://github.com/AmalNamm/Safe-CityLearn](https://github.com/AmalNamm/Safe-CityLearn).
**Paper (PDF):** [http://www.scitepress.org/Papers/2026/144633/144633.pdf](http://www.scitepress.org/Papers/2026/144633/144633.pdf).

**1. Context: The safety gap in energy AI**

The global energy transition is driving the integration of distributed energy resources (DERs) like photovoltaic generation and battery storage into residential and commercial buildings. Reinforcement learning (RL) has emerged as a promising way to manage these complex systems. 

However, deploying unconstrained RL in real-world energy systems poses a fundamental challenge: agents may take actions that over-discharge batteries, violate thermal comfort, or exceed grid thresholds. While safe RL has shown promise in synthetic benchmarks like robotics, no open and reproducible benchmark previously existed for evaluating these methods in realistic distributed energy settings.

**2. What SafeCityLearn does**

SafeCityLearn is the first benchmark for safe RL in distributed energy systems. It extends the existing CityLearn environment by transforming it into a full constrained Markov decision process (CMDP). 

* **Explicit safety channels**: It introduces configurable constraint functions and cost signals that reflect realistic energy limits.
* **Standardized integration**: The benchmark is integrated with the OmniSafe ecosystem, enabling standardized training and evaluation across major Safe RL algorithms.
* **Reproducibility**: The full framework, implementation, and experiment scripts are available as open source to foster community research.

**3. Technical approach**

SafeCityLearn embeds a CMDP formulation directly into the simulation framework. While traditional environments only provide reward signals, SafeCityLearn provides explicit cost channels that quantify operational violations.

The environment supports several families of constraint-handling mechanisms, including penalty methods, Lagrangian relaxation, and projection-based methods. It allows researchers to monitor both discounted constraint costs and empirical violation rates throughout training to ensure policies remain within a predefined safety budget.

**4. Why this matters for Climate AI**

Climate-friendly energy management requires more than just economic efficiency; it requires operational reliability. Unconstrained RL agents tend to fail in these environments because they lack signals regarding physical or regulatory boundaries, leading to persistent infeasibility.

SafeCityLearn demonstrates that incorporating constraint awareness significantly reduces violations, often below 5%, without compromising energy cost performance or emissions reduction. By maintaining the battery state-of-charge within admissible regions, Safe RL policies preserve the system's ability to absorb renewable surplus and discharge strategically during high-price periods, leading to more efficient long-horizon energy shifting.

**5. Key outcomes of the project**

* **Systematic comparison of safe RL algorithms**: The authors performed the first systematic comparison of safe RL methods in distributed energy systems. Experiments on a year-long battery scheduling task showed that while unconstrained agents (like PPO and TRPO) had violation rates as high as 70–95%, the proposed Lagrangian-based version successfully stabilized near the 5% budget.
* **Superiority of deterministic off-policy methods**: DDPG-Lag was found to perform exceptionally well because the battery-scheduling task is a continuous control problem where deterministic actor-critic methods excel. The Lagrangian dual update provided the necessary stability to enforce feasibility while benefiting from the data efficiency of sample reuse.
