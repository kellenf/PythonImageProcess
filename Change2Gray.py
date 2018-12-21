import cv2
import numpy as np
def Change2Gray(image):
    l=len(np.shape(image))
    assert  l==3,'不是彩色图'
    '''
    BGR模式彩色图变成黑白的：
    RGB 按照 0.299 R， 0.587 G 和 0.114 B，需要注意的是opencv中元素是按照BGR排列的
    '''
    rows,cols,_=image.shape
    result=np.zeros((rows,cols),dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            result[i,j]=image[i,j,0]*0.114+image[i,j,1]*0.587+image[i,j,2]*0.299
    return  result

if __name__ == '__main__':
    image=cv2.imread('test.jpeg')
    cv2.imshow('src',image)
    result=Change2Gray(image)
    result=result.astype(np.uint8)
    cv2.imshow('result',result)
    cv2.waitKey()