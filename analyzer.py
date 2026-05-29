import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

print("Basic statistics")
print(df.describe())

plt.plot(df["frequency"], df["voltage"], marker="o")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Voltage [V]")
plt.title("Frequency Response")
plt.grid(True)
plt.show()
