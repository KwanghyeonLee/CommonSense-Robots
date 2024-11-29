import os
import sys
import numpy as np

import d4rl.locomotion
import d4rl.hand_manipulation_suite
import d4rl.pointmaze
import d4rl.gym_minigrid
import d4rl.gym_mujoco
from d4rl.offline_env import set_dataset_path, get_keys

SUPPRESS_MESSAGES = bool(os.environ.get("D4RL_SUPPRESS_IMPORT_ERROR", 0))

_ERROR_MESSAGE = "Warning: %s failed to import. Set the environment variable D4RL_SUPPRESS_IMPORT_ERROR=1 to suppress this message."

try:
    import d4rl.flow
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % "Flow", file=sys.stderr)
        print(e, file=sys.stderr)

try:
    import d4rl.kitchen
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % "FrankaKitchen", file=sys.stderr)
        print(e, file=sys.stderr)

try:
    import d4rl.carla
except ImportError as e:
    if not SUPPRESS_MESSAGES:
        print(_ERROR_MESSAGE % "CARLA", file=sys.stderr)
        print(e, file=sys.stderr)


def qlearning_dataset(env, dataset=None, terminate_on_end=False, **kwargs):
    """
    Returns datasets formatted for use by standard Q-learning algorithms,
    with observations, actions, next_observations, rewards, and a terminal
    flag.

    Args:
        env: An OfflineEnv object.
        dataset: An optional dataset to pass in for processing. If None,
            the dataset will default to env.get_dataset()
        terminate_on_end (bool): Set done=True on the last timestep
            in a trajectory. Default is False, and will discard the
            last timestep in each trajectory.
        **kwargs: Arguments to pass to env.get_dataset().

    Returns:
        A dictionary containing keys:
            observations: An N x dim_obs array of observations.
            actions: An N x dim_action array of actions.
            next_observations: An N x dim_obs array of next observations.
            rewards: An N-dim float array of rewards.
            terminals: An N-dim boolean array of "done" or episode termination flags.
    """
    if dataset is None:
        dataset = env.get_dataset(**kwargs)

    N = dataset["rewards"].shape[0]
    obs_ = []
    next_obs_ = []
    action_ = []
    reward_ = []
    done_ = []

    episode_step = 0
    for i in range(N - 1):
        obs = dataset["observations"][i]
        new_obs = dataset["observations"][i + 1]
        action = dataset["actions"][i]
        reward = dataset["rewards"][i]
        done_bool = bool(dataset["terminals"][i])

        final_timestep = episode_step == env._max_episode_steps - 1
        if (not terminate_on_end) and final_timestep:
            # Skip this transition and don't apply terminals on the last step of an episode
            episode_step = 0
            continue
        if done_bool or final_timestep:
            episode_step = 0

        obs_.append(obs)
        next_obs_.append(new_obs)
        action_.append(action)
        reward_.append(reward)
        done_.append(done_bool)
        episode_step += 1

    return {
        "observations": np.array(obs_),
        "actions": np.array(action_),
        "next_observations": np.array(next_obs_),
        "rewards": np.array(reward_),
        "terminals": np.array(done_),
    }
