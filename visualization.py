import matplotlib.pyplot as plt
from typing import Tuple

def plot_distribution(S_T, S0: float, percentiles: Tuple[float, float, float], ticker: str, horizon_days: int):
    """
    Create a histogram of terminal prices with percentile and current price markers.

    Returns a matplotlib Figure object so callers (e.g., Streamlit) can render it.
    """
    p10, p50, p90 = percentiles

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(S_T, bins=60, color='skyblue', edgecolor='white', alpha=0.6)
    ax.axvline(S0, color="black", linestyle="--", linewidth=2, label=f"Current ₹{S0:.2f}")
    ax.axvline(p10, color="red", linestyle="--", linewidth=2, label=f"10th percentile ₹{p10:.2f}")
    ax.axvline(p50, color="purple", linestyle="--", linewidth=2, label=f"50th percentile ₹{p50:.2f}")
    ax.axvline(p90, color="green", linestyle="--", linewidth=2, label=f"90th percentile ₹{p90:.2f}")
    ax.set_title(f"{ticker} Monte Carlo Terminal Price Distribution ({horizon_days} Days)")
    ax.set_xlabel("Price (INR)")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4)

    return fig
