import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def resized_frame(image):
    width=256
    height=256
    dimensions=(width,height)
    return cv.resize(image,dimensions,interpolation=cv.INTER_AREA)


def Hist(img):
    row,col= img.shape[:2] 
    y = np.zeros(256,dtype='uint8')
    for i in range(0,row): 
        for j in range(0,col):
            y[img[i,j]] += 1
            
    x = np.arange(0,256)
    plt.figure(figsize=(15,8))
    plt.bar(x, y, color='b', width=5, align='center', alpha=0.25)
    plt.xticks(np.arange(0,256,step=10))
    plt.show()
    return y