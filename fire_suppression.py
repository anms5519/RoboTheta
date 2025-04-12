import RPi.GPIO as GPIO
import time

class FireSuppression:
    def __init__(self, pump_pin, valve_pin):
        self.pump_pin = pump_pin
        self.valve_pin = valve_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pump_pin, GPIO.OUT)
        GPIO.setup(self.valve_pin, GPIO.OUT)

    def activate_pump(self):
        GPIO.output(self.pump_pin, GPIO.HIGH)

    def deactivate_pump(self):
        GPIO.output(self.pump_pin, GPIO.LOW)

    def open_valve(self):
        GPIO.output(self.valve_pin, GPIO.HIGH)

    def close_valve(self):
        GPIO.output(self.valve_pin, GPIO.LOW)

    def suppress_fire(self, duration):
        self.activate_pump()
        self.open_valve()
        time.sleep(duration)
        self.close_valve()
        self.deactivate_pump()

    def cleanup(self):
        GPIO.cleanup()
