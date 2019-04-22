# Remote Surveillance System of the heavy machinery
### Introduction:
The project was ideated and the basic draft was created in a 24 hours long make-a-thon. The system uses various sensor feeds to display to the user a realtime graph all the values. A camera feed is provided to the user to be able to see the condition of the machinery. The data from the sensors gathered is uploaded to a firebase database.The realtime graph is displayed using matplotlib. The whole project is backboned by python and it is the major language used for the development of the major systems.We use **Raspberry Pi 3B+** for data collections and loading the data to cloud.

### Walk through the components:

### Firebase and python:
##### Firebase:
Firebase is a Backend as a service(BAAS) started as a startup and grew up to be this amazing and easy app development platform on Google Cloud Platform. It provides with a number of services but for our project we simply use the realtime database. It also provides tools for authentication and ML operations which is intended to be included in the project as soon as I get time to complete the system with all the functionalities mentioned in the later section. The firebase realtime database provides a means to set a fixed number of variables and change the values to be stored.
##### Python:
Pytohn is the most amazing programming language I have come accross till now. It have the power to demolish the worlds and yet as simple as it could be. We use python for a number of things in this project. Actually the whole project is done in python except the web page viz developed in HTML,CSS and will later use javascript to include a realtime graph on the page(although I am finding a good way to do it using python, currently it seems easier done in javascript). We use the Pyrebase library for making connections and receive data from the firebase. It's easy to install pyrebase just do the ```#pip install pyrebase``` and you're good to go.
Refer to the following [github page](https://github.com/thisbejim/Pyrebase) for details.

### The User Interface:
The user interface was devided into two parts:
#### The web Page:
The web page designed in HTML, CSS and hosted on python flask. Was created for the user to be able to get the feed from the camera on site. The Camera feed streaming is currently done using a **pi cam** on the pi but we can also achieve live feed streaming from a web camera using **motion** server on linux(raspbian). The page also had various values shown on the page. The user is given an option to change the values of the current and voltage remotely. The value changed is updated in the firebase too. In this project, Pi acted as a server and on receiving the values from the user, dialed down a servo connected to a potentiometer to regulate current and potential.
#### The android app:
The app will be created to receive the current and potential values the phone and also allowed the user to change the values. The app had almost all facilitiees of the web app except for the live feed.

#### The Graph:
Currently the graph is plot on a seperate window currently using matplotlib is later to put in the web page itself hopefully using python (fingers crossed ::p:).The graph takes the values form the database and stores the values of the features in seperate queues and plots the features against time(again stored in a queue and taken from the system using the datetime library in python).
#### The Live feed : 
As mentioned earlier, the feed is provided using pi cam server which can also be achieved by other servers and camras. one alternative being the motion server.

## The Future:
I intend to extend the project to be able to take in the input sensor values and be able to predict the time it will take for machine to fail. Also put the graph on the web page using python itself. Also I wish to use the live feed as the background of the web page(still experimenting about that).I also will try to provide more remote control for the machine operations.

Moral of the story, **This is the first version of the surveillance system, a very expandable system for remote heavy machinery.**
