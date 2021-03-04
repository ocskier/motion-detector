import cv2, os

video = cv2.VideoCapture(0)

numFrames = 0
compare = None

while(True):
    check, frame = video.read()
    grey_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if (numFrames == 0):
        compare = grey_image
        cv2.imwrite(os.path.join("./output","compare.jpg"),grey_image)

    cv2.imshow("front_cam",grey_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()