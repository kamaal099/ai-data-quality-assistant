```python
import pandas as pd

# Load dataset
df = pd.read_csv('dataset.csv')

# Drop rows with missing CustomerID values
df = df.dropna(subset=['CustomerID'])

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with negative Quantity values
df = df[df['Quantity'] >= 0]

# Remove outliers in UnitPrice (assuming outliers are defined as values outside 1.5 times the IQR)
Q1 = df['UnitPrice'].quantile(0.25)
Q3 = df['UnitPrice'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['UnitPrice'] >= (Q1 - 1.5 * IQR)) & (df['UnitPrice'] <= (Q3 + 1.5 * IQR))]

# Convert InvoiceDate to datetime dtype
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Reset index after cleaning
df.reset_index(drop=True, inplace=True)

# Save cleaned dataset if needed
# df.to_csv('cleaned_dataset.csv', index=False)
```