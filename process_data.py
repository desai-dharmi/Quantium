import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

df = pd.concat([pd.read_csv(file) for file in files])

df = df[df["product"] == "pink morsel"]

df["price"] = (
    df["price"]
    .replace("[$]", "", regex=True)
    .astype(float)
)

df["sales"] = df["price"] * df["quantity"]

output = df[["sales", "date", "region"]]

output.columns = ["Sales", "Date", "Region"]

output.to_csv("output.csv", index=False)

print("output.csv created successfully!")