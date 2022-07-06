# -*- coding: utf-8 -*-


import cv2
import base64 



def find(encoded_string,finish_file):
    base64_image = str.encode(encoded_string)
    #save image locally

    with open("new_py.png", "wb") as fh:
        fh.write(base64.decodebytes(base64_image))
    
    image_path = "new_py.png"
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor= 1.08,
        minNeighbors= 6,
        minSize=(10, 10)
    )
    faces_detected = "Лиц обнаружено: " + format(len(faces))
    print(faces_detected)
    # Рисуем квадраты вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
    cv2.putText(image, faces_detected, (20,60), cv2.FONT_HERSHEY_COMPLEX, 2, 3, 2)

    cv2.imwrite(finish_file, image)
    return image , faces_detected
    
    
    
    


    