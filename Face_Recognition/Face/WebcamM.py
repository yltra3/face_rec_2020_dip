import face_recognition
import cv2
import numpy as np

# Указание пути к вебкамере
video_capture = cv2.VideoCapture(0)

# Загрузка эталона и обучение его распознаванию
obama_image = face_recognition.load_image_file("./img/known/Vlad.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Загрузка ещё одного эталона.
biden_image = face_recognition.load_image_file("./img/known/Elon Musk.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Создание массивов распознаваний и имён
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Vlad",
    "Elon Musk"
]

while True:
    # Забор одного кадра видео
    ret, frame = video_capture.read()

    # Конвертирование из BGR цвета (который используется OpenCV) в RGB цвет (который использует face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Нахождение всех лиц и распознавание на видео
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Цикл каждого лица в этом кадре видео
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Проверка на совпадение)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        #     Если совпадение было найдено в known_face_encodings, просто используется первое.
        #     если True в совпадениях:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Или вместо этого используеися известное лицо с наименьшим отрывом(tolerance) до нового лица
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Вывод рамки
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Вывод текста
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Вывод обработанного изображения
    cv2.imshow('Video', frame)

    # Нажать 'q' на клавиатуре чтобы выйти!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()