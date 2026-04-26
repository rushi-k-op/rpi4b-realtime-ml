"""
plot_temp.py — Plot temperature logs from temp_log.csv and temp_log_py.csv

Usage:
    python3 plot_temp.py

Outputs:
    temp_plot.png  (saved in the same directory)
"""

import pandas as pd
import matplotlib.pyplot as plt
import re

# ── Load temp_log.csv ─────────────────────────────────────────────────────────
# Format: timestamp (HH:MM:SS), temp string like "temp=57.4'C"
df1 = pd.read_csv("temp_log.csv", header=None, names=["time", "temp_raw"])
df1["temp_c"] = df1["temp_raw"].str.extract(r"([\d.]+)").astype(float)
df1["time"] = pd.to_datetime(df1["time"], format="%H:%M:%S")

# ── Load temp_log_py.csv ──────────────────────────────────────────────────────
# Format: time_s (elapsed seconds), temp_c (float)
df2 = pd.read_csv("temp_log_py.csv")
df2.columns = df2.columns.str.strip()   # strip any accidental whitespace
df2.rename(columns={"temp_c": "temp_c"}, inplace=True)  # normalize

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 1, figsize=(10, 7))
fig.suptitle("Temperature Logs", fontsize=14, fontweight="bold")

# Top: temp_log.csv — real timestamps on x-axis
axes[0].plot(df1["time"], df1["temp_c"], color="tab:red", linewidth=1.5, marker="o", markersize=3)
axes[0].set_title("temp_log.csv")
axes[0].set_xlabel("Time (HH:MM:SS)")
axes[0].set_ylabel("Temperature (°C)")
axes[0].tick_params(axis="x", rotation=45)
axes[0].grid(True, linestyle="--", alpha=0.5)

# Bottom: temp_log_py.csv — elapsed seconds on x-axis
axes[1].plot(df2["time_s"], df2["temp_c"], color="tab:blue", linewidth=1.5, marker="o", markersize=3)
axes[1].set_title("temp_log_py.csv")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Temperature (°C)")
axes[1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("temp_plot.png", dpi=150)
print("Saved: temp_plot.png")
plt.show()
