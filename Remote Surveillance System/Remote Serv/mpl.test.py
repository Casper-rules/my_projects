import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pyrebase
from datetime import datetime
config = {
    "apiKey": "AIzaSyDFbUqL2L-mjNI81IEgdzwKPdvhyG1b8GQ",
    "authDomain": "controls-204d0.firebaseapp.com",
    "databaseURL": "https://controls-204d0.firebaseio.com/",
    "storageBucket": "controls-204d0.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


# style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

x = []
y = []
y2 = []


def anim(i):
    user = db.child("Controls").get()
    global x, y, y2

    if len(x) > 10 or len(y) > 10 or len(y2) > 10:
        x = x[1:]
        y = y[1:]
        y2 = y2[1:]

    time = datetime.now()
    y.append(float(user.val()['current']))
    y.sort()
    y2.append(float(user.val()['voltage']))
    y2.sort()
    x.append(time)
    ax1.clear()
    ax1.plot(x, y, label='$y = current')
    ax1.plot(x, y2, label='$y2 = voltage')
    for i, j in zip(x, y):
        ax1.annotate(str("%.2f" % j), xy=(i, j))
    for i, j in zip(x, y2):
        ax1.annotate(str("%.2f" % j), xy=(i, j))

    ax1.legend()


animate = animation.FuncAnimation(fig, anim, interval=1000)
plt.show()
