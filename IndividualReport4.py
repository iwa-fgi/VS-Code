import cv2
Capture = cv2.VideoCapture(0)
fWidth = int(Capture.get(cv2.CAP_PROP_FRAME_WIDTH))
fHeight = int(Capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (fWidth,fHeight)
Writer = cv2.VideoWriter('Resources/Capture.mp4', cv2.VideoWriter_fourcc(*'XVID'),10, size)
while True:
    success, img = Capture.read()
    if success:
        cv2.imshow('Video', img)
        Writer.write(img)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
    else:
        break
Capture.release()
cv2.destroyAllWindows()
