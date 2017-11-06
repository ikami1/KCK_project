import cv2


def showLiveCam():
    # to get second camera pass 1
    cap = cv2.VideoCapture(0)

    ret, first_frame = cap.read()

    rectangles = []
    from_center = False
    cv2.selectROI("Image", first_frame, rectangles, from_center)
    # r = cv2.selectROI("ROI to track", first_frame, False)

    while():
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Cannot read frame")
            break

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('Live camera, press Q to quit',gray)

        # Quit if q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()