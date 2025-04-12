import cv2
import numpy as np

class ThermalImaging:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

    def capture_image(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture image")
        return frame

    def process_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        return heatmap

    def save_image(self, image, filename):
        cv2.imwrite(filename, image)

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
