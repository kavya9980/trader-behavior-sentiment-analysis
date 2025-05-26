import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Data Loading ---
print("--- 1. Data Loading ---")
df_historical = pd.read_csv('historical_data.csv')
df_fear_greed = pd.read_csv('fear_greed_index.csv')

print("\n--- Initial Inspection: historical_data.csv ---")
print(df_historical.head().to_markdown(index=False, numalign="left", stralign="left"))
print("\n")
df_historical.info()
print("\nMissing values in historical_data.csv:")
print(df_historical.isnull().sum().to_markdown(numalign="left", stralign="left"))


print("\n--- Initial Inspection: fear_greed_index.csv ---")
print(df_fear_greed.head().to_markdown(index=False, numalign="left", stralign="left"))
print("\n")
df_fear_greed.info()
print("\nMissing values in fear_greed_index.csv:")
print(df_fear_greed.isnull().sum().to_markdown(numalign="left", stralign="left"))

# --- 2. Data Preprocessing and Cleaning ---
print("\n--- 2. Data Preprocessing and Cleaning ---")
# Convert 'Timestamp IST' in df_historical to datetime objects
df_historical['Timestamp IST'] = pd.to_datetime(df_historical['Timestamp IST'], format='%d-%m-%Y %H:%M')
# Extract only the date part for merging with the daily fear/greed index
df_historical['Date'] = df_historical['Timestamp IST'].dt.date

# Convert 'date' in df_fear_greed to datetime objects
df_fear_greed['date'] = pd.to_datetime(df_fear_greed['date'])

# Ensure the 'Date' column in df_historical is of datetime64[ns] type for proper merging
df_historical['Date'] = pd.to_datetime(df_historical['Date'])

print("\nFirst 5 rows of historical_data.csv after datetime conversion and adding 'Date' column:")
print(df_historical[['Timestamp IST', 'Date', 'Closed PnL']].head().to_markdown(index=False, numalign="left", stralign="left"))
print("\n")
df_historical.info()


print("\nFirst 5 rows of fear_greed_index.csv after datetime conversion:")
print(df_fear_greed.head().to_markdown(index=False, numalign="left", stralign="left"))
print("\n")
df_fear_greed.info()

# --- 3. Data Merging ---
print("\n--- 3. Data Merging ---")
df_merged = pd.merge(df_historical, df_fear_greed, left_on='Date', right_on='date', how='left')
df_merged.drop(columns=['date'], inplace=True) # Drop redundant 'date' column

print("\nFirst 5 rows of the merged dataframe:")
print(df_merged.head().to_markdown(index=False, numalign="left", stralign="left"))
print(f"\nShape of the merged dataframe: {df_merged.shape}")
print("\nMissing values in the merged dataframe (from fear_greed_index columns):")
print(df_merged[['value', 'classification']].isnull().sum().to_markdown(numalign="left", stralign="left"))
print(f"\nDate range of the merged dataset: {df_merged['Date'].min().date()} to {df_merged['Date'].max().date()}")
print("\nUnique sentiment classifications and their counts in the merged data:")
print(df_merged['classification'].value_counts().to_markdown(numalign="left", stralign="left"))


# --- 4. Exploratory Data Analysis (EDA) and Performance Metrics ---
print("\n--- 4. Exploratory Data Analysis (EDA) and Performance Metrics ---")

# Aggregate trader performance by sentiment classification
sentiment_performance = df_merged.groupby('classification').agg(
    Total_Closed_PnL=('Closed PnL', 'sum'),
    Average_Closed_PnL=('Closed PnL', 'mean'),
    Total_Trades=('Account', 'count'), # Count of rows represents total trades
    Average_Size_USD=('Size USD', 'mean')
).reset_index()

print("\nAggregated Trader Performance by Sentiment Classification:")
print(sentiment_performance.to_markdown(index=False, numalign="left", stralign="left"))

# Visualize Average Closed PnL by Classification
plt.figure(figsize=(10, 6))
sns.barplot(x='classification', y='Average_Closed_PnL', data=sentiment_performance, palette='viridis')
plt.title('Average Closed PnL by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Average Closed PnL')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('average_pnl_by_sentiment.png') # Save plot
plt.close() # Close plot to prevent display issues in some environments


