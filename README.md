# Junior Data Scientist – Trader Behavior Insights

Author: Kavya M

----

## 1. Introduction

This repository contains the completed assignment for the Junior Data Scientist position focusing on analyzing trader behavior in relation to market sentiment. The primary objective of this project was to explore the relationship between the Bitcoin market's Fear/Greed Index and historical trader performance data from Hyperliquid. Through this analysis, I aimed to uncover hidden patterns and derive actionable insights that can inform and optimize trading strategies.

---

## 2. Problem Statement

The core problem addressed by this assignment is to understand how different market sentiment conditions (ranging from "Extreme Fear" to "Extreme Greed") impact individual trader profitability, trading volume, and trade sizing. By identifying correlations and unique behavioral patterns, the goal is to provide data-driven recommendations for smarter trading decisions.

---

## 3. Datasets

Two primary datasets were utilized for this analysis:

1.  **`historical_data.csv`**: Contains detailed historical trading records from Hyperliquid, including trade timestamps, account IDs, symbols, execution prices, trade sizes (USD), trade sides (BUY/SELL), and Closed PnL (Profit and Loss).
    * **Note:** Due to its size, this file is not directly committed to this repository. Please download it from the following link and place it in the `data/` directory before running the script:
        [**Download historical_data.csv (Google Drive Link)**](https://drive.google.com/file/d/1RpSuz5t_C1I2OV7g8i8SHQ_VKGStndJ4/view?usp=drivesdk)
2.  **`fear_greed_index.csv`**: Provides daily Bitcoin market sentiment data, including a numerical value for the Fear & Greed Index and its corresponding qualitative classification (e.g., "Fear," "Greed," "Neutral"). This file is included directly in the `data/` folder.

---

## 4. Project Structure

The repository is organized as follows to ensure clarity and reproducibility:

. 
├── data/
│   └── fear_greed_index.csv
├── results/
│   ├── average_pnl_by_sentiment.png
│   ├── total_trades_by_sentiment.png
│   ├── average_trade_size_by_sentiment.png
│   └── pnl_distribution_boxplot.png
├── analysis_script.py
├── analysis_report.md
└── README.md


* `data/`: This directory contains `fear_greed_index.csv`. **Note that `historical_data.csv` should be downloaded separately into this folder.**
* `results/`: Stores all the generated visualizations (PNG images) from the analysis.
* `analysis_script.py`: The main Python script that performs data loading, cleaning, merging, analysis, and plot generation.
* `analysis_report.md`: A detailed Markdown report summarizing the project objectives, methodology, key findings, hidden patterns, and actionable insights.
* `README.md`: This file, providing an overview of the project.

---

## 5. Methodology

The analysis followed a structured approach:

1.  **Data Loading & Initial Inspection:** Both datasets were loaded and initial checks were performed to understand their structure and identify any immediate data quality issues.
2.  **Data Preprocessing & Merging:**
    * Timestamp columns were converted to datetime objects.
    * A common `Date` column was created for merging the daily sentiment data with the trade-level historical data.
    * The datasets were merged on the `Date` column, ensuring each trade record was associated with the corresponding market sentiment.
3.  **Exploratory Data Analysis (EDA) & Performance Metrics:**
    * Trader performance metrics (Total PnL, Average PnL, Total Trades, Average Trade Size) were aggregated and analyzed by market sentiment classification.
    * Visualizations (bar plots, box plots) were generated to understand the relationship between sentiment and performance.
4.  **Uncovering Hidden Patterns:**
    * In-depth statistical analysis of PnL distribution (including skewness) across different sentiments.
    * Analysis of account-level performance under specific sentiment conditions.
    * Investigation into the impact of `Side` (BUY/SELL) on PnL for each sentiment.
    * Exploration of `Coin` type performance influenced by market sentiment.
5.  **Actionable Insights:** Based on the patterns and findings, practical and data-driven trading strategies were formulated.

---

## 6. Key Findings & Actionable Insights

### Key Findings:

* **Sentiment-Specific Profitability:** 'Extreme Greed' and 'Fear' periods yielded the highest average `Closed PnL` per trade, suggesting distinct opportunities in extreme market conditions.
* **Trade Volume vs. PnL:** While 'Fear' and 'Greed' saw the highest trade volumes, 'Extreme Greed' trades, despite smaller average sizes, led to higher average profitability.
* **PnL Distribution Skewness:** 'Fear' and 'Extreme Fear' showed high positive skewness in PnL, indicating a few large winning trades. Conversely, 'Greed' exhibited negative skewness, suggesting a risk of significant losses.
* **Contrarian Trading Opportunities:**
    * During 'Extreme Greed' and 'Greed', `SELL` trades were significantly more profitable on average.
    * During 'Fear', `BUY` trades were more profitable on average.
* **Asset Performance by Sentiment:** Major cryptocurrencies (BTC, ETH, SOL) showed general stability, while certain altcoins exhibited highly sentiment-dependent performance (e.g., some performing well only in bullish environments).

### Actionable Insights:

1.  **Adopt Contrarian Strategies:** Consider initiating `SELL` positions during 'Extreme Greed' and 'Greed', and `BUY` positions during 'Fear' to align with historical profitability patterns.
2.  **Dynamic Trade Sizing & Risk Management:** Be mindful of heightened risk during 'Greed' periods due to negative PnL skew. Implement robust stop-losses and adaptive position sizing across all market conditions.
3.  **Sentiment-Aware Asset Selection:** Focus on specific assets that historically perform well under current market sentiment.
4.  **Emphasize Dynamic Risk Management:** The high volatility (large standard deviations) and extreme PnL outliers in all sentiments necessitate robust risk management practices. Always set strict stop-losses and manage position sizes proportionally to your risk tolerance.
5.  **Learn from High Performers:** Analyze the strategies of accounts that consistently profit in specific sentiment categories.

---

## 7. How to Run the Analysis

To reproduce the analysis and generate the plots:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourGitHubUsername/your-repo-name.git](https://github.com/YourGitHubUsername/your-repo-name.git)
    cd your-repo-name
    ```
    (Replace `YourGitHubUsername/your-repo-name` with your actual repository path)

2.  **Download the `historical_data.csv` file** from the link provided in the "Datasets" section above, and place it into the `data/` directory.

3.  **Ensure you have Python installed** (Python 3.8+ is recommended).

4.  **Install the required libraries:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

5.  **Run the analysis script:**
    ```bash
    python analysis_script.py
    ```
    This script will perform the data processing and analysis, and save the generated plots into the `results/` directory. Output tables and summary statistics will be printed to the console.

---

## 8. Files Included

* `analysis_script.py`: Python script for data processing and analysis.
* `analysis_report.md`: Detailed findings, patterns, and insights.
* `data/`: Directory containing `fear_greed_index.csv`.
* `results/`: Directory containing all generated `.png` plot images.
* `README.md`: This file.

---
