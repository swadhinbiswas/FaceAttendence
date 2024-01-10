import math


def face_confidence(face_distance, facematch_threshold=0.6):
    distance = (1.0 - facematch_threshold)
    linear_val = (1.0-face_distance)/(distance*2.0)

    if face_distance > facematch_threshold:
        return str(round(linear_val*100, 2))+'%'
    else:
        value = (linear_val + ((1.0-linear_val) *
                 math.pow((linear_val-0.5)*0.2, 0.2)))
        return str(round(value, 2))+'%'