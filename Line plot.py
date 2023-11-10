import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("world-data-2023.csv")

data["Armed Forces size"] = data["Armed Forces size"].astype(str)

# Sort the data by army size
data = data.sort_values(by="Armed Forces size", ascending=False)

top_10_countries = data.head(10)

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(data["Country"], data["Armed Forces size"])
plt.xlabel("Country")
plt.ylabel("Armed Forces size")
plt.title("Armed Forces size of All Countries in the Global Country Information Dataset 2023")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()