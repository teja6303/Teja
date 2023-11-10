import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("world-data-2023.csv")

data["Armed Forces size"] = pd.to_numeric(data["Armed Forces size"], errors="coerce")

# Create the boxplot
plt.figure(figsize=(10, 6))
plt.boxplot(data["Armed Forces size"], notch=True, patch_artist=True)
plt.xlabel("Country")
plt.ylabel("Armed Forces size")
plt.title("Distribution of Armed Forces Size in the Global Country Information Dataset 2023")
plt.tight_layout()
plt.show()

