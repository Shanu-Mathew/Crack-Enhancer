import cv2 as cv
import os

from src.utils import resized_frame
from src.otsu import otsu_thresholding
from src.M2GLD import M2GLD_Apply
def M2GLD_Otsu(user_input_image):
    M2GLD_img=M2GLD_Apply(user_input_image,1.1,0.7)
    otsu_img=otsu_thresholding(M2GLD_img)
    return otsu_img


if __name__=="__main__":
    data_test=".\\Test Images\\TestImage.jpg"
    img_M2GLD=cv.imread(os.path.join(data_test),cv.IMREAD_COLOR)
    img_M2GLD=resized_frame(img_M2GLD)
    Enhanced_img=M2GLD_Otsu(img_M2GLD)
    cv.imshow('Enhanced Surface Crack Image',Enhanced_img)
    cv.imshow('Raw Image',img_M2GLD)
    cv.waitKey(0)