
import cv2
import imagematch as im
from faceconfidence import *
import numpy as np
import face_recognition as fr
face_location = []
face_encoding = []
face_names = []

# input your face xmlfile
video_cap = cv2.VideoCapture(0)

while True:
    temp, video_data = video_cap.read()

    if im.process_current_frame:
        small_frame=cv2.resize(video_data,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame=small_frame[:,:,::-1]

        face_location=fr.face_locations(rgb_small_frame)
        face_encoding=fr.face_encodings(rgb_small_frame,face_location)
        for face_encode in face_encoding:
            mathches=fr.compare_faces(im.known_face_encoding,face_encoding)
            name='Unkown'
            confidence='unknown'
            face_distances=fr.face_distance(im.known_face_encoding,face_encoding)
            best_match_index=np.argmin(face_distances)

            if mathches[best_match_index]:
                name=im.known_face_name
                confidence=face_confidence(face_distances[best_match_index])
                tempvar=confidence
                face_names.append(f'{name}({confidence})')
                       
            im.process_current_frame=not im.process_current_frame

            for (top,right,bottom,left), name in zip(face_location,face_names):
                top*=4
                right*=4
                bottom*=4
                left*=4

                cv2.rectangle(video_data,(left,top),(right,bottom),(0,0,225),2)
                cv2.rectangle(video_data,(left,bottom-35),(right,bottom),(0,0,225),-1)
                cv2.putText(video_data,name,(left+6,bottom-6),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),1)

            cv2.imshow('Student Face',video_data)
        
        video_cap.release()



        


            
   



            


