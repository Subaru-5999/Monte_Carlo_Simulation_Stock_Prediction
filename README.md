# Monte Carlo and Regression Based Stock Price Forecaster

Team **AlgoX** (PRP-III-T009)  
Course: Probability and Random Processes (TCS-344)

## 🚀 Overview
This project forecasts stock prices using:
- **Linear Regression** → Drift & Volatility estimation  
- **Monte Carlo Simulation** → Thousands of stock price paths  
- **Percentile Analysis & VaR** → Probability-based risk insights  
- **Visualization** → Bell curve & percentile bands  

## 👩‍💻 Team Members
- Garima Bhargava – Data Input & Preprocessing
- Stavya Dhyani – Regression Model
- Garvit Joshi – Monte Carlo Simulation & Analysis
- Akshat Bansal – Visualization

## 📂 Project Structure
- `modules/data_input.py` → Fetch stock data & compute log returns  
- `modules/regression_model.py` → Drift & volatility estimation  
- `modules/montecarlo_simulation.py` → Simulation & probability measures  
- `modules/visualization.py` → Histogram & percentile visualization  
- `main.py` → Integrates everything  

## ⚙️ Installation
```bash
git clone https://github.com/YOUR_USERNAME/stock-predictor-algox.git
cd stock-predictor-algox
pip install -r requirements.txt
```

## ▶️ Usage
Run the main script:
```bash
python main.py
```


## 🌐 Streamlit App

Run the interactive web app:
```bash
pip install -r requirements.txt
streamlit run app.py
```

Use the sidebar to set the ticker, historical start date, horizon, and number of paths, then click **Run Simulation**.
