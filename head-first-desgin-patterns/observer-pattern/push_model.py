from abc import ABC, abstractmethod

# The push model below has disadvantages. If the update method has a new measurement such as wind speed
# all classes with the update method will have to be changed. Also, not all displays might need all
# measurements. Thus, we implemented the pull model. This will allow individual displays to get the 
# metrics they need from the subject i.e. WeatherData

class Observer(ABC):

    @abstractmethod
    def update(self, t: float, h: float, p: float) -> None:
        pass

class Subject(ABC):

    @abstractmethod
    def add_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)
    
    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurement_changed(self, t : float, h: float, p: float) -> None:
        self.temperature = t
        self.humidity = h
        self.pressure = p
        self.notify_observers()


class CurrentDisplay(Observer):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.add_observer(self)

    def update(self, t: float, h: float, p: float) -> None:
        self.display(t, h, p)

    def display(self, t: float, h: float, p: float) -> None:
        print(f"CurrentDisplay - Temperature: {t}, humidity: {h}, pressure: {p}")


class ForecastDisplay(Observer):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.add_observer(self)

    def update(self, t: float, h: float, p: float) -> None:
        self.display(t, h, p)

    def display(self, t: float, h: float, p: float) -> None:
        print(f"ForecastDisplay - Temperature: {t}, humidity: {h}, pressure: {p}")
    

class MetricsDisplay(Observer):

    def __init__(self, weather_data: WeatherData):
        self.weather_data = weather_data
        self.weather_data.add_observer(self)

    def update(self, t: float, h: float, p: float) -> None:
        self.display(t, h, p)

    def display(self, t: float, h: float, p: float) -> None:
        print(f"MetricsDisplay - Temperature: {t}, humidity: {h}, pressure: {p}")

def main():
    weather_data = WeatherData()
    current_display = CurrentDisplay(weather_data=weather_data)
    forecast_display = ForecastDisplay(weather_data=weather_data)
    metrics_display = MetricsDisplay(weather_data=weather_data)
    weather_data.measurement_changed(1.0, 1.0, 1.0)
    weather_data.measurement_changed(2.0, 2.0, 2.0)
    weather_data.measurement_changed(3.0, 3.0, 3.0)
    
    print(f"----------------------------------------")

    weather_data.remove_observer(current_display)
    weather_data.measurement_changed(4.0, 4.0, 4.0)

if __name__ == "__main__":
    main()



    