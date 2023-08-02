import numpy as np
import cv2


# initialize video from the webcam
video = cv2.VideoCapture(0)
# Read the video
cap, frame = video.read()

# set up initial coordinates for the tracking window
x, y = 0, 0
# Set up initial size of the tracking window
height, width = 25, 25
track_window = (x, y, width, height)
# set up region of interest (roi)
roi = frame[y:y + height, x:x + width]

# apply mask
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_frame, np.array((0, 20, 20)), np.array((180, 250, 250)))
hist_frame = cv2.calcHist([hsv_frame], [0], mask, [180], [0, 180])
cv2.normalize(hist_frame, hist_frame, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria: 10 iteration 1 pxl movement
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    
    cap, frame = video.read()
    if cap == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],hist_frame,[0,180],1)
        # apply camshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        # Draw a box around the ROI
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, 255, 2)
        cv2.imshow('img2', img2)
        # Use the q button to quit the operation
        if cv2.waitKey(60) & 0xff == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()
video.release()


