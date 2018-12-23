import numpy as np
import cv2
def Erode(image):
    '''
    图像腐蚀函数
    :param image:二值化图像
    :return:
    '''
    rows,cols=image.shape[0],image.shape[1]
    result=np.zeros((rows,cols),np.uint8)
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if image[i,j]==255 and image[i+1,j]==255 and image[i-1,j]==255 and image[i,j+1]==255 and image[i,j-1]==255:
                result[i,j]=255
    return  result


if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,image=cv2.threshold(image,20,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('src',image)
    # cv2.waitKey()
    result=Erode(image)
    cv2.imshow('result',result)
    cv2.waitKey()

