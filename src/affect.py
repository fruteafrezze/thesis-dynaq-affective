# src/affect.py
class AffectModel:
    def __init__(self, params, env):
        self.p = params
        self.env = env
        self.reset()

    def reset(self):
        self.f_col = 0.0
        self.f_dir = 0.0
        self.f_goal = 0.0
        self.f_right = 0.0
        self.prev_action = None
        self.prev_dist = 0

    def _freq(self, f, event, rate):
        # Konvergen ke +1 jika ada kejadian, ke -1 jika tidak ada (Eq. 2 & 3)[cite: 1, 2]
        target = 1.0 if event else -1.0
        return f + (target - f) * rate

    def update(self, state, action, collided):
        # Frekuensi tabrakan (Eq. 2)[cite: 1, 2]
        self.f_col = self._freq(self.f_col, collided, self.p["nu"])

        # Frekuensi perubahan arah (Eq. 3)[cite: 1, 2]
        d = self.prev_action is not None and action != self.prev_action
        self.f_dir = self._freq(self.f_dir, d, self.p["theta1"])
        self.prev_action = action

        # Frekuensi keterlihatan target[cite: 1, 2]
        g = self.env.goal_in_sight(state)
        self.f_goal = self._freq(self.f_goal, g, self.p["theta2"])

        # Pergerakan menjauhi titik awal (Eq. 5)[cite: 1, 2]
        dist = self.env.manhattan(state, self.env.start)
        i = 1.0 if dist > self.prev_dist else -1.0
        self.prev_dist = dist
        self.f_right += (i - self.f_right) * self.p["kappa"]

        # Perhitungan Arousal (Eq. 4) & Valence (Eq. 6)[cite: 1, 2]
        if g == 0:
            A = (self.f_dir + self.f_col) / 2.0
        else:
            A = (self.f_dir + self.f_col + self.f_goal) / 3.0

        V = (self.f_goal + self.f_right) / 2.0
        return V, A