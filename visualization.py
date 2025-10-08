import matplotlib.pyplot as plt

def plot_distribution(S_T, S0, percentiles, ticker, horizon_days):
    p10, p50, p90 = percentiles

    plt.figure(figsize=(10,6))
    plt.hist(S_T, bins=60, color='skyblue', edgecolor='white', alpha=0.6)
    plt.axvline(S0, color="black", linestyle="--", linewidth=2, label=f"Current ₹{S0:.2f}")
    plt.axvline(p10, color="red", linestyle="--", linewidth=2, label=f"10th percentile ₹{p10:.2f}")
    plt.axvline(p50, color="purple", linestyle="--", linewidth=2, label=f"50th percentile ₹{p50:.2f}")
    plt.axvline(p90, color="green", linestyle="--", linewidth=2, label=f"90th percentile ₹{p90:.2f}")
    plt.title(f"{ticker} Monte Carlo Terminal Price Distribution ({horizon_days} Days)")
    plt.xlabel("Price (INR)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.show()
