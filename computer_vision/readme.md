# Image processing using opencv and python 
## What:
This section is to describe what the tools used
#### Image processing:
Image processing is basically to take an image as an input and produce an output image with some modification and information extraction. here in the below codes, I have used opencv and python2 for a number of applications

#### What you need before this :
##### Python:
Python is one of the most simple yet elegant programming languages. It is super easy to learn and has a hell load of applications. Since the codes are in python, it is logical to expect enough profeciency in python. Following are some of the concepts needed 
..* basic keywords and flow controls
..* creating functions in python
..* working with classes in python
..* working with numpy arrays
..* data structures in python
..* working with modules


If on a linux system, it is most probable that you already have a version of python2 and 3 already installed. If not, execute following commands from your terminal to install python:

```$sudo apt-get install python```


```$sudo apt-get install python3```

To enter the python shell fronm terminal, simply run

```$python```

or

```$python3```

we also need numpy, to install numpy, run


```$sudo apt-get install python-numpy```


##### Opencv:

To run the above codes it is important that we have the latest version of opencv installed on the system.

The easy way to do so is:

```$sudo apt-get install python-opencv```

it installs opencv and basic libraries needed to run the above codes

The proper way takes more time and commands to install, hence reffer to the following [link](https://docs.opencv.org/3.4/d7/d9f/tutorial_linux_install.html)


To read about and learn basic methods of opencv and how to use them, the best source are the [opencv documentations](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) 


## Intentions:
This section is to explain what the above codes do. The codes are comprised of all the initial codes used to learn how opencv works and then there are some applications created by using opencv.The programms were made with an intention to be used for making an object recognition sub-system for the system designed to run the robots for ROBOCON-2018.
#### imlod.py:
this program's main intention is to take an image input. It was further extended to test some methods used to handle the image and manipulate it. It also uses the matplotlib library of pytohn to plot the image(i.e to show the image in a new window).I have used poly and line methods of opencv to draw line and polygons. 
#### vidlod.py:
vidlod.py basically is video loading program. It actually uses the webcam attached to your system to read the video. Every frame is basically an image hence the functions in imlod.py are useful for the frame too. In this code we convert the video to grayscale by converting the frame images to grayscale, and show both the original and the grayed videos.
#### hsv_cv.py:
The program is used to convert the bgr video to hsv for filtering out the objects of a perticular color. The code can be used as object color distinguisher(for a given set of colors)
#### converter_hsv.py:
is more of a utility program. it is used to get the lower and higher values for hue in a given frame

#### edge_det.py:
This program takes in an image and returns a thresholded(i.e only white and black pixels) where only edges are highlighted. The code can be modifies to detect edges. Can be used for making a line follower using image processing.
#### line_follow.py:
A sample program for line following. The hsv filter values are set to detect a perticular colored line. Edge detection can also be used to achieve the task although we use contours. There can be many algos for this task.
#### face_det.py:
This program detects a human face using an already trained classifier for the same. The output video has a rectangle arround the face, specifing that a face has been detected. Again this program can be extended to make many cool projects.
#### ballColorDet.py:
This program was made for ROBOCON problem statement. It's purpose is to detect if the ball is of one of the given colors, and set appropriate flag variables.
#### weight.py
This is a fun project program. The task was to determine the weight of liquid in a given bottle. We assumed the bottle to be cylinder although with minor changes, the code can be actually put to use for some greater goods.
