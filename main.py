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
distance_hamilton = hamilton['Distance']

# Plot the data
fig, ax = plt.subplots()
ax.plot(distance_hamilton, speed_hamilton, label='Hamilton', color=plotting.driver_color('ham'))
ax.set_xlabel('Distance [m]')
ax.set_ylabel('Speed [km/h]')
fig.set_size_inches(16, 9)
fig.set_dpi(100)

plt.show()
