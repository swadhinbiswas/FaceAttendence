#function for confirm attendence 
import time,datetime
def confirm_attendence(data):
    attendence=False
    if data>60:
        attendence=True
        time=datetime.datetime.now()
        print(time)
    

