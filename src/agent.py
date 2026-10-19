# src/agent.py
import numpy as np

class DynaQAgent:
    def __init__(self, rows, cols, n_actions, params, rng):
        self.rows = rows
        self.cols = cols
        self.n_actions = n_actions
        self.p = params
        self.rng = rng
        self.Q = np.zeros((rows, cols, n_actions))
        self.model = {}
        self.seen = []

    def select_action(self, state):
        if self.rng.random() < self.p["epsilon"]:
            return self.rng.integers(self.n_actions)
        q = self.Q[state]
        return self.rng.choice(np.flatnonzero(q == q.max()))

    def update(self, s, a, r, s2, is_goal):
        # Pembaruan Q-learning langsung (Eq. 1)[cite: 1, 2]
        target = r if is_goal else r + self.p["gamma"] * self.Q[s2].max()
        self.Q[s][a] += self.p["alpha"] * (target - self.Q[s][a])

        # Pembelajaran model[cite: 1, 2]
        if (s, a) not in self.model:
            self.seen.append((s, a))
        self.model[(s, a)] = (r, s2)

        # Tahap Planning[cite: 1, 2]
        for _ in range(self.p["planning_steps"]):
            ps, pa = self.seen[self.rng.integers(len(self.seen))]
            pr, ps2 = self.model[(ps, pa)]
            ptarget = pr if ps2 == (0, 8) else pr + self.p["gamma"] * self.Q[ps2].max()
            self.Q[ps][pa] += self.p["alpha"] * (ptarget - self.Q[ps][pa])