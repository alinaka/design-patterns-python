from typing import List
from contextlib import suppress


class Observer:
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        raise NotImplementedError


class Subject:
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError

    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError

    def notify_observers(self) -> None:
        raise NotImplementedError


class DisplayElement:
    def display(self) -> None:
        raise NotImplementedError


class WeatherData(Subject):
    observers: List[Observer]
    temperature: float
    humidity: float
    pressure: float

    def __init__(self):
        self.observers = []

    def register_observer(self, o: Observer) -> None:
        self.observers.append(o)

    def remove_observer(self, o: Observer) -> None:
        with suppress(ValueError):
            self.observers.remove(o)

    def notify_observers(self) -> None:
        for i in range(len(self.observers)):
            obs: Observer = self.observers[i]
            obs.update(self.temperature, self.humidity, self.pressure)

    def measurements_changes(self) -> None:
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changes()


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature: float
    humidity: float
    weather_data: Subject

    def __init__(self, weather_data: Subject):
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")


def main():
    weather_data: WeatherData = WeatherData()
    current_display: CurrentConditionsDisplay = CurrentConditionsDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == "__main__":
    main()
