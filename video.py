import cv2
import numpy as np


def liveCamTracking():
    # to get second camera pass 1
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Not opened")
        return

    cv2.waitKey(1000)
    ret, first_frame = cap.read()

    if not ret:
        print("Cannot read first frame")
        return

    col, row, width, height = cv2.selectROI("ROI to track", first_frame, False)
    track_window = (col, row, width, height)

    # Crop image
    img_crop = first_frame[row:row+height, col:col+width]
    # Display cropped image
    cv2.imshow("Image to track", img_crop)

    hsv_crop = cv2.cvtColor(img_crop, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_crop, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
    roi_hist = cv2.calcHist([hsv_crop], [0], mask, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Start timer
            timer = cv2.getTickCount()

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
            # apply CamShift to get the new location
            ret, track_window = cv2.CamShift(dst, track_window, term_crit)

            # Draw it on image
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            res_img = cv2.polylines(frame, [pts], True, 255, 2)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            # Display FPS on frame
            cv2.putText(res_img, "FPS : " + str(int(fps)), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            cv2.imshow('Live camera, press Q to quit', res_img)

            # Quit if q is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Cannot read frame")
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()