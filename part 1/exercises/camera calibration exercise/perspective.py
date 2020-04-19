import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def warp(img):
    new_image_size=(img.shape[0],img.shape[1])#here i chose to set the new image size equal to the previous image
    
    #defining calibration box in the source(original) and destination (desire or warped image) cordinates
    src=np.float32([[850,320],[865,450],[533,350],[535,210]])
    dst=np.float32([[870,240],[870,370],[520,370],[520,240]])
    
    #compute perspective transform, M
    M=cv2.getPerspectiveTransform(src,dst)
    
    #could get the inverse by swapping the input parameters
    M_inv=cv2.getPerspectiveTransform(dst,src)
    
    # create warped image - use linear interpolation
    warped=cv2.warpPerspective(img,M, new_image_size,flags=cv2.INTER_LINEAR)
    
    return warped


img=cv2.imread('for_warping.png')

warp_image=warp(img)

fig, (axis1,axis2)=plt.subplots(1,2,figsize=(25,30))

axis1.set_title('Source Image')
axis2.set_title('Warped Image')
axis1.imshow(img)
axis2.imshow(warp_image)
plt.show()
