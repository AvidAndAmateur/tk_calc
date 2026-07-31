import tkinter as tk
from time import sleep
root = tk.Tk()
root.geometry("350x500")
root.title('calculator')
state = 'one'
firstinp = ""
secondinp = ""
operator = ""
finalout = 0 #final calculated answer
text = "" #used as the display so you can see your equation
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
outputwindow = tk.Frame(root,width=250,height=250,bg="lightgrey",padx=5,pady=5)
buttonwindow = tk.Frame(root,width=100,height=45,bg='darkgrey',padx=5,pady=5)
#from text to here it is basic customising of frames
outputwindow.grid_propagate(False)
buttonwindow.grid_propagate(True)
outputwindow.grid(row=0,column=0)
buttonwindow.grid(row=1,column=0)
output = tk.Label(outputwindow, text='')
finaloutput = tk.Label(outputwindow,text='')
def addtext(x,onetwo): #adds text to the window so you can see your operation
    global firstinp
    global secondinp
    if onetwo == "one":
        firstinp+=str(x)
        text = firstinp
        output.config(text=text)
    elif onetwo == "two":
        secondinp+=str(x)
        text = firstinp+operator+secondinp
        output.config(text=text)
def add(): #adds variables and adds operator to screen
    global operator
    global state
    global text
    operator = "+"
    text = firstinp+operator
    state = "two"
    output.config(text=text)
def sub(): #subtracts variables and adds operator to screen
    global operator
    global state
    global text
    operator = "-"
    text = firstinp+operator
    state = "two"
    output.config(text=text)
def mult(): #multiplies variables and adds operator to screen
    global operator
    global state
    global text
    operator = "*"
    text = firstinp+operator
    state = "two"
    output.config(text=text)
def operations(): #calculates final answer then presents it to output screen
    global finalout
    if operator == "+" and len(operator)==1:
        finalout=int(firstinp)+int(secondinp)
        finaloutput.config(text=finalout)
    elif operator == "-" and len(operator)==1:
        finalout=int(firstinp)-int(secondinp)
        finaloutput.config(text=finalout)
    elif operator == "*" and len(operator)==1:
        finalout=int(firstinp)*int(secondinp)
        finaloutput.config(text=finalout)
    else:
        finaloutput.config(text='error')
        sleep(1.5)
        clear()
def clear(): #clears all stores and screen to begin new op
    global finalout
    global operator
    global state
    global firstinp
    global secondinp
    state = 'one'
    firstinp = ""
    secondinp = ""
    operator = ""
    finalout = 0
    output.config(text='')
    finaloutput.config(text='')
btn0 = tk.Button(buttonwindow, text='0', command=lambda: addtext(0,state),padx=5)
btn1 = tk.Button(buttonwindow, text='1', command=lambda: addtext(1,state),padx=5)
btn2 = tk.Button(buttonwindow,text='2',command=lambda: addtext(2,state),padx=5)
btn3 = tk.Button(buttonwindow,text='3',command= lambda: addtext(3,state),padx=5)
btn4 = tk.Button(buttonwindow, text='4', command=lambda: addtext(4,state),padx=5)
btn5 = tk.Button(buttonwindow, text='5', command=lambda: addtext(5,state),padx=5)
btn6 = tk.Button(buttonwindow, text='6', command=lambda: addtext(6,state),padx=5)
btn7 = tk.Button(buttonwindow, text='7', command=lambda: addtext(7,state),padx=5)
btn8 = tk.Button(buttonwindow, text='8', command=lambda: addtext(8,state),padx=5)
btn9 = tk.Button(buttonwindow, text='9', command=lambda: addtext(9,state),padx=5)
btnx = tk.Button(buttonwindow,text='X',command=mult,padx=5)
btnp = tk.Button(buttonwindow,text='+',command=add,padx=5)
btns = tk.Button(buttonwindow,text='-',command=sub,padx=5)
btne = tk.Button(buttonwindow,text='=',command=operations,padx=5)
btnc = tk.Button(buttonwindow,text='CLR',command=clear,padx=5)
btn0.grid(row=0,column=0)
btn1.grid(row=0,column=1)
btn2.grid(row=0,column=2)
btn3.grid(row=2,column=0)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=3,column=0)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=4,column=0)
btnx.grid(row=4,column=1)
btnp.grid(row=4,column=2)
btns.grid(row=5,column=0)
btne.grid(row=5,column=1)
btnc.grid(row=5,column=2)
output.grid(row=0,column=0)
finaloutput.grid(row=1,column=0)
#everything from line 86 to here is setting up buttons and their functions
root.mainloop() #runs window