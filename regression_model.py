
import numpy as np

# Fake sample daily returns (normally distributed) for demo
sample_returns = np.random.normal(0.0005, 0.01, 100)

def estimate_parameters(returns):
    mu = np.mean(returns)   # Drift
    sigma = np.std(returns) # Volatility
    return mu, sigma


mu, sigma = estimate_parameters(sample_returns)

print("Regression Model Test")
print(f"Estimated Drift (μ): {mu:.6f}")
print(f"Estimated Volatility (σ): {sigma:.6f}")