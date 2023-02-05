import cv2
import mediapipe as mp



# img = cv2.imread('person.jpg')
# cv2.imshow('title', img)
# cv2.waitKey(0)


cap = cv2.VideoCapture('person.mp4')

mp_fd = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils
fd = mp_fd.FaceDetection()

while True:
    success, img = cap.read()
    if success:
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face = fd.process(from_bgr_to_rgb)
        
        if face.detections:
            for id, detection in enumerate(face.detections):
                mp_draw.draw_detection(img, detection)

        cv2.imshow('title', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

