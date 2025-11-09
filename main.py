from data_input import get_stock_data
from regression_model import estimate_parameters
from montecarlo_simulation import run_montecarlo, analyze_simulation
from visualization import plot_distribution

def main():
    ticker = input("Enter the stock ticker (e.g., TCS.NS): ").upper()
    horizon_days = int(input("Enter number of days for prediction horizon: "))

    S0, daily_returns = get_stock_data(ticker)
    print(f"\nCurrent Price of {ticker}: ₹{S0:.2f}")

    mu, sigma = estimate_parameters(daily_returns)
    print(f"Drift (μ): {mu:.6f}, Volatility (σ): {sigma:.6f}")

    S_paths = run_montecarlo(S0, mu, sigma, horizon_days)
    results = analyze_simulation(S_paths, S0)

    p10, p50, p90 = results["percentiles"]
    print(f"\n10th percentile: ₹{p10:.2f}, 50th: ₹{p50:.2f}, 90th: ₹{p90:.2f}")
    print(f"VaR 95%: ₹{results['VaR'][0]:.2f} (Loss {results['VaR'][1]:.2f})")
    print(f"VaR 99%: ₹{results['VaR'][2]:.2f} (Loss {results['VaR'][3]:.2f})")
    print(f"Highest probable max: ₹{results['highest_prob_max']:.2f}")
    print(f"Lowest probable min: ₹{results['lowest_prob_min']:.2f}")

    plot_distribution(S_paths[-1], S0, (p10, p50, p90), ticker, horizon_days)

if __name__ == "__main__":
    main()
