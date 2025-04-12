import Adafruit_DHT
import time

class GasDetection:
    def __init__(self, sensor, pin):
        self.sensor = sensor
        self.pin = pin

    def read_gas_level(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is None or temperature is None:
            raise Exception("Failed to read from sensor")
        return humidity, temperature

    def detect_gas(self, threshold):
        humidity, temperature = self.read_gas_level()
        if humidity > threshold:
            return True
        return False

    def log_gas_level(self, filename):
        humidity, temperature = self.read_gas_level()
        with open(filename, 'a') as file:
            file.write(f"Humidity: {humidity}, Temperature: {temperature}\n")
