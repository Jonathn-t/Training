import matplotlib.pyplot as plt

# Read the data from the file
times = []
temperatures = []

with open("Exercises/ex7/myfile.txt", "r") as f:
    next(f)  # Skip the header
    for line in f:
        time_value, temperature = line.split()
        times.append(int(time_value))
        temperatures.append(int(temperature))

# Plot the data
plt.plot(times, temperatures, marker='o')
plt.title("Temperature Readings Over Time")
plt.xlabel("Time (every 10 seconds)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
