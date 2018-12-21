import cv2
import numpy as np
'''
灰度图方框滤波器
'''

#均值滤波快速算法
def BoxFilter(image,size):
    assert size%2==1,"size value is not right"
    size=int(size/2)
    rows,cols=image.shape
    result=np.zeros((rows,cols),dtype=np.float32)
    graph=np.zeros((rows,cols),dtype=np.float32)
    #计算积分图
    for i in range(rows):
        for j in range(cols):
            c1=0
            if i-1>=0 and j-1>=0:
                c1=graph[i-1,j-1]
            c2=np.sum(image[i,0:j+1])
            c3=np.sum(image[0:i+1,j])
            graph[i,j]=c1+c2+c3-image[i,j]
    for i in range(rows):
        for j in range(cols):
            x0=max(i-size,0)
            y0=max(j-size,0)
            x1=min(rows-1,i+size)
            y1=min(cols-1,j+size)
            cnt=(y1-y0+1)*(x1-x0+1)
            result[i,j]=(graph[x1,y1]+graph[x0,y0]-graph[x0,y1]-graph[x1,y0])/cnt
    return result

if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    data=np.asarray(image)
    data_f=data/255
    result=BoxFilter(data_f,5)
    cv2.imshow('after filter',result)
    cv2.waitKey()
