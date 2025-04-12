import time
from thermal_imaging import ThermalImaging
from gas_detection import GasDetection
from motion_sensors import MotionSensors
from fire_suppression import FireSuppression
from autonomous_navigation import AutonomousNavigation
from survivor_detection import SurvivorDetection

class EmergencyResponse:
    def __init__(self):
        self.thermal_imaging = ThermalImaging()
        self.gas_detection = GasDetection(sensor='DHT22', pin=4)
        self.motion_sensors = MotionSensors(pin=17)
        self.fire_suppression = FireSuppression(pump_pin=18, valve_pin=23)
        self.autonomous_navigation = AutonomousNavigation()
        self.survivor_detection = SurvivorDetection()

    def monitor_environment(self):
        while True:
            try:
                thermal_image = self.thermal_imaging.capture_image()
                gas_detected = self.gas_detection.detect_gas(threshold=50)
                motion_detected = self.motion_sensors.detect_motion()
                survivors = self.survivor_detection.detect_survivors()

                if gas_detected:
                    print("Gas detected! Initiating fire suppression.")
                    self.fire_suppression.suppress_fire(duration=10)

                if motion_detected:
                    print("Motion detected! Navigating to the location.")
                    self.autonomous_navigation.navigate()

                if survivors:
                    print("Survivors detected! Initiating rescue operation.")
                    # Add rescue operation logic here

                time.sleep(1)

            except KeyboardInterrupt:
                print("Emergency response terminated.")
                break

    def cleanup(self):
        self.thermal_imaging.release_camera()
        self.survivor_detection.release_camera()
        self.fire_suppression.cleanup()
        self.motion_sensors.cleanup()
