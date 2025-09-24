import pandas as pd

# Sample dataset
data = {
    "Name": ["Ali", "Aisha", "John", "Sara", None],
    "Age": [25, 30, None, 22, 28],
    "City": ["Almaty", "Astana", "London", None, "Dubai"]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Handle missing values
df_cleaned = df.fillna({"Name": "Unknown", "Age": df["Age"].mean(), "City": "Not Specified"})

print("\nCleaned Data:")
print(df_cleaned)

# Save to CSV
df_cleaned.to_csv("cleaned_data.csv", index=False)
