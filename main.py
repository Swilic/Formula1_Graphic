import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

ff1.Cache.enable_cache('./cache')
# FastF1's default color scheme
ff1.plotting.setup_mpl()


def get_weather_data(place, year=2023, session='Q'):
    """
    Function to get the weather data from a session.
    """
    session = ff1.get_session(year, place, session)
    session.load(telemetry=True)
    weather_data = session.laps.pick_fastest().get_weather_data()

    return weather_data


def get_pilot_data(place, pilot, year, session='Q'):
    """
    Function to get the data from a session.
    """
    session = ff1.get_session(year, place, session)
    session.load(telemetry=True)
    pilot_data = session.laps.pick_driver(pilot).pick_fastest().get_car_data().add_distance()

    return pilot_data


def make_graphic(first_pilot, second_pilot, place, year):
    """
     Function to make the graphic comparison between two pilots, on the quali day from their best lap.
    """
    # Get the drivers data
    pilot1 = get_pilot_data(place=place, pilot=first_pilot, year=year)
    pilot2 = get_pilot_data(place=place, pilot=second_pilot, year=year)
    pilot1_laptime = pilot1['Time'].iloc[-1]
    pilot2_laptime = pilot2['Time'].iloc[-1] - pilot2['Time'].iloc[0]
    print(f"{first_pilot} laptime: {pilot1_laptime}")
    weather = get_weather_data(place=place, year=year)

    # Plot the data
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
    # Plot the speed
    ax1.plot(pilot1['Distance'], pilot1['Speed'], label=first_pilot, color=plotting.driver_color(first_pilot))
    ax1.plot(pilot2['Distance'], pilot2['Speed'], label=second_pilot, color=plotting.driver_color(second_pilot))
    ax1.legend(loc='lower right')
    ax1.set_xlabel('Distance [m]')
    ax1.set_ylabel('Speed [km/h]')

    # Plot the throttle
    ax2.plot(pilot1['Distance'], pilot1['Throttle'], label=first_pilot, color=plotting.driver_color(first_pilot))
    ax2.plot(pilot2['Distance'], pilot2['Throttle'], label=second_pilot, color=plotting.driver_color(second_pilot))
    ax2.set_xlabel('Distance [m]')
    ax2.set_ylabel('Throttle [%]')

    # Plot the break
    ax3.plot(pilot1['Distance'], pilot1['Brake'], label=first_pilot, color=plotting.driver_color(first_pilot))
    ax3.plot(pilot2['Distance'], pilot2['Brake'], label=second_pilot, color=plotting.driver_color(second_pilot))
    ax3.set_xlabel('Distance [m]')
    ax3.set_ylabel('Break')

    # Plot the gear
    ax4.step(pilot1['Distance'], pilot1['nGear'], label=first_pilot, color=plotting.driver_color(first_pilot))
    ax4.step(pilot2['Distance'], pilot2['nGear'], label=second_pilot, color=plotting.driver_color(second_pilot))
    ax4.set_xlabel('Distance [m]')
    ax4.set_ylabel('Gear [number]')

    # Set the limits of the y-axis and the ticks
    ax4.set(ylim=(1, 9), yticks=[i+1 for i in range(9)])

    # Uniform the x-axis
    for ax in plt.gcf().axes:
        ax.margins(x=0.05, y=0.1)
        ax.label_outer()

    # Qualifying info
    fig.text(x=0.05, y=0.95, s="Testing but it's long")
    fig.suptitle(f"{place} {year} Qualifying!")
    # Figure info
    fig.set_size_inches(16, 9)
    fig.set_dpi(300)
    fig.savefig('plot.png')

    plt.show()


if __name__ == '__main__':
    first_pilot = 'HAM'
    second_pilot = 'BOT'
    place = 'Monaco'
    year = 2021

    make_graphic(first_pilot, second_pilot, place, year)
