import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('Experiment 4\haarcascade_stapler.xml')
img = cv2.imread('../../images/stapler.jpg')
cap=cv2.VideoCapture(0)
frameWidth = 640
frameHeight = 480
while True:
    ret,img=cap.read()
    img=cv2.resize(img, (frameWidth, frameHeight))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect stapler
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the stapler
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()