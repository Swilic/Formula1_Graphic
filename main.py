import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

ff1.Cache.enable_cache('./cache')
# FastF1's default color scheme
ff1.plotting.setup_mpl()

# Get the data
session = ff1.get_session(2021, 'Austria', 'Q')
session.load(telemetry=True)
hamilton = session.laps.pick_driver('HAM').pick_fastest().get_car_data().add_distance()
speed_hamilton = hamilton['Speed']
throttle_hamilton = hamilton['Throttle']
break_hamilton = hamilton['Brake']
gear_hamilton = hamilton['nGear']
distance_hamilton = hamilton['Distance']

# Plot the data
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
# Plot the speed
ax1.plot(distance_hamilton, speed_hamilton, label='Hamilton', color=plotting.driver_color('ham'))
ax1.set_xlabel('Distance [m]')
ax1.set_ylabel('Speed [km/h]')
# Plot the throttle
ax2.plot(distance_hamilton, throttle_hamilton, label='Hamilton', color=plotting.driver_color('ham'))
ax2.set_xlabel('Distance [m]')
ax2.set_ylabel('Throttle [%]')
# Plot the break
ax3.plot(distance_hamilton, break_hamilton, label='Hamilton', color=plotting.driver_color('ham'))
ax3.set_xlabel('Distance [m]')
ax3.set_ylabel('Break')
# Plot the gear
ax4.step(distance_hamilton, gear_hamilton, label='Hamilton', color=plotting.driver_color('ham'))
ax4.set_xlabel('Distance [m]')
ax4.set_ylabel('Gear [number]')
# Set the limits of the y-axis and the ticks
ax4.set(ylim=(1, 9), yticks=[i+1 for i in range(9)])

# Uniform the x-axis
for ax in plt.gcf().axes:
    ax.margins(x=0.05, y=0.1)
    ax.label_outer()

fig.set_size_inches(16, 9)
fig.set_dpi(300)
fig.savefig('plot.png')

plt.show()
