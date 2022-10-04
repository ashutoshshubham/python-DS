import cv2
filepath = r"E:\TUTORIALS\The Complete Data Structures and Algorithms Course in Python\25. Binary Heap\1. What is Binary Heap Why do we need it.mp4"

video = cv2.VideoCapture(filepath)

while True:
    check,frame = video.read()
    if not check:
        break
    cv2.imshow("webcam 0",frame)         #displays a window with the webcam
    if cv2.waitKey(1) == ord('q'):       #if the key is q, the loop breaks
        break
video.release()                          #release the webcam
cv2.destroyAllWindows()                  #closes all windows