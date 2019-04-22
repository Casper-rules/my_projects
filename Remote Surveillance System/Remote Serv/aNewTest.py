from flask import Flask, render_template
# import pyrebase
# import sklearn


app = Flask(__name__)
# config = {
#     "apiKey": "AIzaSyDFbUqL2L-mjNI81IEgdzwKPdvhyG1b8GQ",
#     "authDomain": "controls-204d0.firebaseapp.com",
#     "databaseURL": "https://controls-204d0.firebaseio.com/",
#     "storageBucket": "controls-204d0.appspot.com"
# }

# firebase = pyrebase.initialize_app(config)
# db = firebase.database()

# sensorValue = 4.0
# predicted_danger = False


@app.route('/')
def root():
    # global predicted_danger
    # user = db.child("Controls").get()
    # current = str("%.2f" % float(user.val()['current']))
    # if float(current)-sensorValue >= 0.8:
    #     predicted_danger = True
    # volt = user.val()['voltage']
    # temp = user.val()['temperature']
    # rpm = user.val()['rpm']
    # danger = "Yes" if predicted_danger else "No"
    # , current=current, voltage=volt, temp=temp, rpm=rpm, danger=danger)
    return render_template('main.html')


app.run(debug=True)
