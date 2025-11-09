import streamlit as st
import numpy as np
import pandas as pd

from data_input import get_stock_data
from regression_model import estimate_parameters
from montecarlo_simulation import run_montecarlo, analyze_simulation
from visualization import plot_distribution

st.set_page_config(page_title="Stock Predictor • Monte Carlo", layout="wide")

st.title("📈 Stock Prediction Model (Monte Carlo)")
st.caption("Interactive front end for fetching data, estimating parameters, running simulations, and visualizing outcomes.")

with st.sidebar:
    st.header("⚙️ Controls")
    ticker = st.text_input("Ticker (e.g., TCS.NS, RELIANCE.NS)", value="TCS.NS").upper()
    start_date = st.date_input("Historical start date", pd.to_datetime("2022-01-01"))
    horizon_days = st.number_input("Prediction horizon (days)", min_value=1, max_value=365*2, value=30, step=1)
    num_paths = st.slider("Number of Monte Carlo paths", min_value=500, max_value=20000, value=5000, step=500)
    run_button = st.button("Run Simulation", type="primary")

@st.cache_data(show_spinner=False)
def _load_data(ticker: str, start: str):
    S0, returns = get_stock_data(ticker, start=start)
    return S0, returns

def _run_pipeline(ticker: str, start: str, horizon_days: int, num_paths: int):
    S0, daily_returns = _load_data(ticker, start)
    mu, sigma = estimate_parameters(daily_returns)
    S_paths = run_montecarlo(S0, mu, sigma, horizon_days, num_paths=num_paths)
    results = analyze_simulation(S_paths, S0)
    return S0, daily_returns, mu, sigma, S_paths, results

tabs = st.tabs(["Overview", "Simulation", "Chart"])

if run_button:
    with st.spinner("Running Monte Carlo simulation..."):
        S0, daily_returns, mu, sigma, S_paths, results = _run_pipeline(
            ticker, str(start_date), horizon_days, num_paths
        )
    with tabs[0]:
        st.subheader("Snapshot")
        col1, col2, col3 = st.columns(3)
        p10, p50, p90 = results["percentiles"]
        with col1:
            st.metric("Current Price", f"₹{S0:,.2f}")
            st.metric("Drift (μ)", f"{mu:.6f}")
        with col2:
            st.metric("Volatility (σ)", f"{sigma:.6f}")
            st.metric("VaR 95% Price", f"₹{results['VaR'][0]:,.2f}")
        with col3:
            st.metric("VaR 99% Price", f"₹{results['VaR'][2]:,.2f}")
            st.metric("10/50/90 pct", f"₹{p10:,.0f} / ₹{p50:,.0f} / ₹{p90:,.0f}")
        with st.expander("Show recent returns (sample)", expanded=False):
            df = pd.DataFrame({"log_return": daily_returns[-250:]})
            st.dataframe(df.tail(20), use_container_width=True)

    with tabs[1]:
        st.subheader("Terminal Prices (S(T))")
        st.write(f"Simulated {S_paths.shape[1]} paths for {horizon_days} days.")
        st.write("Below is a sample of 10 paths:")
        sample_idx = np.linspace(0, S_paths.shape[1]-1, 10, dtype=int)
        df_paths = pd.DataFrame(S_paths[:, sample_idx], columns=[f"Path {i+1}" for i in range(len(sample_idx))])
        st.line_chart(df_paths)

    with tabs[2]:
        st.subheader("Distribution Chart")
        fig = plot_distribution(S_paths[-1], S0, results["percentiles"], ticker, horizon_days)
        if fig:
            st.pyplot(fig)  # Pass the figure directly
        else:
            st.warning("No figure generated.")


else:
    with tabs[0]:
        st.info("Enter a ticker and press **Run Simulation** to begin.")
    with tabs[1]:
        st.empty()
    with tabs[2]:
        st.empty()
