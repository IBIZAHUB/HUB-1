import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [20, 22, 19, 23, 21, 24, 20]

plt.plot(days, temps, marker='o')
plt.title("Weekly Temperature Readings")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()