import face_recognition
import os
import cv2
import pickle
import time

def main(path):
    KNOWN_FACES_DIR = 'C:/Users/HeroW/PycharmProjects/untitled/Face/known_faces'
    # UNKNOWN_FACES_DIR = 'unknown_faces'
    TOLERANCE = 0.6
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = 'cnn'
    video = cv2.VideoCapture(path)

    print("loading known faces")
    known_faces = []
    known_names = []
    for name in os.listdir(KNOWN_FACES_DIR):
        # Next we load every file of faces of known person
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
            # Получить 128-мерную кодировку лица
            # Всегда возвращает список найденных лиц, для этого мы берем только первое лицо
            # (предполагается, что одно лицо на изображение, так как вы не можете быть дважды на одном изображении)
            # encoding = face_recognition.face_encodings(image)[0]
            encoding = pickle.load(open(f"{KNOWN_FACES_DIR}/{name}/{filename}", "rb"))
            # Добавить кодировки и имя
            known_faces.append(encoding)
            known_names.append(int(name))

    if len(known_names) > 0:
        next_id = max(known_names) + 1
    else:
        next_id = 0

    print('Processing unknown faces...')
    while True:

        ret, image = video.read()
        locations = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, locations)

        for face_encoding, face_location in zip(encodings, locations):
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = str(known_names[results.index(True)])
            
            else:
                match = str(next_id)
                next_id += 1
                known_names.append(match)
                known_faces.append(face_encoding)
                os.mkdir(f"{KNOWN_FACES_DIR}/{match}")
                pickle.dump(face_encoding, open(f"{KNOWN_FACES_DIR}/{match}/{match}-{int(time.time())}.pkl", "wb"))

            color = [0, 255, 0]
            # Создаем рамку
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
            # Создаем текст
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (200, 200, 200))

        cv2.imshow("", image)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break