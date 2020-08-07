from tkinter import *

cal=Tk()

cal.title("Calaculator by ROHAN the Devil")
textentry=Entry(cal,borderwidth=5,width=50 )
textentry.grid(row=0,column=0,columnspan=4,pady=3)


def numpress(number):
	current=textentry.get()
	textentry.delete(0,END)
	curr_val =str(current)+str(number)
	textentry.insert(0,curr_val)

def clrscr():
	textentry.delete(0,END)

def plus():
	scrno=textentry.get()
	global f_num
	global math
	math="add"
	f_num=int(scrno)
	textentry.insert(numpress('+'))


def minus():
	scrno=textentry.get()
	global f_num
	global math
	math="sub"
	f_num=int(scrno)
	textentry.insert(numpress('-'))

def multiply():
	scrno=textentry.get()
	global f_num
	global math
	math="mul"
	f_num=int(scrno)
	textentry.insert(numpress('x'))

def divide():
	scrno=textentry.get()
	global f_num
	global math
	math="div"
	f_num=int(scrno)
	textentry.insert(numpress('/'))

def equal():
	scrno=textentry.get()
	for i in str(scrno):
		if i == "+"or i=="-" or i=="x" or i=="/":
			scrno=scrno[(str(scrno).index(i))+1:]
	textentry.delete(0,END)
	if math == "add":
		value= int(f_num+int(scrno))
	if math == "sub":
		value= int(f_num-int(scrno))
	if math == "mul":
		value= int(f_num*int(scrno))
	if math == "div":
		value= f_num/int(scrno)
		if value.is_integer():
			value=int(value)
		else:
			value=value
	textentry.insert(0, value)


button_0 = Button(cal,text="0",padx=30,pady=10,borderwidth=3,command=lambda:numpress(0))
button_1 = Button(cal,text="1",padx=30,pady=10,borderwidth=3,command=lambda:numpress(1))
button_2 = Button(cal,text="2",padx=30,pady=10,borderwidth=3,command=lambda:numpress(2))
button_3 = Button(cal,text="3",padx=30,pady=10,borderwidth=3,command=lambda:numpress(3))
button_4 = Button(cal,text="4",padx=30,pady=10,borderwidth=3,command=lambda:numpress(4))
button_5 = Button(cal,text="5",padx=30,pady=10,borderwidth=3,command=lambda:numpress(5))
button_6 = Button(cal,text="6",padx=30,pady=10,borderwidth=3,command=lambda:numpress(6))
button_7 = Button(cal,text="7",padx=30,pady=10,borderwidth=3,command=lambda:numpress(7))
button_8 = Button(cal,text="8",padx=30,pady=10,borderwidth=3,command=lambda:numpress(8))
button_9 = Button(cal,text="9",padx=30,pady=10,borderwidth=3,command=lambda:numpress(9))

button_equal = Button(cal,text="=",padx=30,pady=10,borderwidth=3,command=equal)
button_clrscr = Button(cal,text="C",padx=30,pady=10,borderwidth=3,command=clrscr)

button_plus = Button(cal,text="+",padx=30,pady=10,borderwidth=3,command=plus)
button_minus = Button(cal,text="-",padx=30,pady=10,borderwidth=3,command=minus)
button_multiply = Button(cal,text="x",padx=30,pady=10,borderwidth=3,command=multiply)
button_divide = Button(cal,text="/",padx=30,pady=10,borderwidth=3,command=divide)



button_1.grid(row=4,column=1)
button_2.grid(row=4,column=2)
button_3.grid(row=4,column=3)

button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)

button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)

button_0.grid(row=5,column=2)

button_equal.grid(row=5,column=3)
button_clrscr.grid(row=5,column=1)

button_plus.grid(row=2,column=0)
button_minus.grid(row=3,column=0)
button_multiply.grid(row=4,column=0)
button_divide.grid(row=5,column=0)




cal.mainloop()
