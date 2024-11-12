""" Face Detection Using Python"""

# pip install ovencv-python
# pip install 


# Module from ovencv-python
import cv2
face_cap = cv2.CascadeClassifier("C:/Users/vaibh/OneDrive/Desktop/Python Streak/(P-6) face detection/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(video_data, (x,y), (x+w,y+h), (0,255,0),2)

    cv2.imshow("video_live", video_data)
    
    # when you press S the video capturing stops.
    if cv2.waitKey(10) == ord("s"):
        break
video_cap.release()
