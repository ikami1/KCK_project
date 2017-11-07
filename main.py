from video import liveCamTracking
from motion_detection_grey import motion_detection


if __name__ == '__main__':
    print("Elo w projekcie, przykład zastosowania BackProjection ~ikami")

    liveCamTracking()
    # motion_detection()

    '''img_part = cv2.imread('trolltunga_river.jpg')
    hsv_part = cv2.cvtColor(img_part, cv2.COLOR_BGR2HSV)

    img_target = cv2.imread('trolltunga.jpg')
    hsv_target = cv2.cvtColor(img_target, cv2.COLOR_BGR2HSV)

    # calculating object histogram
    hist_part = cv2.calcHist([hsv_part], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # normalize histogram and apply backprojection
    cv2.normalize(hist_part, hist_part, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsv_target], [0, 1], hist_part, [0, 180, 0, 256], 1)

    # Now convolute with circular disc
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cv2.filter2D(dst, -1, disc, dst)


    # threshold and binary AND
    ret, thresh = cv2.threshold(dst, 50, 255, 0)
    thresh = cv2.merge((thresh, thresh, thresh))
    res = cv2.bitwise_and(img_target, thresh)

    res = np.vstack((img_target, thresh, res))
    cv2.imwrite('res.jpg', res)'''