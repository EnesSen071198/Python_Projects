

import cv2
import numpy as np
import pyttsx3

# Haar Cascade dosyaları
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
# Maske ve yaş/cinsiyet için model dosyaları (örnek, gerçek model dosyaları eklenmeli)
# mask_cascade = cv2.CascadeClassifier('mask_cascade.xml')


# Yaş ve cinsiyet tahmini için model dosyalarının yolu
age_proto = "models/deploy_age.prototxt"
age_model = "models/age_net.caffemodel"
gender_proto = "models/deploy_gender.prototxt"
gender_model = "models/gender_net.caffemodel"

AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
GENDER_LIST = ['Male', 'Female']

# Model dosyaları varsa yaş/cinsiyet tahmini aktif
import os
age_gender_enabled = all(os.path.exists(p) for p in [age_proto, age_model, gender_proto, gender_model])
if age_gender_enabled:
    age_net = cv2.dnn.readNet(age_model, age_proto)
    gender_net = cv2.dnn.readNet(gender_model, gender_proto)

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
face_count_prev = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    face_count = len(faces)
    # Yüz sayısını ekrana yaz
    cv2.putText(frame, f"Face Count: {face_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # Yüz sayısı değişirse sesli uyarı
    if face_count != face_count_prev:
        engine.say(f"{face_count} face detected")
        engine.runAndWait()
        face_count_prev = face_count
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # Gözlük tespiti
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cv2.putText(frame, "Glasses", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        # Maske tespiti (örnek, gerçek model dosyası eklenmeli)
        # mask = mask_cascade.detectMultiScale(roi_gray)
        # if len(mask) > 0:
        #     cv2.putText(frame, "Mask", (x, y + h + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        # Yaş ve cinsiyet tahmini
        if age_gender_enabled:
            face_img = frame[y:y+h, x:x+w].copy()
            blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), [104, 117, 123], swapRB=False)
            gender_net.setInput(blob)
            gender_preds = gender_net.forward()
            gender = GENDER_LIST[gender_preds[0].argmax()]
            age_net.setInput(blob)
            age_preds = age_net.forward()
            age = AGE_LIST[age_preds[0].argmax()]
            cv2.putText(frame, f"{gender}, {age}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
        else:
            cv2.putText(frame, "Human", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
