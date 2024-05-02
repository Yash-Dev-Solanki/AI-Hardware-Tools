import numpy as np
import cv2
import time
import serial
from keras.utils import img_to_array
from keras.models import model_from_json

# Serial port initialization
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600)

# OpenCV initialization
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam_port = 2
cap = cv2.VideoCapture(cam_port)

# Face expression recognizer initialization
model = model_from_json(open("facial_expression_model_structure.json", "r").read())
model.load_weights('facial_expression_model_weights.h5')

emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')

# map emotions to serial output
emotion_map = {'angry': 'S', 'disgust': 'S', 'fear': 'A', 'happy': 'H', 'sad': 'S', 'surprise': 'H', 'neutral': 'N'}

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        detected_face = gray[y:y + h, x:x + w]
        detected_face = cv2.resize(detected_face, (48, 48))

        img_pixels = img_to_array(detected_face)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)
        max_index = np.argmax(predictions[0])
        emotion = emotions[max_index]
        cv2.putText(img, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        # Send 'H' if happy emotion is detected
        ser_data = bytes(emotion_map[emotion], 'utf-8')
        print(ser_data)
        ser.write(ser_data)

        time.sleep(0.5)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
