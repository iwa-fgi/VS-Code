import cv2
Font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread("Resources/Shapes.jpg",0)
placeholder,threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
contours, placeholder = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
og=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (255,255,0), -1)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(og, "Triangle", (x, y), Font, 1, (255,0,0))
    elif len(approx) == 4 :
        x, y , w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        print(aspectRatio)
        if  1.5>= aspectRatio >= 0.95 :
            cv2.putText(og, "square", (x, y), Font, 1, (255, 0, 0))
        else:
            cv2.putText(og, "rectangle", (x, y), Font, 1, (255, 0, 0))
    elif len(approx) == 5:
        cv2.putText(og, "Pentagon", (x, y), Font, 1, (255,0,0))
    elif 6 < len(approx) < 15:
        cv2.putText(og, "Star", (x, y), Font, 1, (255,0,0))
    else:
        cv2.putText(og, "Circle", (x, y), Font, 1, (255,0,0))
cv2.imshow("shapes", og)
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()