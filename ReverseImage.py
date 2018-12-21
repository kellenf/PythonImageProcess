import numpy as np
import cv2
def ReverseImage(image,axies=0):
    '''
    对彩色图像镜像翻转：
    :param image: 原图像
    :param axie: 为0表示水平镜像翻转，为1表示垂直镜像翻转
    :return: 返回处理完之后的图像
    '''
    shape=np.shape(image)
    c=3
    i,j=0,0
    if axies==0:
        i,j=0,shape[1]-1
        while i<j:
            image[:,[i,j]]=image[:,[j,i]]
            i+=1
            j-=1
    if axies==1:
        i, j = 0, shape[0] - 1
        while i < j:
            image[[i,j],:] = image[[j, i], :]
            i += 1
            j -= 1
    return image
if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    cv2.imshow('src',image)
    image_0=image.copy()
    ReverseImage(image_0,axies=0)
    cv2.imshow('axies=0',image)
    image_1=image.copy()
    ReverseImage(image_1,axies=1)
    cv2.imshow('axies=1',image_1)
    cv2.waitKey()
