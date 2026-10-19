import numpy as np

ROWS, COLS = 6, 9
START, GOAL = (2, 0), (0, 8)
WALLS = {
    (1, 2), (2, 2), (3, 2),
    (4, 5),
    (0, 7), (1, 7), (2, 7)
}
ACTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # Atas, Bawah, Kanan, Kiri[cite: 1, 2]

class MazeEnv:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.start = START
        self.goal = GOAL
        self.walls = WALLS

    def reset(self):
        return self.start

    def step(self, state, action_idx):
        r, c = state
        dr, dc = ACTIONS[action_idx]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < self.rows and 0 <= nc < self.cols) or (nr, nc) in self.walls:
            return state, True  # Mengalami tabrakan/terhalang[cite: 1, 2]
        return (nr, nc), False

    def bresenham(self, p0, p1):
        """Menghitung sel sepanjang garis lurus p0 ke p1 (Persamaan Ref [20])"""
        (y0, x0), (y1, x1) = p0, p1
        dx, dy = abs(x1 - x0), abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        cells = []
        while True:
            cells.append((y0, x0))
            if (y0, x0) == (y1, x1):
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy
        return cells

    def goal_in_sight(self, state):
        """Memeriksa apakah tidak ada dinding yang menghalangi pandangan ke GOAL"""
        cells = self.bresenham(state, self.goal)
        return int(not any(c in self.walls for c in cells))

    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])