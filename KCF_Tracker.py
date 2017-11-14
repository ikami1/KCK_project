import numpy as np
import cv2

def KCF_Tracking():
    # to get second camera pass 1
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Not opened")
        return

    while True:
        ret, frame = cap.read()
        cv2.imshow('Press Q when ready to select ROI', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    ret, first_frame = cap.read()

    if not ret:
        print("Cannot read first frame")
        return

    col, row, width, height = cv2.selectROI("ROI to track", first_frame, False)
    track_window = (col, row, width, height)
    print(track_window)

    # Crop image
    img_crop = first_frame[row:row + height, col:col + width]
    # Display cropped image
    cv2.imshow("Image to track", img_crop)

    tracker = cv2.TrackerKCF_create()
    ok = tracker.init(frame, track_window)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Start timer
            timer = cv2.getTickCount()

            ok, bbox = tracker.update(frame)

            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

            # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);

            cv2.imshow('Live camera, press Q to quit', frame)

            # Quit if q is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Cannot read frame")
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()