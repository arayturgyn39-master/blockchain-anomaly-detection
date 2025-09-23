# ==========================
# Exploratory Data Analysis
# Blockchain-style Fake Dataset
# ==========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate a fake dataset (like transactions)
np.random.seed(42)  # for reproducibility
n = 100

df = pd.DataFrame({
    "transaction_id": range(1, n+1),
    "user_id": np.random.randint(1, 21, size=n),  # 20 fake users
    "amount": np.round(np.random.exponential(50, size=n), 2),  # skewed distribution
    "category": np.random.choice(["payment", "transfer", "deposit", "withdrawal"], size=n)
})

# 2. First look at the dataset
print("First 5 rows:")
display(df.head())

print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
display(df.describe())

# 3. Simple analysis
# Count transactions by category
category_counts = df["category"].value_counts()
print("\nTransactions per category:")
print(category_counts)

# 4. Plot histogram of amounts
plt.figure(figsize=(8,5))
plt.hist(df["amount"], bins=20, edgecolor="black")
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

# 5. Transactions per user (top 5 users)
top_users = df["user_id"].value_counts().head(5)
print("\nTop 5 users by transaction count:")
print(top_users)

plt.figure(figsize=(8,5))
top_users.plot(kind="bar")
plt.title("Top 5 Users by Transaction Count")
plt.xlabel("User ID")
plt.ylabel("Number of Transactions")
plt.show()
