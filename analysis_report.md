TRADER BEHAVIOR INSIGHTS(Assignment report) 

 1. Assignment Overview

This assignment aims to explore the relationship between Bitcoin market sentiment (Fear/Greed Index) and historical trader performance from Hyperliquid. The primary objectives are to uncover hidden patterns within the data and deliver actionable insights that can drive smarter trading strategies.

Datasets Used:
* Bitcoin Market Sentiment Dataset (`fear_greed_index.csv`): Contains daily sentiment classifications (Fear/Greed).
* Historical Trader Data from Hyperliquid (`historical_data.csv`): Provides detailed trade-level information including account, symbol, execution price, size, side, time, PnL, etc.

 2. Data Preprocessing and Merging

 2.1. Data Loading and Initial Inspection

Both `historical_data.csv` (211,224 entries, 16 columns) and `fear_greed_index.csv` (2,644 entries, 4 columns) were loaded. Initial checks confirmed no missing values in either raw dataset.

 2.2. Data Cleaning and Transformation

* Date/Time Conversion:
    * The 'Timestamp IST' column in `historical_data.csv` was converted from string to datetime objects. A new 'Date' column was extracted (YYYY-MM-DD) to represent the trade date, aligning with the daily granularity of the sentiment data.
    * The 'date' column in `fear_greed_index.csv` was also converted to datetime objects.
* Data Type Alignment: Ensured both 'Date' columns were in a compatible datetime format for merging.

 2.3. Data Merging

The two datasets were merged using a `left` join on the daily date columns (`Date` from historical data and `date` from sentiment data). This ensures all individual trade records are preserved, and corresponding sentiment information is added where available.

* Merged Dataset Shape: (211,224 rows, 20 columns).
* Missing Sentiment Data: Only 6 trade entries in the merged dataset had no corresponding sentiment `value` or `classification`, indicating a high match rate. These few missing values were deemed negligible for the overall analysis.
* Date Range of Merged Data: The combined dataset covers trades and sentiment from "2023-05-01 to 2025-05-01".
* Sentiment Distribution: The merged data contains trades across all sentiment classifications: 'Fear', 'Greed', 'Extreme Greed', 'Neutral', and 'Extreme Fear'.

 3. Key Findings on Trader Performance and Market Sentiment

 3.1. Aggregated Trader Performance by Sentiment Classification

The table below summarizes key performance metrics grouped by market sentiment:

| Classification   | Total_Closed_PnL   | Average_Closed_PnL   | Total_Trades   | Average_Size_USD   |
| :--------------- | :----------------- | :----------------- | :------------- | :----------------- |
| Extreme Fear     | 739110             | 34.5379            | 21400          | 5349.73            |
| Extreme Greed    | 2.71517e+06        | 67.8929            | 39992          | 3112.25            |
| Fear             | 3.35716e+06        | 54.2904            | 61837          | 7816.11            |
| Greed            | 2.15013e+06        | 42.7436            | 50303          | 5736.88            |
| Neutral          | 1.29292e+06        | 34.3077            | 37686          | 4782.73            |

Observations:
* Highest Average PnL: 'Extreme Greed' periods exhibit the highest average `Closed PnL` per trade (~$67.89).
* Second Highest Average PnL: 'Fear' periods follow with the second highest average `Closed PnL` (~$54.29), notable for also having the largest average trade size.
* Lower Average PnL: 'Neutral' and 'Extreme Fear' sentiments generally correlate with lower average `Closed PnL`.
* Trade Volume: 'Fear' and 'Greed' periods see the highest number of overall trades.
* Trade Size vs. PnL: Interestingly, 'Extreme Greed' has a relatively smaller average trade size (~$3,112) compared to 'Fear' (~$7,816), suggesting that during peak bullishness, smaller, possibly more agile, trades contribute to higher average profitability.

 3.2. Distribution of Closed PnL (Risk Analysis)

| Classification   | count   | mean    | std     | min       | 25%   | 50%   | 75%     | max     | skewness     |
| :--------------- | :------ | :------ | :------ | :-------- | :---- | :---- | :------ | :------- | :----------- |
| Extreme Fear     | 21400   | 34.5379 | 1136.06 | -31036.7  | 0     | 0     | 5.63503 | 115287   | 60.066       |
| Extreme Greed    | 39992   | 67.8929 | 766.828 | -10259.5  | 0     | 0     | 10.0287 | 44223.5  | 26.1698      |
| Fear             | 61837   | 54.2904 | 935.355 | -35681.7  | 0     | 0     | 5.59086 | 135329   | 71.3389      |
| Greed            | 50303   | 42.7436 | 1116.03 | -117990   | 0     | 0     | 4.94411 | 74530.5  | -15.7868     |
| Neutral          | 37686   | 34.3077 | 517.122 | -24500    | 0     | 0     | 3.99579 | 48504.1  | 32.3025      |

Observations:
* Extreme Positive Skewness in Fear/Extreme Fear: 'Fear' (skewness: 71.34) and 'Extreme Fear' (skewness: 60.07) show highly positive skewness. This indicates that while most trades result in small or zero PnL, there's a strong presence of a few very large positive PnL outliers. This suggests a "home run" potential in these high-stress market conditions.
* Negative Skewness in Greed: 'Greed' exhibits negative skewness (-15.79). This pattern suggests that while small profits might be common, there is a risk of significant losses. Traders might be taking on too much risk as market sentiment grows excessively optimistic.
* High Volatility: The consistently high standard deviations across all sentiments highlight the inherent volatility of crypto trading, emphasizing the importance of robust risk management.

 Plots:

