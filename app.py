#Importing the module tkinter:
from tkinter import *
#Defining the root and it's geometry:
root = Tk()
root.geometry('300x300')
#Defining the labels needed and the entries too:
myLabel = Label(root, text="Your Email")
myLabel.pack()

entry = Entry(text="Password", bd=5, cursor="arrow", justify=CENTER)
entry.pack()

myLabel2 = Label(root, text="Your Password")
myLabel2.pack()

entry2 = Entry(text="Email", bd=5, cursor="arrow", justify=CENTER)
entry2.pack()
#Defining the function that is going to stock our passwords and emails:
def stock_the_data():
	infos = "*********\n" + "      The email is : " + entry.get() + " and the password is : " + entry2.get() + "\n**********************"
	a = open('#Your file name and path to it here', 'a') 
	a.write(infos)
	a.close()
#Defining the function that is going to print our data in the screen:
def buttonAction():
	label3 = Label(root, text="Your email is: " + entry.get())
	label3.pack()

	label = Label(root, text="Your password is: " + entry2.get())
	label.pack()
	
button = Button(root, text = "Submit", command=buttonAction)
button.pack()

button2 = Button(root, text = "Stock the data",command= stock_the_data)
button2.pack()

root.mainloop()
