import cv2
import numpy as np
import face_recognition as fr
import os
import sys
import math

# input your face xmlfile
stduent_face = cv2.CascadeClassifier("")
video_cap = cv2.VideoCapture(0)

while True:
    temp, video_data = video_cap.read()