* Average Closed PnL by Market Sentiment: (See `average_pnl_by_sentiment.png`)
* Total Trades by Market Sentiment: (See `total_trades_by_sentiment.png`)
* Average Trade Size (USD) by Market Sentiment: (See `average_trade_size_by_sentiment.png`)
* Distribution of Closed PnL by Market Sentiment (Boxplot): (See `pnl_distribution_boxplot.png`)

 4. Uncovering Hidden Patterns

 4.1. Account-Level Performance by Sentiment

Analysis of individual accounts reveals varied performance profiles based on market sentiment:

* Top Performers during Extreme Greed: Account `0xb1231a4a2dd02f2276fa3c5e2a2f3436e6bfed23` recorded over $1.1 million in `Total_Closed_PnL`.
* Top Performers during Fear: Account `0x083384f897ee0f19899168e3b1bec365f52a9012` achieved over $1.1 million in `Total_Closed_PnL`.
* Inconsistent Performance: Some accounts experienced significant losses in specific sentiment categories, suggesting that not all trading strategies are adaptable to all market conditions. This highlights the importance of matching strategy to prevailing sentiment.

 4.2. Trade Side (BUY/SELL) Impact on PnL by Sentiment

| Classification   | Side   | Average_Closed_PnL   | Total_Trades   |
| :--------------- | :----- | :------------------- | :------------- |
| Extreme Greed    | BUY    | 10.4989              | 17940          |
| Extreme Greed    | SELL   | 114.585              | 22052          |
| Fear             | BUY    | 63.9271              | 30270          |
| Fear             | SELL   | 45.0496              | 31567          |
| Greed            | BUY    | 25.0023              | 24576          |
| Greed            | SELL   | 59.6911              | 25727          |
| Neutral          | BUY    | 29.2274              | 18969          |
| Neutral          | SELL   | 39.4564              | 18717          |

Key Pattern:
* Extreme Greed & Greed: `SELL` trades are significantly more profitable on average. This indicates a strong contrarian opportunity in overbought markets.
* Fear: `BUY` trades are more profitable on average. This supports the "buy the dip" strategy when market sentiment is overly negative.

 4.3. Coin Type Performance by Sentiment

The performance of different `Coin` types varies across sentiments:

* Major Cryptocurrencies (BTC, ETH, SOL):** Generally show positive average PnL across various sentiments, indicating relative stability and consistent trading opportunities.
* Sentiment-Specific Altcoins:
    * `@107` demonstrated high average PnL during 'Extreme Greed' but negative PnL during 'Fear', suggesting it might be a better asset for bullish environments.
    * Highly speculative/meme coins (`FARTCOIN`, `MELANIA`, `GRIFFAIN`) can experience extreme PnL swings (both positive and negative) depending on the sentiment, indicating their high-risk, high-reward nature. For instance, `FARTCOIN` had significant losses in 'Extreme Fear' but gains in 'Extreme Greed'.

 5. Actionable Insights for Smarter Trading Strategies

Based on the analysis, here are data-driven strategies to enhance trading performance:

1.  Adopt Contrarian Strategies in Extreme Sentiments:
    * When "Extreme Greed" prevails: Prioritize SELL/shorting strategies. The data strongly indicates that going against the prevailing bullish sentiment by taking profit or opening short positions yields superior average returns.
    * When "Fear" is dominant: Focus on BUY strategies. Accumulating assets when market sentiment is pessimistic appears to be a more profitable approach on average.

2.  Optimize Trade Direction by Sentiment: Actively choose your trade `Side` (BUY or SELL) based on the current market sentiment to align with historical profitability patterns. This is a crucial, actionable insight for day-to-day trading.

3.  Implement Sentiment-Aware Asset Selection:
    * Stable Assets: Consider major cryptocurrencies like `BTC`, `ETH`, and `SOL` for more consistent trading across different market conditions.
    * Strategic Altcoin Plays: Identify specific altcoins or assets that have historically performed exceptionally well under particular sentiment classifications. For example, if `@107` thrives in 'Extreme Greed', consider focusing on that asset during such periods. Be cautious with highly volatile, speculative assets; if traded, understand their specific sentiment dependencies.

4.  Emphasize Dynamic Risk Management:
    * The high volatility (large standard deviations) and extreme PnL outliers in all sentiments necessitate robust risk management practices. Always set strict stop-losses and manage position sizes proportionally to your risk tolerance.
    * Be particularly vigilant during "Greed" periods due to the observed negative skewness, indicating a higher probability of large losses despite many small wins.

5.  Learn from Successful Traders: Analyze the specific strategies (e.g., typical trade size, preferred assets, execution patterns) of accounts that consistently show high profitability in different sentiment conditions. This can help refine personal trading methodologies.

 6. Conclusion

This assignment effectively demonstrates that market sentiment plays a significant role in trader performance in the crypto market. By understanding and strategically adapting to prevailing market sentiments, traders can significantly improve their outcomes. The insights derived – particularly regarding the profitability of contrarian moves in extreme sentiments (selling into greed, buying into fear) and sentiment-specific asset selection – provide a strong foundation for developing smarter, data-driven trading strategies.
