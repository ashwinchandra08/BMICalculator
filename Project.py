from tkinter import *
from tkinter.font import *
import webbrowser
import Standard

window=Tk() #creating window
window.title("BMI Calculator")
window.geometry('600x600')
window.config(bg='grey17') #setting window background colour

bg = PhotoImage(file="healthbg.png") #setting background image
mylabell=Label(window,image=bg)
mylabell.place(x=0,y=0,relwidth=1,relheight=1)

frame=Frame(window,padx=10,pady=10,highlightbackground="black",highlightthickness=4)
frame.pack(side=LEFT,expand=True)

frameURL=Frame(frame)
frameURL.grid(row=7,columnspan=3,pady=10)   

def callback(url):
    webbrowser.open_new_tab(url)

#Display Input
Label(frame,text="Enter Age(2-120)",font=("Raleway",12)).grid(row=1,column=1) 
age=Entry(frame)
age.grid(row=1,column=2,pady=5)

gender= Label(frame,text='Select Gender',font=("Raleway",12)) 
gender.grid(row=2,column=1)
var=IntVar() #holds integer data 
frame2 = Frame(frame)
frame2.grid(row=2,column=2,pady=5)
male=Radiobutton(frame2,text ='Male',variable=var,value=0,font=("Raleway",12))
male.pack(side=LEFT)
female_rb = Radiobutton(frame2,text ='Female',variable=var,value=1,font=("Raleway",12))
female_rb.pack(side=RIGHT)

height=Label(frame)
weight=Label(frame)
hf=Label(frame)
wl=Label(frame)

height=Label(frame,text="Enter Height (in cm)",font=("Raleway",12))
height.grid(row=3,column=1,sticky=N)
e_height=Entry(frame)
e_height.grid(row=3,column=2,pady=5,sticky=N)
weight=Label(frame,text="Enter Weight (in kg)",font=("Raleway",12))
weight.grid(row=4,column=1,sticky=N)
e_weight=Entry(frame)
e_weight.grid(row=4,column=2,pady=5)

frame3 = Frame(frame)
frame3.grid(row=5,columnspan=3,pady=10)
bm=Frame(frame3)
bs=Frame(frame3)

frame4=Frame(frame)
frame4.grid(row=6,columnspan=3,pady=10)

def bmi_calculate(): #function to calculate BMI
    h=float(e_height.get())/100
    w=float(e_weight.get())
    bmi=w/h**2
    bmi=round(bmi,1)
    bmi_show(bmi)
    bm["state"]="disabled" #disabling button 

def bmi_show(bmi): #function to display output
    link=Label(frameURL,text="Take Action Towards Better Health",font=('Helvet icabold',10),fg="blue", cursor="hand2") #creating hyperlink
    Label(frame4,text="The BMI is "+str(bmi)+"\n").pack()
    if (bmi <= 18.5):
        Label(frame4,text="UNDERWEIGHT\n\n Click on the link below to know \n more about your health status").pack(side=BOTTOM)
        link.pack(pady=8)
        link.bind("<Button-1>", lambda e:
        callback("https://www.healthdirect.gov.au/what-to-do-if-you-are-underweight"))  
    elif ( bmi > 18.5 and bmi <= 24.9):
        Label(frame4,text="HEALTHY\n\n Click on the link below to know \n more about your health status").pack(side=BOTTOM)
        link.pack(pady=8)
        link.bind("<Button-1>", lambda e:
        callback("https://www.hioscar.com/blog/how-to-maintain-a-healthy-body-mass-index-bmi"))
    elif ( bmi > 24.9 and bmi < 30):
        Label(frame4,text="OVERWEIGHT\n\n Click on the link below to know \n more about your health status").pack(side=BOTTOM)
        link.pack(pady=8)
        link.bind("<Button-1>", lambda e:
        callback("https://www.diabetes.co.uk/bmi/what-to-eat-to-lower-bmi.html"))
    elif ( bmi >= 30):
        Label(frame4,text="OBESITY\n\n Click on the link below to know \n more about your health status").pack(side=BOTTOM) 
        link.pack(pady=8)
        link.bind("<Button-1>", lambda e:
        callback("https://www.doconline.com/what-we-treat/obesity-weight-loss"))

def reset(): #function to clear the data inputed 
    age.delete(0,'end')
    e_height.delete(0,'end')
    e_weight.delete(0,'end')
    for widgets in frame4.winfo_children(): #destroying info in that frame
        widgets.destroy()
    for widgets in frameURL.winfo_children():
        widgets.destroy()
    bm["state"]="normal"
    bs["state"]="normal"

def bmi_standard(): #function to change input to standard data
    global hf,wl,bs,bm
    height.grid_forget()
    weight.grid_forget()
    bm.pack_forget()
    hf=Label(frame,text="Enter Height (in feet inches)",font=("Raleway",11))
    hf.grid(row=3,column=1)
    wl=Label(frame,text="Enter Weight (in lbs)",font=("Raleway",12))
    wl.grid(row=4,column=1,sticky=N)
    bs=Button(frame3,text="Compute BMI",command=s_calculate)
    bs.pack(side=LEFT)
    b5["state"] = "normal"
    b4["state"] = "disabled"

def s_calculate(): #function to call custom module to calculate standard result
    bs["state"]="disabled"
    result=Standard.bmi_s(e_height.get(),e_weight.get())
    bmi_show(result)
    
def bmi_metric():
    hf.grid_forget()
    wl.grid_forget()
    bs.pack_forget()
    bm.pack(side=LEFT)
    height.grid(row=3,column=1,sticky=N)
    weight.grid(row=4,column=1,sticky=N)
    b4["state"] = "normal"
    b5["state"] = "disabled"

#Displaying BMI categories for user to understand
frame5=Frame(window,padx=10,pady=10,relief=SUNKEN,highlightbackground="black",highlightthickness=4)
frame5.pack(side=RIGHT,expand=True)
Label(frame5,text="BMI categories",font=("Verdana",10,'bold'),relief=RIDGE).pack(padx=5)
Label(frame5,text="Underweight =< 18.5",font=("Verdana",10)).pack(padx=5)
Label(frame5,text="Normal weight = 18.5–24.9",font=("Verdana",10)).pack(padx=5)
Label(frame5,text="Overweight = 25–29.9",font=("Verdana",10)).pack(padx=5)
Label(frame5,text="Obesity = BMI of 30 or greater",font=("Verdana",10)).pack(padx=5)
Label(frame5,text="",font=("Verdana",10)).pack(padx=5)

frame6=Frame(frame5)
frame6.pack(side=BOTTOM)

#creating buttons
bm=Button(frame3,text="Compute BMI",command=bmi_calculate)
bm.pack(side=LEFT)
B2=Button(frame3,text="Exit",command=lambda:window.destroy()).pack(side=RIGHT)
B3=Button(frame3,text="Reset",command=reset).pack(side=RIGHT)
b4=Button(frame6,text="Standard",command=bmi_standard)
b4.pack(side=LEFT)
b5=Button(frame6,text="Metric",command=bmi_metric)
b5.pack(side=LEFT)
b5["state"] = "disabled"

window.mainloop()