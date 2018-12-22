import numpy as np
import cv2


def Sobel(image, thresh=100):
    print(np.shape(image))
    rows, cols = np.shape(image)
    result = np.zeros((rows, cols), dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            det_x = 2 * np.abs(image[i + 1, j] - image[i - 1, j]) + np.abs(
                image[i - 1][j - 1] - image[i - 1][j + 1]) + np.abs(image[i + 1, j - 1] - image[i + 1, j + 1])
            det_y = 2 * np.abs(image[i + 1, j] - image[i - 1, j]) + np.abs(
                image[i - 1][j - 1] - image[i + 1][j - 1]) + np.abs(image[i + 1, j + 1] - image[i - 1, j + 1])
            det = np.sqrt(det_x * det_x + det_y * det_y)
            if det > thresh:
                result[i, j] = 255
    return result


if __name__ == '__main__':
    image = cv2.imread('test.jpeg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY)
    # print(np.shape(image))
    result=Sobel(image,600)
    cv2.imshow('result', result)
    cv2.waitKey()
