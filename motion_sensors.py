import RPi.GPIO as GPIO
import time

class MotionSensors:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def detect_motion(self):
        return GPIO.input(self.pin)

    def log_motion(self, filename):
        motion_detected = self.detect_motion()
        with open(filename, 'a') as file:
            file.write(f"Motion detected: {motion_detected}\n")

    def cleanup(self):
        GPIO.cleanup()
