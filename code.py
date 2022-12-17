from tkinter import *
from PIL import Image,ImageTk
screen = Tk()
screen.geometry("450x550")
screen.title("Calculator")

def click(event):
    global entry_value
    value = entry_value.get()
    digit = event.widget.cget("text")
    if(digit == "AC"):
        entry_value.set(" ")
    elif(digit == "Del"):
        value = value[:-1]
        entry_value.set(value)
    elif(digit == "="):
        try:
            num_lst = []
            oper_lst  =[]
            num = ""
            for i in value:
                if(i=="+" or i=="-" or i=="×" or i=="÷"):
                    oper_lst.append(i)
                    num_lst.append(num)
                    num = ""
                else:
                    num = num+i
            num_lst.append(num)
            index = 0
            while(index < len(oper_lst)):
                if(oper_lst[index]=="×"):
                    num_lst[index] = float(num_lst[index]) * float(num_lst[index+1])
                    del oper_lst[index]
                    del num_lst[index+1]
                    index -= 1

                elif(oper_lst[index]=="÷"):
                    num_lst[index] = float(num_lst[index]) / float(num_lst[index+1])
                    del oper_lst[index]
                    del num_lst[index+1]
                    index -= 1
                index += 1
            
            index = 0
            while(index < len(oper_lst)):
                if(oper_lst[index]=="+"):
                    num_lst[index] = float(num_lst[index]) + float(num_lst[index+1])

                elif(oper_lst[index]=="-"):
                    num_lst[index] = float(num_lst[index]) - float(num_lst[index+1])
                    
                del oper_lst[index]
                del num_lst[index+1]

            value = num_lst[0]
            entry_value.set(value)
        except:
            entry_value.set("Syntax Error")
    else:
        entry_value.set(value + digit)
    
def button(label,r,c,color):
    b = Button(f1,text=label ,font="lucuda 33 bold",height=1,width=2,fg=color,relief=RAISED,bd=4)
    b.grid(row=r,column=c)
    b.bind("<Button-1>",click)

sign = Image.open("Shourya.png")
sign = sign.resize((100,35),Image.Resampling.LANCZOS)
sign = ImageTk.PhotoImage(sign)

f0 = Frame(screen,padx=20,pady=15,relief=GROOVE,bd=10,bg="grey")
Label(image=sign,bg="grey").place(relx=0.08,rely=0.02,anchor=NW)
entry_value = StringVar()
entry_value.set(" ")
entry_widget = Entry(f0,font="lucuda 33",textvariable=entry_value,relief=SUNKEN,bd=7)
entry_widget.pack(pady=25)

f1 = Frame(f0,bg="grey",relief=GROOVE,bd=5)
button("9",0,0,"black")
button("8",0,1,"black")
button("7",0,2,"black")
button("Del",0,3,"red")
button("AC",0,4,"red")
button("6",1,0,"black")
button("5",1,1,"black")
button("4",1,2,"black")
button("+",1,3,"orange")
button("-",1,4,"orange")
button("3",2,0,"black")
button("2",2,1,"black")
button("1",2,2,"black")
button("×",2,3,"orange")
button("÷",2,4,"orange")
button(".",3,0,"black")
button("0",3,1,"black")
button("00",3,2,"black")
button("=",3,3,"green")
f1.pack(side=TOP)
f0.pack()

screen.mainloop()