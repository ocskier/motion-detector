import cv2, os
from time import sleep

video = cv2.VideoCapture(1)
sleep(1)
numFrames = 0
compare = None

while(True):
    check, frame = video.read()
    grey_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if (numFrames == 0):
        compare = grey_image
        cv2.imwrite(os.path.join("./output","compare.jpg"),grey_image)
    numFrames += 1
    # print(numFrames)
    frame_diff = cv2.absdiff(compare, grey_image)
    ret, thres_image = cv2.threshold(frame_diff,127,255,cv2.THRESH_BINARY)
    cv2.imshow("front_cam",grey_image)
    cv2.imshow('frame diff',frame_diff)
    cv2.imshow("thres_diff",thres_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(numFrames)
video.release()
cv2.destroyAllWindows()