import numpy as np
import cv2 as cv

def M2GLD_Apply(img_M2GLD,R,tau):    
    gray=cv.cvtColor(img_M2GLD,cv.COLOR_BGR2GRAY)
    row,col=img_M2GLD.shape[:2]
    M2GLD_img=np.zeros((row,col),dtype='uint8')
    min_I=300
    max_I=-1

    for i in range(0,row):        
        for j in range(0,col):
            if gray[i,j]<min_I:
                min_I=gray[i,j]
            if gray[i,j]>max_I:
                max_I=gray[i,j]
    range_I=max_I-min_I
    print("Minimum Intensity:{} Maximum Intensity:{} tau:{} R factor:{}".format(min_I,max_I,tau,R))
    fn=(min_I+(tau*(range_I)))
    for i in range(0,row):        
        for j in range(0,col):            
                if gray[i,j]>fn:
                    M2GLD_img[i,j]=np.minimum(min_I,gray[i,j]*R)
                else:
                    M2GLD_img[i,j]=np.maximum(min_I,gray[i,j]*(1/R))
    return M2GLD_img