import numpy as np
import cv2
def EquelizeHist(image):
    '''
    直方图均衡化：
    就实现对灰度图的，彩色图在BGR模式下貌似不能对每个通道分别计算，需要转到HSV或者其他颜色模型，但是主要思想还是一样的
    :param image:
    :return:
    '''
    rows,cols=image.shape[0],image.shape[1]
    result=np.zeros((rows,cols),np.uint8)
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            val=image[i,j]*5-image[i-1,j]-image[i+1,j]-image[i,j-1]-image[i,j+1]
            result[i,j]=val
    return result
if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('src',image)
    result=EquelizeHist(image)
    cv2.imshow('result',result)
    cv2.waitKey()

