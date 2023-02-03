import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

ff1.Cache.enable_cache('./cache')
# FastF1's default color scheme
ff1.plotting.setup_mpl()

session = ff1.get_session(2021, 'Monaco', 'Q')
session.load(telemetry=True)
pilot_data = session.laps.pick_driver('HAM').pick_fastest().get_car_data().add_distance()
print(pilot_data['Driver'])