# Visualize Total Trades by Classification
plt.figure(figsize=(10, 6))
sns.barplot(x='classification', y='Total_Trades', data=sentiment_performance, palette='magma')
plt.title('Total Trades by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Total Number of Trades')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('total_trades_by_sentiment.png') # Save plot
plt.close()


# Visualize Average Size USD by Classification
plt.figure(figsize=(10, 6))
sns.barplot(x='classification', y='Average_Size_USD', data=sentiment_performance, palette='cividis')
plt.title('Average Trade Size (USD) by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Average Trade Size (USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('average_trade_size_by_sentiment.png') # Save plot
plt.close()

# Further explore the distribution of Closed PnL for each classification using box plots
plt.figure(figsize=(12, 7))
sns.boxplot(x='classification', y='Closed PnL', data=df_merged, palette='plasma')
plt.title('Distribution of Closed PnL by Market Sentiment')
plt.xlabel('Market Sentiment Classification')
plt.ylabel('Closed PnL')
plt.ylim(-1000, 1000) # Limit y-axis for better visualization of main distribution, ignoring extreme outliers
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('pnl_distribution_boxplot.png') # Save plot
plt.close()

# --- 5. Uncovering Hidden Patterns ---
print("\n--- 5. Uncovering Hidden Patterns ---")

# PnL Distribution within each sentiment - Descriptive statistics and Skewness
print("\nDescriptive statistics of Closed PnL by Market Sentiment:")
print(df_merged.groupby('classification')['Closed PnL'].describe().to_markdown(numalign="left", stralign="left"))

print("\nSkewness of Closed PnL by Market Sentiment:")
print(df_merged.groupby('classification')['Closed PnL'].apply(lambda x: x.skew()).to_markdown(numalign="left", stralign="left"))

# Account-level performance by sentiment
account_sentiment_performance = df_merged.groupby(['Account', 'classification']).agg(
    Total_Closed_PnL=('Closed PnL', 'sum'),
    Average_Closed_PnL=('Closed PnL', 'mean'),
    Trades_Count=('Account', 'count')
).reset_index()

print("\nTop 5 Accounts by Total Closed PnL during Extreme Greed:")
print(account_sentiment_performance[account_sentiment_performance['classification'] == 'Extreme Greed'] \
      .sort_values(by='Total_Closed_PnL', ascending=False).head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nBottom 5 Accounts by Total Closed PnL during Extreme Greed:")
print(account_sentiment_performance[account_sentiment_performance['classification'] == 'Extreme Greed'] \
      .sort_values(by='Total_Closed_PnL', ascending=True).head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nTop 5 Accounts by Total Closed PnL during Fear:")
print(account_sentiment_performance[account_sentiment_performance['classification'] == 'Fear'] \
      .sort_values(by='Total_Closed_PnL', ascending=False).head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nBottom 5 Accounts by Total Closed PnL during Fear:")
print(account_sentiment_performance[account_sentiment_performance['classification'] == 'Fear'] \
      .sort_values(by='Total_Closed_PnL', ascending=True).head().to_markdown(index=False, numalign="left", stralign="left"))

# Trade side analysis: Average Closed PnL by Side and Classification
side_pnl = df_merged.groupby(['classification', 'Side']).agg(
    Average_Closed_PnL=('Closed PnL', 'mean'),
    Total_Trades=('Account', 'count')
).reset_index()

print("\nAverage Closed PnL and Total Trades by Market Sentiment and Trade Side:")
print(side_pnl.to_markdown(index=False, numalign="left", stralign="left"))

# Coin type analysis: Average Closed PnL by Coin and Classification
coin_pnl = df_merged.groupby(['classification', 'Coin']).agg(
    Average_Closed_PnL=('Closed PnL', 'mean'),
    Total_Trades=('Account', 'count')
).reset_index()

print("\nAverage Closed PnL and Total Trades by Market Sentiment and Coin Type:")
print(coin_pnl.to_markdown(index=False, numalign="left", stralign="left"))
