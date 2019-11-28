from tkinter import *
import os
import numpy as np
import pickle

#create a window
root=Tk()
#title for the window
root.title('Taxi Fare Prediction')
#shape of the window
root.geometry("600x400")

#set a lable to inform user waht to do
userTypeLabel=Label(root,text="New User? (choose one) : ")
userTypeLabel.grid(row=0,column=0) #the grid method assumes the whole window to be made of grids and places the widgets in specified grid

#checkboxes for new or old user
new_user_NO=DoubleVar()
new_user_YES=DoubleVar()
chkbtn_n = Checkbutton(root, text = "No", variable = new_user_NO, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)  
chkbtn_y = Checkbutton(root, text = "Yes", variable = new_user_YES, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)
chkbtn_n.grid(row=1,column=0)
chkbtn_y.grid(row=1,column=1)  

#toll amount
tollAmountLabel=Label(root,text="Enter toll amount : ")
tollAmountLabel.grid(row=2,column=0)

tollAmount=Entry(root)
tollAmount.grid(row=2,column=1)

#tip money
tipAmountLabel=Label(root,text="Enter amount of tip : ")
tipAmountLabel.grid(row=3,column=0)

tip=Entry(root)
tip.grid(row=3,column=1)

#mta_tax
mta_taxLabel=Label(root,text="Enter mta_tax : ")
mta_taxLabel.grid(row=4,column=0)

mta_tax=Entry(root)
mta_tax.grid(row=4,column=1)

#number of passengers
passengerCountLabel=Label(root,text="Enter number of passengers : ")
passengerCountLabel.grid(row=5,column=0)

passengerCount=Entry(root)
passengerCount.grid(row=5,column=1)

#type of payment preffered(checkbox)
paymentTypeLabel=Label(root,text="Choose a payment type : ")
paymentTypeLabel.grid(row=6,column=0)

payment_type_CRD=DoubleVar()
payment_type_CSH=DoubleVar()
payment_type_DIS=DoubleVar()
payment_type_NOC=DoubleVar()
payment_type_UNK=DoubleVar()

chkbtn1 = Checkbutton(root, text = "payment_type_CRD", variable = payment_type_CRD, onvalue =1.0, offvalue = 0.0, height = 2, width = 15)  
chkbtn2 = Checkbutton(root, text = "payment_type_CSH", variable = payment_type_CSH, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)  
chkbtn3 = Checkbutton(root, text = "payment_type_DIS", variable = payment_type_DIS, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)  
chkbtn4 = Checkbutton(root, text = "payment_type_NOC", variable = payment_type_NOC, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)  
chkbtn5 = Checkbutton(root, text = "payment_type_UNK", variable = payment_type_UNK, onvalue = 1.0, offvalue = 0.0, height = 2, width = 15)
#positioning checkboxes to make it look good
chkbtn1.grid(row=7,column=0)
chkbtn2.grid(row=7,column=3)
chkbtn3.grid(row=8,column=0)
chkbtn4.grid(row=8,column=3)
chkbtn5.grid(row=9,column=0)

#surcharge
surchargeLabel=Label(root,text="Enter surcharge : ")
surchargeLabel.grid(row=10,column=0)

surcharge=Entry()
surcharge.grid(row=10,column=1)

#distance covered
distanceLabel=Label(root,text="Enter the distance : ")
distanceLabel.grid(row=11,column=0)

distance=Entry(root)
distance.grid(row=11,column=1)

#textbox to show result
result=Label(root,text="predictions shown here")
result.grid(row=14,column=2)

#creating function to make prediction using saved regression model(random forest regressor)
with open('randomForest.pickle','rb') as clf:
    myClf=pickle.load(clf)
def predict():
    toll=tollAmount.get()
    tips=tip.get()
    m_tax=mta_tax.get()
    pass_count=passengerCount.get()
    s_charge=surcharge.get()
    dist=distance.get()
    valList=[
                float(str(toll)),
                float(str(tips)),
                float(str(m_tax)),
                float(str(pass_count)),
                float(str(s_charge)),
                float(str(dist)),
                float(str(new_user_NO.get())),
                float(str(new_user_YES.get())),
                float(str(payment_type_CRD.get())),
                float(str(payment_type_CSH.get())),
                float(str(payment_type_DIS.get())),
                float(str(payment_type_NOC.get())),
                float(str(payment_type_UNK.get()))
            ]
    features=np.array(valList).reshape(1,-1)
    prediction=myClf.predict(features)
    result['text']="Rs. "+str(prediction)

button = Button(root,text = "Predict",command = predict,activeforeground = "red",activebackground = "green",pady=10)
button.grid(row=12,column=2)


root.mainloop()