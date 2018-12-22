import numpy as np
import cv2
def Ostu(image):
    '''
    最大类间方差：
    E=left_n/size*np.square(left_p-average)+right_n/size*np.square(right_p-average),求这个的最大值
    left_n：小于所选阈值的像素点的个数
    right_n:大于所选阈值的像素点的个数
    size:图像总像素点的个数
    left_p:小于该阈值的像素点的均值
    right_p:大于该阈值的像素点的均值
    average：图像整体的像素均值
    需要注意的是当图像太大的时候不要超出整数表示范围，所以需要一些细节上的技巧
    :param image: 
    :return: 
    '''
    shape=np.shape(image)
    size=np.size(image)
    rows,cols=shape[0],shape[1]
    #灰度直方图
    hist=[0 for x in range(256)]
    #均值
    average=0
    for i in range(rows):
        for j in range(cols):
            val=image[i,j]
            average+=image[i,j]/size
            hist[val]+=1
    m=-np.inf
    thresh=0
    for i in range(256):
        left_n=np.sum(hist[0:i+1])
        right_n=np.sum(hist[i+1:256])
        left_p=0
        for x in range(i):
            left_p+=hist[x]*x/left_n
        right_p=0
        for x in range(i+1,256):
            right_p+=hist[x]*x/right_n
        value=left_n/size*np.square(left_p-average)+right_n/size*np.square(right_p-average)
        if  value>m:
            m=value
            thresh=i
    for i in range(rows):
        for j in range(cols):
            if image[i,j]>thresh:
                image[i,j]=255
            else:
                image[i,j]=0

if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('src',image)
    Ostu(image)
    cv2.imshow('result',image)
    cv2.waitKey()
