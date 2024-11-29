# CommonSense-Robots

#### This repository organizes researches related to AI Technology Development for Commonsense Extraction, Reasoning, and Inference from Heterogeneous Data, especially CommonSense-Robots task.
#### This repository summarizes following researches.

## Research list
* Cross-Domain Transfer via Semantic Skill Imitation (CoRL 2022) - Karl Pertsch, Ruta Desai, Vikash Kumar, Franziska Meier, Joseph J. Lim, Dhruv Batra, Akshara Rai.

  * The proposed method, Semantic Transfer Accelerated RL (STAR), is an approach that accelerates reinforcement learning (RL) in a target domain (e.g., a robotic manipulator in a simulated kitchen) through semantic imitation by utilizing demonstrations from a different source domain, such as human videos. Unlike conventional methods that imitate low-level actions, STAR focuses on reproducing sequences of semantic skills, such as “opening the microwave” or “turning on the stove.” This enables effective transfer of demonstrations across different environments (e.g., real-world to simulated kitchen) and agent embodiments (e.g., bimanual human demonstrations to robotic arms).
 
* Skill-based Model-based Reinforcement Learning (CoRL 2022) - Lucy Xiaoyang Shi, Joseph J. Lim, Youngwoon Lee.

  * The proposed Skill-based Model-based RL (SkiMo) bridges the gap between the efficiency of model-based RL and the abstraction of skill-based learning. By planning in the skill space, SkiMo allows agents to operate at a higher level of abstraction, reducing the computational burden and improving scalability for long-horizon tasks. This approach contrasts with traditional methods that rely on fine-grained single-step predictions, which can be computationally expensive and prone to compounding errors over extended horizons. SkiMo leverages a skill dynamics model that directly predicts the outcomes of high-level skills, enabling the agent to reason about task completion without simulating every intermediate state. This abstraction not only accelerates the learning process but also enhances robustness to environmental variability by focusing on achieving meaningful outcomes rather than micromanaging every action.


* Bootstrap Your Own Skills: Learning to Solve New Tasks with Large Language Model Guidance (CoRL 2023 Oral) - Jesse Zhang, Jiahui Zhang, Karl Pertsch, Ziyi Liu, Xiang Ren, Minsuk Chang, Shao-Hua Sun, and Joseph J. Lim.

  * The proposed BOotStrapping your own Skills (BOSS), is an approach that automatically learns to solve new long-horizon, complex, and meaningful tasks by growing a learned skill library with minimal supervision. BOSS learns to accomplish new tasks by performing "skill bootstrapping", where an agent with a set of primitive skills interacts with the environment to practice new skills without receiving reward feedback for tasks outside of the initial skill set.
 
* SPRINT: Scalable Policy Pre-Training via Language Instruction Relabeling (ICRA 2024) - Jesse Zhang, Karl Pertsch, Jiahui Zhang, and Joseph J. Lim.

  * The proposed SPRINT(Scalable Pre-training via Relabeling Language INsTructions) is an approach that allows automatic expansion of a base set of pre-training tasks, resulting in a significanly broader skill repertoire. SPRINT leverages two core ideas: instruction relabeling via LLMs and cross-trajectory skill chaining through offline reinforcement learning.

## Acknowledgements
These works were supported by Institute of Information & communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT). Also, these works were supported by supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT).
