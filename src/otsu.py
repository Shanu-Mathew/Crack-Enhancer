import cv2 as cv
import numpy as np

from src.utils import Hist

def calc_hist(img_enhanced):
    gray_hist=cv.calcHist([img_enhanced],[0],None,[256],[0,256])
    gray_hist=gray_hist.flatten()
    Hist(img_enhanced)
    return gray_hist

def normalize_histogram(histogram):
    total_pixels = np.sum(histogram)  # Calculate the total number of pixels
    normalized_histogram = histogram.astype(float) / total_pixels  # Normalize the histogram
    return normalized_histogram

def cum_sum_histogram(norm_gray_hist):
    cum_sum=np.cumsum(norm_gray_hist)
    return cum_sum

def compute_minimum_thresh(cum_sum, norm_hist):
    bins = np.arange(256)
    min_fn_values=np.zeros_like(norm_hist)
    
    fn_min=np.inf
    for i in range(len(norm_hist)):
        p1,p2 = np.hsplit(norm_hist,[i]) # probabilities
        q1,q2 = cum_sum[i],cum_sum[255]-cum_sum[i] # cum sum of classes
        
        if q1 < 1.e-6 or q2 < 1.e-6:
            continue
            
        b1,b2 = np.hsplit(bins,[i]) # weights
        
        # finding means and variances
        m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
        
        # calculates the minimization function
        min_fn_value = v1*q1 + v2*q2
        min_fn_values[i]=  min_fn_value
        
        
        #finding the minimum value
        if min_fn_value<fn_min:
            fn_min=min_fn_value
            optimal_threshold=i
    
    return optimal_threshold

def otsu_threshold_image(img_enhanced,optimal_threshold):
    _,thresh=cv.threshold(img_enhanced,optimal_threshold,255,cv.THRESH_BINARY_INV)
    return thresh

def otsu_thresholding(gray_img):
    blur_img=cv.GaussianBlur(gray_img,(5,5),0)
    hist_otsu=calc_hist(blur_img)
    norm_hist_otsu=normalize_histogram(hist_otsu)
    cum_sum_otsu=cum_sum_histogram(norm_hist_otsu)
    optimal_thresh_otsu=compute_minimum_thresh(cum_sum_otsu, norm_hist_otsu)
    print('Optimal Threshold',optimal_thresh_otsu)
    thresh_img=otsu_threshold_image(blur_img,optimal_thresh_otsu)
    return thresh_img