# Extended Kalman Filter For Ego vehicle Localization

<img src="https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/kalman.gif?raw=true" width="500">

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/ekf_intro.png)

## What is a Kalman Filter and Why do we need it?

Please read the [Blog](https://www.geeksforgeeks.org/overview-of-kalman-filter-for-self-driving-car/) on Kalman Filter where I went in detail to explain the Kalman Filter. Please do not get overwhelmed by this amazing algorithm, it looks complicated but it runs on some basic Mathematics and gives you unlimited power. 

In a perfect world, everything works exactly as expected. And when you build a robot and tell it to go forward one meter, it does exactly that. And then when you pull out your Righteous Measuring Tape of Exactitude you find that, indeed by the grace of the lord almighty, it moved forward exactly one meter. Praise be! He is risen!

Well I’ve got news for you, sister - it don’t work like that. I don’t care how careful you were when you built it, that robot didn’t move *exactly* one meter. And while I’m bursting bubbles, I may as well let you know that your measurement was off. Maybe not by much (if you bought the expensive measuring tape), but I *guarantee* it was off.

Well, crap! That just made my easy problem (determining that robot’s location) a lot harder. But hold on a sec! Enter: Gaussians. Magical, magical Gaussians.

Beautiful, is it not? Here’s the equation for that little bump:

![Gaussian equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/ffe7c5cbdecda556bf2170e31f1f9a127b74e239)

The Gaussian is completely defined by its mean (or “expected value” - the actual measured value, represented by the symbol mu in the equation, which looks like the letter u) and variance (the uncertainty of the measurement, represented by sigma, which looks like an o) - the larger the variance, the wider the bump. The true magical beauty of Gaussians happens when you combine them. The product of two Gaussians? A Gaussian. The convolution of two Gaussians? Again, a Gaussian. The Fourier Transform of a Gaussian? You guessed it - a Gaussian. [See for yourself](http://www.tina-vision.net/docs/memos/2003-003.pdf).

That means that we don’t have to worry so much about the e’s and square roots and pi’s, and can focus just on the u’s and o’s, making the calculations far simpler. When you get into trying to work with complex movements and measurements in multidimensional space, this trick is a lifesaver. I can’t imagine that the actual probability distributions for any robot’s motion or any sensor’s measurement follow a Gaussian distribution, necessarily, but they’re just so dang easy to work with that it’s worth it to assume they do.

So that’s basically what we’re doing with the Kalman Filter - taking just the mean and variance for each dimension of our robot’s motion that we’re interested in tracking and putting them into a “state” vector and “covariance” matrix, respectively. From there, the math is *relatively* simple. It’s just a cycle of *predict* (“based on your previous motion, I’d expect you to be *here* n seconds later”) and *measurement update* (“but my sensor thinks you’re *here*”), from which a compromise is made and a new state vector and covariance matrix are determined. This is all contained in a [short list of equations](https://en.wikipedia.org/wiki/Kalman_filter#Predict), which I am not going to get into right now (this post is already long enough). The [Extended Kalman Filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter) simply adapts these equations slightly to account for nonlinear relationships between current/previous states and states/measurements.

Phew! How about an example?

These are the two sets of sensor measurements (in yellow), and associated ground truth (in blue) given for the project, along with my Kalman Filter estimate (in green):

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/ekf-output-1.png)

![](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/ekf-output-2.png)



---

## Dependencies

* cmake >= 3.5
  
  * All OSes: [click here for installation instructions](https://cmake.org/install/)
* make >= 4.1
  * Linux: make is installed by default on most Linux distros
  * Mac: [install Xcode command line tools to get make](https://developer.apple.com/xcode/features/)
  * Windows: [Click here for installation instructions](http://gnuwin32.sourceforge.net/packages/make.htm)
* gcc/g++ >= 5.4
  * Linux: gcc / g++ is installed by default on most Linux distros
  * Mac: same deal as make - [install Xcode command line tools]((https://developer.apple.com/xcode/features/)
  * Windows: recommend using [MinGW](http://www.mingw.org/)
* [uWebSockets](https://github.com/uWebSockets/uWebSockets)
  * Run either `./install-mac.sh` or `./install-ubuntu.sh`.
  * If you install from source, checkout to commit `e94b6e1`, i.e.
    ```
    git clone https://github.com/uWebSockets/uWebSockets 
    cd uWebSockets
    git checkout e94b6e1
    ```
    Some function signatures have changed in v0.14.x. See [this PR](https://github.com/udacity/CarND-MPC-Project/pull/3) for more details.
* Simulator. You can download these from the [project intro page](https://github.com/udacity/self-driving-car-sim/releases) in the classroom.

## Basic Build Instructions

1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make`
4. Run it: `./pid`. 

## Editor Settings

We've purposefully kept editor configuration files out of this repo in order to
keep it as simple and environment agnostic as possible. However, we recommend
using the following settings:

* indent using spaces
* set tab width to 2 spaces (keeps the matrices in source code aligned)

## Code Style

Please (do your best to) stick to [Google's C++ style guide](https://google.github.io/styleguide/cppguide.html).

## Project Instructions and Rubric

Note: regardless of the changes you make, your project must be buildable using
cmake and make!

More information is only accessible by people who are already enrolled in Term 2
of CarND. If you are enrolled, see [the project page](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/f1820894-8322-4bb3-81aa-b26b3c6dcbaf/lessons/e8235395-22dd-4b87-88e0-d108c5e5bbf4/concepts/6a4d8d42-6a04-4aa6-b284-1697c0fd6562)
for instructions and the project rubric.# CarND-Extended-Kalman-Filter-P1
Udacity Self-Driving Car Nanodegree - Extended Kalman Filter Implementation

# Overview
This project consists of implementing an [Extended Kalman Filter](https://en.wikipedia.org/wiki/Extended_Kalman_filter) with C++. A simulator provided by Udacity ([it could be downloaded here](https://github.com/udacity/self-driving-car-sim/releases)) generates noisy RADAR and LIDAR measurements of the position and velocity of an object, and the Extended Kalman Filter[EKF] must fusion those measurements to predict the position of the object. The communication between the simulator and the EKF is done using [WebSocket](https://en.wikipedia.org/wiki/WebSocket) using the [uWebSockets](https://github.com/uNetworking/uWebSockets) implementation on the EKF side.
To get this project started, Udacity provides a seed project that could be found (here)(https://github.com/udacity/CarND-Extended-Kalman-Filter-Project).

# Prerequisites

The project has the following dependencies (from Udacity's seed project):

- cmake >= 3.5
- make >= 4.1
- gcc/g++ >= 5.4
- Udacity's simulator.

For instructions on how to install these components on different operating systems, please, visit [Udacity's seed project](https://github.com/udacity/CarND-Extended-Kalman-Filter-Project). As this particular implementation was done on Mac OS, the rest of this documentation will be focused on Mac OS. I am sorry to be that restrictive.

In order to install the necessary libraries, use the [install-mac.sh](./install-mac.sh).

# Compiling and executing the project

These are the suggested steps:

- Clone the repo and cd to it on a Terminal.
- Create the build directory: `mkdir build`
- `cd build`
- `cmake ..`
- `make`: This will create two executables
  - `ExtendedKF` : EKF implementation.
  - `Test` : Simple unit tests using [Catch](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md).

## Running the tests

From the build directory, execute `./Tests`. The output should be something similar to this:

```
ERROR - CalculateRMSE () - The estimations vector is empty
ERROR - CalculateRMSE () - The ground-truth vector is empty
ERROR - CalculateRMSE () - The ground-truth and estimations vectors must have the same size.
ERROR - CalculateJacobian () - The state vector must have size 4.
ERROR - CalculateJacobian () - Division by Zero
===============================================================================
All tests passed (13 assertions in 2 test cases)
```

These unit tests were an experiment with [Catch](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md). It looks like a good and simple unit testing framework for C++.

## Running the Filter

From the build directory, execute `./ExtendedKF`. The output should be:

```
Listening to port 4567
Connected!!!
```

As you can see, the simulator connect to it right away.

The following is an image of the simulator:

![Simulator without data](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/simulator_without_running.png)

The simulator provides two datasets. The difference between them are:

- The direction the car (the object) is moving.
- The order the first measurement is sent to the EKF. On dataset 1, the LIDAR measurement is sent first. On the dataset 2, the RADAR measurement is sent first.

Here is the simulator final state after running the EKL with dataset 1:

![Simulator with dataset 1](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/simulator_dataset1.png)

Here is the simulator final state after running the EKL with dataset 2:

![Simulator with dataset 1](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/simulator_dataset2.png)

# [Rubric](https://review.udacity.com/#!/rubrics/748/view) points

## Compiling

### Your code should compile

The code compiles without errors. I did change the [CMackeLists.txt](https://github.com/amancodeblast/self-Driving-car/blob/master/assets/images/CMakeLists.txt) to add the creation of the `./Tests`. I don't think this will create incompatibilities with other platforms, but I only test it on Mac OS.

## Accuracy

### px, py, vx, vy output coordinates must have an RMSE <= [.11, .11, 0.52, 0.52] when using the file: "obj_pose-laser-radar-synthetic-input.txt which is the same data file the simulator uses for Dataset 1"

The EKF accuracy was:

- Dataset 1 : RMSE <= [0.0973, 0.0855, 0.4513, 0.4399]
- Dataset 2 : RMSE <= [0.0726, 0.0965, 0.4216, 0.4932]

## Following the Correct Algorithm

### Your Sensor Fusion algorithm follows the general processing flow as taught in the preceding lessons.

The Kalman filter implementation can be found [src/kalman_filter.cpp](https://github.com/amancodeblast/self-Driving-car/blob/master/localization/Markov%20localization/final%20filter/mian.cpp) and it is used to predict at [src/FusionEKF.cpp](https://github.com/amancodeblast/self-Driving-car/blob/master/localization/Markov%20localization/final%20filter/mian.cpp) line 147 and to update line 159 to 169.

### Your Kalman Filter algorithm handles the first measurements appropriately.

The first measurement is handled at [src/FusionEKF.cpp](./src/kalman_filter.cpp#L61) from line 61 to line 107.

### Your Kalman Filter algorithm first predicts then updates.

The predict operation could be found at [src/FusionEKF.cpp](https://github.com/amancodeblast/self-Driving-car/blob/master/localization/Markov%20localization/final%20filter/mian.cpp) line 147 and the update operation from line 159 to 169 of the same file.

### Your Kalman Filter can handle radar and lidar measurements.

Different type of measurements are handled in two places in [src/FusionEKF.cpp](https://github.com/amancodeblast/self-Driving-car/blob/master/localization/Markov%20localization/final%20filter/mian.cpp):

- For the first measurement from line 61 to line 107.
- For the update part from line 159 to 169.

## Code Efficiency

### Your algorithm should avoid unnecessary calculations.

An example of this calculation optimization is when the Q matrix is calculated [src/FusionEKF.cpp](./src/kalman_filter.cpp#L141) line 135 to line 144.

## Video Output

[Video Link](https://youtu.be/TmfqCB15n90)