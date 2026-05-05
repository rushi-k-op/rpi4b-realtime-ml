import pandas as pd
import matplotlib.pyplot as plt

# Load the data
powersave = pd.read_csv('powersave_test_data.csv')
ondemand  = pd.read_csv('ondemand_test_data.csv')
performance = pd.read_csv('performance_test_data.csv')

# Plot Core 0 frequency (GHz) vs time for each mode
plt.figure(figsize=(10, 5))

plt.plot(powersave['Time_Seconds'], powersave['Core_0_GHz'],
         label='Powersave', linewidth=2)
plt.plot(ondemand['Time_Seconds'], ondemand['Core_0_GHz'],
         label='Ondemand', linewidth=2)
plt.plot(performance['Time_Seconds'], performance['Core_0_GHz'],
         label='Performance', linewidth=2)

plt.xlabel('Time (seconds)')
plt.ylabel('Core 0 Frequency (GHz)')
plt.title('CPU Frequency vs Time – Governor Comparison')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
