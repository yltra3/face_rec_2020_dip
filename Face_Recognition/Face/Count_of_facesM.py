import face_recognition

image = face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coords of each face
# print(face_locations)

print(f'Здесь {len(face_locations)} человек на изображении')
