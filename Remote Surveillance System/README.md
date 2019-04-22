# Remote Surveillance System of the heavy machinery
### Introduction:
The project was ideated and the basic draft was created in a 24 hours long make-a-thon. The system uses various sensor feeds to display to the user a realtime graph all the values. A camera feed is provided to the user to be able to see the condition of the machinery. The data from the sensors gathered is uploaded to a firebase database.The realtime graph is displayed using matplotlib. The whole project is backboned by python and it is the major language used for the development of the major systems.

### Walk through the components:

### Firebase and python:
##### Firebase:
Firebase is a Backend as a service(BAAS) started as a startup and grew up to be this amazing and easy app development platform on Google Cloud Platform. It provides with a number of services but for our project we simply use the realtime database. It also provides tools for authentication and ML operations which is intended to be included in the project as soon as I get time to complete the system with all the functionalities mentioned in the later section. The firebase realtime database provides a means to set a fixed number of variables and change the values to be stored.
##### Python:
Pytohn is the most amazing programming language I have come accross till now. It have the power to demolish the worlds and yet as simple as it could be. We use python for a number of things in this project. Actually the whole project is done in python except the web page viz developed in HTML,CSS and will later use javascript to include a realtime graph on the page(although I am finding a good way to do it using python, currently it seems easier done in javascript). We use the Pyrebase library for making connections and receive data from the firebase. It's easy to install pyrebase just do the ```#pip install pyrebase``` and you're good to go.
Refer to the following [github page](https://github.com/thisbejim/Pyrebase) for details.
