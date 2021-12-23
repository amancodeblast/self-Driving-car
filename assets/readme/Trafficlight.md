# Traffic Light Classifier Project (Final project for the Introduction to Self-Driving-Cars Engineer Nanodegree)

This is a traffic light classifier project using Python and basic OpenCV2 techniques to recognize traffic lights. And it is also part of the final project of the Udacity's Introduction to Self-Driving Car Engineer Nanodegree.

In this project, knowledge of computer vision techniques is used to build a classifier for images of traffic lights.

<img src="https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/Traffic_light.gif?raw=true" width="500">

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/images/all_lights.png "Traffic Lights")

In the notebook, it pre-processes these images and extracts features that will help us distinguish the different types of images, and use those features to classify the traffic light images into three classes: red, yellow, or green.

# About the data

This traffic light dataset consists of 1484 number of color images in 3 categories - red, yellow, and green. As with most human-sourced data, the data is not evenly distributed among the types. There are:
* 904 red traffic light images
* 536 green traffic light images
* 44 yellow traffic light images

*Note: All images come from this [MIT self-driving car course](https://selfdrivingcars.mit.edu/) and are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).*

# Accuracy of traffic light classification

With the traffic light classifier pipeline below, I was able to obtain approx 90% accuracy of traffic light classification

# The traffic light classifier pipeline
1. __Loading and visualizing the data__: The first step is to import Python libraries used in this project such as numpy, matplotlib, cv2 and the custom "helpers" function. And then we'll use load and visualize the image using matplotlib to ensure the image is loaded correctly.

2. __Pre-processing__: The input images and output labels need to be standardized. This way, you can analyze all the input images using the same classification pipeline, and you know what output to expect when you eventually classify a new image. Resizing and cropping are be used to standardize each image to 32x32px. Given the sample of the datasets, shift and rotations are not required. Then later the image label can be binarized using the custom __one-hot_encode()__ function to classification processing.

3. __Feature extraction__: Extraction of some features from each image will help to distinguish and classify the traffic lights. Main feature extraction techniques used in this project are: __RGB to HSV conversion__, average __brightness feature()__ for the 3 equal verticlaly spaced segments.

4. __Classification and visualizing error__: At last, a traffic light classifer function is created to use the extracted image features to classify any traffic light images. This __estimate_label__ function takes in an image and outputs a predicted label for the traffic light based on the average brightness of the equally divided horizontal segments.
Then, __get_misclassified_images()__ is used to generate the list of the misclassified images. From this list, we can then determine the accuracy of your classification model by comparing both the __predicted label__ (from the classifier) and __ground truth label__ (from the dataset).

   To understand the traffic light misclassification better, a loop is created to step through each image, display the misclassified image along with both incorrectly predicted and ground-truth labels, as well as attributes such as avearge RGB, brightness, hue values in the 3 equal vertically spaced segments.

5. __Evaluate your model__: This project has acheived 90% accuracy in traffic light classification and has never classified red lights as green and verified with the __test_functions.Tests()__ in the helpers.py



# Successful Results 

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/images/Traffic_light_detection.png "Traffic Lights Detection Output")

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/images/Traffic_light_simulator.png)

![Video Link](https://youtu.be/MspewuQH75U)