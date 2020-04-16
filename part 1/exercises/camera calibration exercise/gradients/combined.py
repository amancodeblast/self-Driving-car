# Modifyed this for the sake of combining the complete filters 
def abs_sobel_thresh(img, orient='x', sobel_kernel=3, thresh=(0, 255)):
    # Calculate directional gradient
    # Apply threshold
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    if orient=='x':
        SobelXY=cv2.Sobel(gray,cv2.CV_64F, 1,0)
    if orient =='y':
        SobelXY=cv2.Sobel(gray,cv2.CV_64F, 0,1)
    abs_v=np.absolute(SobelXY)
    scaled=np.uint8(255*abs_v/(np.max(abs_v)))
    binary_output=np.zeros_like(scaled)
    binary_output[(thresh[0]>= scaled) | (thresh[1]<= scaled)]=1
    return binary_output

def mag_thresh(image, sobel_kernel=3, mag_thresh=(0, 255)):
    # Calculate gradient magnitude
    # Apply threshold
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    SobelX = cv2.Sobel(gray, cv2.CV_64F, 1, 0,ksize=sobel_kernel)
    SobelY = cv2.Sobel(gray, cv2.CV_64F, 0, 1,ksize=sobel_kernel)
    abs_V = np.sqrt(SobelX**2+SobelY**2)
    scaled = np.uint8(255*abs_V/np.max(abs_V))
    mag_binary = np.zeros_like(scaled)
    mag_binary[(mag_thresh[0]>= scaled) | (mag_thresh[1]<= scaled)]=1    
    return mag_binary

def dir_threshold(image, sobel_kernel=3, thresh=(0, np.pi/2)):
    # Calculate gradient direction
    # Apply threshold
#     binary_output = np.copy(img) # Remove this line
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Calculate the x and y gradients
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    absgraddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))#point to notice
    binary_output =  np.zeros_like(absgraddir)
    binary_output[(absgraddir >= thresh[0]) & (absgraddir <= thresh[1])] = 1
    return binary_output

# Choose a Sobel kernel size
ksize = 15 # Choose a larger odd number to smooth gradient measurements

# Read in an image
image = mpimg.imread('signs_vehicles_xygrad.png')

# Apply each of the thresholding functions
gradx = abs_sobel_thresh(image, orient='x', sobel_kernel=ksize, thresh=(20, 100))
grady = abs_sobel_thresh(image, orient='y', sobel_kernel=ksize, thresh=(20, 100))
mag_binary = mag_thresh(image, sobel_kernel=ksize, mag_thresh=(30, 100))
dir_binary = dir_threshold(image, sobel_kernel=ksize, thresh=(0.7, 1.3))
#combining all of the above
combined = np.zeros_like(dir_binary) 
combined[((gradx == 1) & (grady == 1)) | ((mag_binary == 1) & (dir_binary == 0))] = 1

f, (ax) = plt.subplots(6, 1, figsize=(35, 25))

f.tight_layout()
ax[0].imshow(image)
ax[0].set_title('Original Image', fontsize=30)
ax[1].imshow(gradx,cmap='gray')
ax[1].set_title('Gradient X Image', fontsize=30)
ax[2].imshow(grady,cmap='gray')
ax[2].set_title('Gradient y Image', fontsize=30)
ax[3].imshow(mag_binary,cmap='gray')
ax[3].set_title('Magnitude binary Image', fontsize=30)
ax[4].imshow(dir_binary, cmap='gray')
ax[4].set_title('Thresholded Grad. Dir.', fontsize=30)
ax[5].imshow(combined,cmap='gray')
ax[5].set_title('combined gradients',fontsize=30)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

# For example, here is a selection for pixels where both the xx and yy gradients meet the threshold criteria, or the gradient magnitude and direction are both within their threshold values.

plt.show()
