import subprocess, time

print("Starting stress test and temperature logging...")

stress_process = subprocess.Popen(['stress', '--cpu', '4', '--timeout', '60'])

with open("temp_log_py.csv", "w") as file:
    file.write("time_s, temp_c\n")
    time.sleep(1)
    print("time_s, temp_c")
    
    for seconds in range(60):
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        temp_text = result.stdout
        temp_text = temp_text.replace("temp=", "")
        temp_text = temp_text.replace("'C\n", "")
        temp = float(temp_text)
        
        line = f"{seconds}, {temp:.1f}"
        print(line)
        file.write(line + "\n")
        
        time.sleep(1)

print("Test complete! Data saved to temp_log_py.csv")

time.sleep(1)
result = subprocess.run(['vcgencmd', 'get_throttled'], capture_output=True, text=True)
throttled = result.stdout.strip()
print(f"Throttled status: {throttled}")

if throttled == 'throttled=0x0':
  print("No throttling detected")
else:
  print("Throttling detected")
