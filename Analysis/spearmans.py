from scipy.stats import spearmanr
import pandas as pd
import matplotlib.pyplot as plt

# read the excel file and store in a pandas dataframe
df = pd.read_excel("Green Space x IMD Analysis.xlsx")

print(df.head())    # check that it is reading the file
print(df.columns)

rho, p_value = spearmanr(   # calculate spearman correlation
    df["Avg IMD Score"], 
    df["Sites per capita"])

print(f"Spearman rho: {rho:.2f}")
print(f"p-value: {p_value:.3f}")

plt.scatter(
    df["Avg IMD Score"],
    df["Sites per capita"]
)

plt.xlabel("Mean IMD Score (higher = more deprived)")
plt.ylabel("No. of distinct public spaces per capita")
plt.title("Green Space Access vs Deprivation (Borough Level)")

plt.show()