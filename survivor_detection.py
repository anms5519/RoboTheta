import cv2
import numpy as np

class SurvivorDetection:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(camera_index)

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            raise Exception("Failed to capture frame")
        return frame

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detect_faces(gray)
        return faces

    def detect_faces(self, gray_frame):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        return faces

    def detect_survivors(self):
        while True:
            frame = self.capture_frame()
            faces = self.process_frame(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('Survivor Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()
