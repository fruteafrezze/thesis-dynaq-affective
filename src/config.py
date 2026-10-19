PARAMS = {
    "n_episodes": 20,       # Jumlah episode per eksperimen[cite: 1, 2]
    "max_steps": 2000,      # Batas langkah maksimum per episode[cite: 1, 2]
    "planning_steps": 50,   # Langkah perencanaan Dyna-Q[cite: 1, 2]
    "alpha": 0.01,          # Learning rate[cite: 1, 2]
    "gamma": 0.95,          # Discount factor[cite: 1, 2]
    "epsilon": 0.1,         # Probabilitas eksplorasi epsilon-greedy[cite: 1, 2]
    "nu": 0.2,              # Bobot pembaruan frekuensi tabrakan (f_col)[cite: 1, 2]
    "theta1": 0.2,          # Bobot pembaruan perubahan arah (f_dir)[cite: 1, 2]
    "theta2": 0.2,          # Bobot pembaruan keterlihatan target (f_goal)[cite: 1, 2]
    "kappa": 0.15,          # Bobot pembaruan arah pergerakan (f_right)[cite: 1, 2]
}