import cv2

cap = cv2.VideoCapture(0)

framew = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (framew, frameh)
storedVideo = cv2.VideoWriter('Capture.mp4', cv2.VideoWriter_fourcc(*'XVID'),10, size)
while True:
    success, img = cap.read()
    if success:
        cv2.imshow('Video', img)
        storedVideo.write(img)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()