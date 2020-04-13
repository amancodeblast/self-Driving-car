#calibrating the camera

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg  
%matplotlib qt
import glob

images=glob.glob('../calibration_images/calibration*.jpg')

objpoints=[]
imgpoints=[]

#prepare object points like (0,0,0), (1,0,0)
objp=np.zeros((6*8,3), np.float32)
objp[:,:2]=np.mgrid[0:8,0:6].T.reshape(-1,2)#x, y coordinates
for fname in images:
    cv2.imread("../calibration_images"+fname)
    #converting images to grayscale images
    # for imread BGR is used 
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#RBG if mpimg.imread is used RGB is there

    #find the chessboard corners
    res,corners=cv2.findChessboardCorners(gray,(8,6),None)

    #if corners found then adding the object and the image point
    if ret=True:
        imgpoints.append(corners)
        objpoints.append(objp)
        
        #drawing the corners for the chess board
        img=cv2.drawChessboardCorners(img,(8,6),corners,res)
        plt.imshow(img)


#now we will Calibrate the camera using the data we have collected so far 
# this will also include the transformation of the original image to the 

ret, mtx, dist, rvecs, tvecs= cv2.calibrateCamera(objpoints,imgpoints,gray.shape[::-1],None, None)#img.shape[1::-1] instead of gray.shape
#above is camera calibration given the objpoints, imagepoints and the shape of the grayscale image
#dist= distortion coef. , mtx =camera matrix that is needed to xform 3d object points to 2D points
# also the position of the camera in the world with values revecs= rotational vectors and tvecs =translation vectors
#Undestorting a test image
dst = cv2.undistort(img, mtx, dist, None, mtx)
#input distorted image camera matrix distortion coef. 
#output is the 
