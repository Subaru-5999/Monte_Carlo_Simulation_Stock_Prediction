import numpy as np

def run_montecarlo(S0, mu_daily, sigma_daily, horizon_days, num_paths=5000):
    rng = np.random.default_rng(42)
    dt = 1.0
    drift = (mu_daily - 0.5 * sigma_daily**2) * dt
    diffusion = sigma_daily * np.sqrt(dt)
    
    Z = rng.standard_normal(size=(horizon_days, num_paths))
    log_increments = drift + diffusion * Z
    log_paths = np.vstack([np.zeros((1, num_paths)), np.cumsum(log_increments, axis=0)])
    S_paths = S0 * np.exp(log_paths)

    return S_paths

def analyze_simulation(S_paths, S0):
    S_T = S_paths[-1]
    p10, p50, p90 = np.percentile(S_T, [10, 50, 90])

    VaR_95_price = np.percentile(S_T, 5)
    VaR_99_price = np.percentile(S_T, 1)
    VaR_95_loss = S0 - VaR_95_price
    VaR_99_loss = S0 - VaR_99_price

    bins = 200
    highest_prob_max, lowest_prob_min = [], []

    for day_idx in range(1, S_paths.shape[0]):
        day_prices = S_paths[day_idx, :]
        hist, bin_edges = np.histogram(day_prices, bins=bins, density=True)
        max_bin_idx = np.argmax(hist)
        max_price = (bin_edges[max_bin_idx] + bin_edges[max_bin_idx+1]) / 2
        highest_prob_max.append(max_price)

        max_prob = hist.max()
        candidate_bins = np.where(hist == max_prob)[0]
        min_bin_idx = candidate_bins[0]
        min_price = (bin_edges[min_bin_idx] + bin_edges[min_bin_idx+1]) / 2
        lowest_prob_min.append(min_price)

    return {
        "percentiles": (p10, p50, p90),
        "VaR": (VaR_95_price, VaR_95_loss, VaR_99_price, VaR_99_loss),
        "highest_prob_max": max(highest_prob_max),
        "lowest_prob_min": min(lowest_prob_min)
    }
