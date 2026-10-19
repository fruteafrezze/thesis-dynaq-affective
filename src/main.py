# src/main.py
import os
import numpy as np
from config import PARAMS
from environment import MazeEnv
from affect import AffectModel
from agent import DynaQAgent

def run_experiment(use_affect_reward=False, seed=0):
    rng = np.random.default_rng(seed)
    env = MazeEnv()
    agent = DynaQAgent(env.rows, env.cols, 4, PARAMS, rng)
    affect = AffectModel(PARAMS, env)

    steps_log, V_log, A_log = [], [], []

    for ep in range(PARAMS["n_episodes"]):
        s = env.reset()
        affect.reset()
        Vs, As = [], []
        t = 0
        while t < PARAMS["max_steps"]:
            t += 1
            a = agent.select_action(s)
            s2, collided = env.step(s, a)
            V, A = affect.update(s2, a, collided)
            Vs.append(V); As.append(A)

            is_goal = (s2 == env.goal)
            if is_goal:
                r = 10.0
            elif use_affect_reward and V > 0:
                r = 0.0  # Eksperimen 2: bias imbalan positif[cite: 1, 2]
            else:
                r = -1.0

            agent.update(s, a, r, s2, is_goal)
            s = s2
            if is_goal:
                break

        steps_log.append(t)
        V_log.append(np.mean(Vs))
        A_log.append(np.mean(As))

    return steps_log, V_log, A_log

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    print("Menjalankan eksperimen...")
    steps, V, A = run_experiment(use_affect_reward=False, seed=42)
    np.savez("data/results_exp1.npz", steps=steps, V=V, A=A)
    print("Selesai! Hasil eksperimen disimpan di data/results_exp1.npz")