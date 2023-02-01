import fastf1 as ff1
from fastf1 import plotting
from fastf1 import plotting

ff1.Cache.enable_cache('cache_dir')

# Get the data
laps = ff1.get_session(2021, 'Austria', 'Q').load_laps(with_telemetry=True)
