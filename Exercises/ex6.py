"""
Create a Python Class where you calculate the degrees in Fahrenheit based on
the temperature in Celsius and vice versa.
"""

class TemperatureConverter:

    @staticmethod
    def c2f(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def f2c(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    celsius_temp = 25
    fahrenheit_temp = TemperatureConverter.c2f(celsius_temp)
    print(f"{celsius_temp}°C is {fahrenheit_temp}°F")

    fahrenheit_temp = 77
    celsius_temp = TemperatureConverter.f2c(fahrenheit_temp)
    print(f"{fahrenheit_temp}°F is {celsius_temp}°C")
