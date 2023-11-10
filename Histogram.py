import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("world-data-2023.csv")

data["Armed Forces size"] = data["Armed Forces size"].astype(str)

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(data["Armed Forces size"], bins=100, edgecolor="black")
plt.xlabel("Armed Forces size")
plt.ylabel("Number of countries")
plt.title("Histogram of Armed Forces Size in the Global Country Information Dataset 2023")
plt.tight_layout()
plt.show()