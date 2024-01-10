import face_recognition
import sys
import os

known_face_name = []
known_face_encoding = []
process_current_frame = True


def encodeimage():
    for image in os.listdir('FaceAttendence/studentimage'):
        face_image=face_recognition.load_image_file(f'studentimage/{image}')
        face_encoding=face_recognition.face_encodings(face_image)[0]
        known_face_encoding.append(face_encoding)
        known_face_name.append(image)


