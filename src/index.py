import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
recognition = mp.solutions.face_detection
r = recognition.FaceDetection()

desenho = mp.solutions.drawing_utils

while True:
    verificador, frame = webcam.read()

    if not verificador:
        break

    list_face = r.process(frame)

    if list_face.detections:
        for face in list_face.detections:
            desenho.draw_detection(frame, face)

    cv2.imshow("Reconhecimento de face", frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()