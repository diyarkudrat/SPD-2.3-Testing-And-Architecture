class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def register_observer(observer):
        pass

    def remove_observer(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notify_observers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.


class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def register_observer(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def remove_observer(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notify_observers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notifyObservers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurements_changed()

    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):

    def __init__(self, weather_data):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0

        self.weather_data = weather_data  # save the ref in an attribute.
        weather_data.register_observer(self)  # register the observer
        # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions:", self.temerature,
              "F degrees and", self.humidity, "[%] humidity",
              "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.


class StatisticsDisplay:
    """The StatisticsDisplay class keeps track of the min/max/average measurements and display time."""

    def __init__(self, weather_data):
        self.temps = []
        self.humidities = []
        self.pressures = []
        self.weather_data = weather_data

        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        # add measurements to records
        self.temps.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)

        self.display()

    def get_stats(self, units):
        """Return min, max, and average of a list"""
        if units == "F degrees":
            vals = self.temps
            measurement = "temp"
        elif units == "[%]":
            vals = self.humidities
            measurement = "humidity"
        else:
            vals = self.pressures
            measurement = "pressure"

        message = (
            f"Min {measurement} : {min(values)} {units}"
            + f"Avg {measurement} : {max(values)} {units}"
            + f"Max {measurement} : {sum(values) / len(values)} {units}"
        )

        return message

    def display(self):
        if len(self.temps) > 0:
            temp_message = self.get_stats("F degrees")
        else:
            temp_message = "No Temp Stats"

        print(temp_message)

        if len(self.humidities) > 0:
            humidity_message = self.get_stats("[%]")
        else:
            humidity_message = "No Humidity Stats"

        print(humidity_message)

        if len(self.pressures) > 0:
            pressure_message = self.get_stats("")
        else:
            pressure_message = "No Pressure Stats"

        print(pressure_message)


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)

        # TODO: Create two objects from StatisticsDisplay class and
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.

        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.

        # The ForecastDisplay class shows the weather forcast based on the current
        # temperature, humidity and pressure. Use the following formuals :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100, 1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
