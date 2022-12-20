from tkinter import *
from PIL import Image,ImageTk
screen = Tk()
screen.geometry("450x550")
screen.title("Calculator")

# This function runs when user clicks any button 
def click(event):
    global entry_value
    # 'value' is the value that entry widgit is showing
    value = entry_value.get()

    # digit is value of button that user press
    digit = event.widget.cget("text")

    if(digit == "AC"):
        entry_value.set(" ")
    elif(digit == "Del"):
        value = value[1:-1]
        entry_value.set(" " + value)
    
    # Runs when user press "=" button
    elif(digit == "="):
        try:
            # num_lst - stores all the numbers
            # oper_lst - stores all the operators
            num_lst = []
            oper_lst  =[]
            num = ""
            # Seperating numbers and operators from value
            for i in range(len(value)):
                if(value[i]=="-"):
                    if(value[i-1].isdigit() or value[i-1]=="."):
                        num_lst.append(num)
                        oper_lst.append("+")
                    num = "-"

                elif(value[i]=="+" or value[i]=="×" or value[i]=="÷"):
                    oper_lst.append(value[i])
                    num_lst.append(num)
                    num = ""
                else:
                    num = num+value[i]
            num_lst.append(num)

            # First solving all the multiply and devide operators
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
            
            # Second solving all plus and minus operators
            index = 0
            while(index < len(oper_lst)):
                if(oper_lst[index]=="+"):
                    num_lst[index] = float(num_lst[index]) + float(num_lst[index+1])

                elif(oper_lst[index]=="-"):
                    num_lst[index] = float(num_lst[index]) - float(num_lst[index+1])
                    
                del oper_lst[index]
                del num_lst[index+1]

            # Showing the result
            value = num_lst[0]
            entry_value.set(value)
        except:
            entry_value.set("Syntax Error")
    else:
        # Program runs when user press any number
        if(digit.isdigit() or digit=="."):
            entry_value.set(value + digit)

        # When user press percentage button, it devide previous digit by 100
        elif(digit=="%" and value[-1].isdigit()):
            i = -1
            while(-i<=len(value)):
                if(value[i].isdigit() or value[i]=="."):
                    pass
                else:
                    entry_value.set(value[:i+1] + str(float(value[i+1:])/100))
                    break
                i = i-1

        # Program when user press "-" operator
        elif(digit=="-"):
            if(value[-1]=="+" or value[-1]=="-"):
                entry_value.set(value[:-1] + digit)
            else:
                entry_value.set(value + digit)

        # Program when user press any other operator
        elif(digit=="+" or digit=="×" or digit=="÷"):
            if(value[-1].isdigit() or value[-1]=="."):
                entry_value.set(value + digit)
            elif(value[-1]==" "):
                pass
            else:
                # If there previous digit is also operator
                i = -1
                while(-i<=len(value)):
                    if(value[i]==" "):
                        break
                    elif(value[i].isdigit() or value[i]=="."):
                        entry_value.set(value[:i+1] + digit)
                        break
                    i = i-1
             
# This is a function which makes button
def button(label,r,c,color):
    b = Button(f1,text=label ,font="lucuda 33 bold",height=1,width=2,fg=color,relief=RAISED,bd=4)
    b.grid(row=r,column=c)
    b.bind("<Button-1>",click)

# Initialising our sign photo 
sign = Image.open("Shourya.png")
sign = sign.resize((100,35),Image.Resampling.LANCZOS)
sign = ImageTk.PhotoImage(sign)

# TODO: Main program starts from here
# f0 is the frame of the whole window
f0 = Frame(screen,padx=20,pady=15,relief=GROOVE,bd=10,bg="grey")
Label(image=sign,bg="grey").place(relx=0.08,rely=0.02,anchor=NW)

# Placing widgit that show results as entry widgit
# Value that user inputs in the entry widget is stored in entry_value
entry_value = StringVar()
entry_value.set(" ")
entry_widget = Entry(f0,font="lucuda 33",textvariable=entry_value,relief=SUNKEN,bd=7)
entry_widget.pack(pady=25)

# f1 is frame that contain all buttons
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
button("%",3,3,"orange")
button("=",3,4,"green")
f1.pack(side=TOP)
f0.pack()

screen.mainloop()