import time
import csv

def get_cpu_freq(core_id):
    """Reads the current frequency of a specific core in GHz."""
    filepath = f"/sys/devices/system/cpu/cpu{core_id}/cpufreq/scaling_cur_freq"
    try:
        with open(filepath, "r") as f:
            # sysfs reports frequency in kHz. Divide by 1,000,000 to get GHz.
            return int(f.read().strip()) / 1000000.0
    except FileNotFoundError:
        return 0.0

def monitor_and_log(duration_seconds=30, filename="cpu_frequency_log.csv"):
    print(f"Monitoring frequencies. Data will be saved to '{filename}'...")
   
    # Open the file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
       
        # Write the header row
        writer.writerow(["Time_Seconds", "Core_0_GHz", "Core_1_GHz", "Core_2_GHz", "Core_3_GHz"])

        print(f"{'Time(s)':<10} | {'Core 0':<10} | {'Core 1':<10} | {'Core 2':<10} | {'Core 3':<10}")
        print("-" * 65)

        for i in range(duration_seconds):
            freqs = [get_cpu_freq(core) for core in range(4)]
           
            # Write to the CSV file
            writer.writerow([i+1, freqs[0], freqs[1], freqs[2], freqs[3]])
           
            # Print to the console
            print(f"{i+1:<10} | {freqs[0]:<10.3f} | {freqs[1]:<10.3f} | {freqs[2]:<10.3f} | {freqs[3]:<10.3f}")
           
            time.sleep(1)
           
    print("Logging complete.")

if __name__ == "__main__":
    # You can change the '30' to any number of seconds you want to record
    monitor_and_log(30)
