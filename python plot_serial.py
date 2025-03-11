import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
from datetime import datetime, timedelta

SERIAL_PORT = "COM7"  # Update this if needed
ser = serial.Serial(SERIAL_PORT, 9600, timeout=1)

time_data = []
temperature_data = []
pressure_data = []
altitude_data = []

fig, ax = plt.subplots(3, 1, figsize=(8, 6))
ax[0].set_title("Temperature (°C)")
ax[1].set_title("Pressure (hPa)")
ax[2].set_title("Altitude (m)")

temp_line, = ax[0].plot([], [], 'r-', label="Temperature")
pressure_line, = ax[1].plot([], [], 'b-', label="Pressure")
altitude_line, = ax[2].plot([], [], 'g-', label="Altitude")

temp_text = ax[0].text(0.02, 0.90, '', transform=ax[0].transAxes, fontsize=12, color='red')
pressure_text = ax[1].text(0.02, 0.90, '', transform=ax[1].transAxes, fontsize=12, color='blue')
altitude_text = ax[2].text(0.02, 0.90, '', transform=ax[2].transAxes, fontsize=12, color='green')

def get_current_time():
    """Returns the current desktop time"""
    return datetime.now()  # Use system (desktop) time

def update(frame):
    try:
        line = ser.readline().decode('utf-8').strip()
        values = line.split(',')
        if len(values) != 3:
            return  # Skip invalid data

        temp = float(values[0])
        pressure = float(values[1])
        altitude = float(values[2])

        current_time = get_current_time()  # Use desktop time
        time_data.append(current_time)
        temperature_data.append(temp)
        pressure_data.append(pressure)
        altitude_data.append(altitude)

        # Keep only the last 30 seconds of data
        cutoff_time = current_time - timedelta(seconds=30)
        while time_data and time_data[0] < cutoff_time:
            time_data.pop(0)
            temperature_data.pop(0)
            pressure_data.pop(0)
            altitude_data.pop(0)

        # Update plots
        temp_line.set_data(time_data, temperature_data)
        pressure_line.set_data(time_data, pressure_data)
        altitude_line.set_data(time_data, altitude_data)

        ax[0].set_xlim(cutoff_time, current_time)
        ax[1].set_xlim(cutoff_time, current_time)
        ax[2].set_xlim(cutoff_time, current_time)

        for a in ax:
            a.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
            a.xaxis.set_major_locator(mdates.SecondLocator(interval=5))
            a.relim()
            a.autoscale_view()

        plt.xticks(rotation=45)

        # Update text labels
        temp_text.set_text(f"Current: {temp:.2f}°C")
        pressure_text.set_text(f"Current: {pressure:.2f} hPa")
        altitude_text.set_text(f"Current: {altitude:.2f} m")

    except Exception as e:
        print("⚠️ Update Error:", e)

ani = animation.FuncAnimation(fig, update, interval=500)
plt.tight_layout()
plt.show()
