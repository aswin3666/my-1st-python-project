from tkinter import*
from tkinter import font as tkFont
expression=""
#numbers and operators displaying function
def press(num):
	global expression
	expression=expression + str(num)
	equation.set(expression)
#equal pressing 
def equal_press():
	try:
		global expression
		total=str(eval(expression))
		equation.set(total)
		expression=""
	except:
		equation.set("error")
		expression=""
#clear display fuctions
def clear():
	equation.set("")

window=Tk()
window.geometry("380x527")
window.configure(bg="black")
equation=StringVar()
expression_field = Entry(window,bg="#C0C0C0",font="Helvetica 15",textvariable=equation,cursor="none")
	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure
expression_field.grid(columnspan=4,ipadx=80,ipady=40)
#button creations
button0=Button(window,text="0",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(0))
button0.grid(column=0,row=2)
button1=Button(window,text="1",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(1))
button2=Button(window,text="2",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(2))
button3=Button(window,text="3",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(3))
button4=Button(window,text="4",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(4))
button5=Button(window,text="5",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(5))
button6=Button(window,text="6",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(6))
button7=Button(window,text="7",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(7))
button8=Button(window,text="8",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(8))
button9=Button(window,text="9",width=12,height=5,bg="skyblue",fg="black",command=lambda:press(9))
button_equal=Button(window,text="=",width=12,height=5,bg="skyblue",fg="black",command=lambda:equal_press())
button_add=Button(window,text="+",width=12,height=5,bg="skyblue",fg="black",command=lambda:press("+"))
button_minus=Button(window,text="-",width=12,height=5,bg="skyblue",fg="black",command=lambda:press("-"))
button_float=Button(window,text=".",width=12,height=5,bg="skyblue",fg="black",command=lambda:press("."))
button_divide=Button(window,text="/",width=12,height=5,bg="skyblue",fg="black",command=lambda:press("/"))
button_multi=Button(window,text="x",width=12,height=5,bg="skyblue",fg="black",command=lambda:press("*"))
button_clear=Button(window,text="C L E A R A L L",width=53,height=5,bg="#00bfff",command=lambda:clear())

#button placements
button1.grid(row=2,column=1)
button2.grid(row=2,column=2)
button3.grid(row=2,column=3)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=3,column=3)
button8.grid(row=4,column=0)
button9.grid(row=4,column=1)
button_equal.grid(row=4,column=2)
button_add.grid(row=4,column=3)
button_minus.grid(row=5,column=0)
button_float.grid(row=5,column=1)
button_divide.grid(row=5,column=2)
button_multi.grid(row=5,column=3)
button_clear.grid(row=6,columnspan=4)
window.mainloop()