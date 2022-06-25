import face_recognition
from PIL import Image, ImageDraw, ImageFont
def main(path):
  image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
  bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

  image_of_steve = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')
  steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

  image_of_elon = face_recognition.load_image_file('./img/known/Elon Musk.jpg')
  elon_face_encoding = face_recognition.face_encodings(image_of_elon)[0]

  image_of_misha = face_recognition.load_image_file('./img/known/Vlad.jpg')
  misha_face_encoding = face_recognition.face_encodings(image_of_misha)[0]


  #  Создание массивов распознаваний и имён
  known_face_encodings = [
    misha_face_encoding,
    bill_face_encoding,
    steve_face_encoding,
    elon_face_encoding
  ]

  known_face_names = [
    "Vlad ",
    "Bill Gates",
    "Steve Jobs",
    "Elon Musk"
  ]

  # Загрузка эталона
  test_image = face_recognition.load_image_file(path)

  # Нахождение эталонности
  face_locations = face_recognition.face_locations(test_image)
  face_encodings = face_recognition.face_encodings(test_image, face_locations)

  # Конвертирование в формат PIL
  pil_image = Image.fromarray(test_image)

  # Создание инстанции ImageDraw
  draw = ImageDraw.Draw(pil_image)

  # Перебор лиц в эталонах
  for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown Person"

    # если есть совпадения
    if True in matches:
      first_match_index = matches.index(True)
      name = known_face_names[first_match_index]

    # Рисование рамки
    draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

    # Вывод текста
    fnt=ImageFont.truetype("arial.ttf", size=30)
    text_width, text_height = draw.textsize(name)

    draw.rectangle(((left,bottom - text_height -50), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
    draw.text((left + 6, bottom - text_height - 25), name, font=fnt, fill=(0,0,0))

  del draw

  # Вывод изображения
  pil_image.show()

  # Сохранение изображения
  pil_image.save('identify.jpg')