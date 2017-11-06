import cv2


#Ronice aktualnej klatki z dwoma poprzednimi
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


#Ronice dwoch klatek
def dif2(t0, t1):
    d = cv2.absdiff(t1, t0)
    return d


def motion_detection():
    cam = cv2.VideoCapture(0)

    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    while(True):
        # Capture frame-by-frame
        ret, frame = cam.read()

        # Display the resulting frame
        cv2.imshow('video', frame)
        cv2.imshow('frame', dif2(t_plus, t))
        cv2.imshow('frame2', diffImg(t_minus, t, t_plus))

        # Read next image
        t_minus = t
        t = t_plus
        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

        # Koniec programu na "q"
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()