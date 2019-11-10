from tkinter import *

expression=""


def perform():
    try:
        global expression
        result=str(eval(expression))
        equation.set(result)
        expression=""
    except:
        equation.set("error")
        expression=""


def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
def ac():
    global  expression
    equation.set('')
    expression=""


if __name__ == "__main__":
    root=Tk()
    root.configure(background='black')
    equation = StringVar()
    root.title("Calculator")
    #tkinter.messagebox.showinfo('Calculator')
    a=Entry(root,justify=RIGHT,bd=2,relief=SUNKEN,textvariable=equation)
    a.place(y=10,relx=0.05,relwidth=0.9,relheight=0.15)


    num1=Button(root, text="1", activebackground='#96b9f2', bg='white', relief=GROOVE, command=lambda:press(1) )
    num2=Button(root,text="2",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(2))
    num3=Button(root,text="3",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(3))
    num4=Button(root,text="4",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(4))
    num5=Button(root,text="5",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(5))
    num6=Button(root,text="6",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(6))
    num7=Button(root,text="7",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(7))
    num8=Button(root,text="8",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(8))
    num9=Button(root,text="9",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(9))
    num0=Button(root,text="0",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(0))

    num9.place(relx=0.05,rely=0.25,relheight=0.12,relwidth=0.15)
    num8.place(relx=0.2375,rely=0.25,relheight=0.12,relwidth=0.15)
    num7.place(relx=0.425,rely=0.25,relheight=0.12,relwidth=0.15)
    num6.place(relx=0.05,rely=0.4075,relheight=0.12,relwidth=0.15)
    num5.place(relx=0.2375,rely=0.4075,relheight=0.12,relwidth=0.15)
    num4.place(relx=0.425,rely=0.4075,relheight=0.12,relwidth=0.15)
    num3.place(relx=0.05,rely=0.565,relheight=0.12,relwidth=0.15)
    num2.place(relx=0.2375,rely=0.565,relheight=0.12,relwidth=0.15)
    num1.place(relx=0.425,rely=0.565,relheight=0.12,relwidth=0.15)
    num0.place(relx=0.2375,rely=0.7225,relheight=0.12,relwidth=0.15)


    butadd=Button(root,text="+",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('+'))
    butsub=Button(root,text="-",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('-'))
    butmul=Button(root,text="x",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('*'))
    butdiv=Button(root,text="/",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('/'))

    butadd.place(relx=0.6125,rely=0.25,relheight=0.12,relwidth=0.15)
    butsub.place(relx=0.6125,rely=0.4075,relheight=0.12,relwidth=0.15)
    butmul.place(relx=0.6125,rely=0.565,relheight=0.12,relwidth=0.15)
    butdiv.place(relx=0.6125,rely=0.7225,relheight=0.12,relwidth=0.15)


    q=Button(root,text="=",activebackground='#96b9f2',bg='white',relief=GROOVE,command=perform)
    q.place(relx=0.425,rely=0.7225,relheight=0.12,relwidth=0.15)


    butac=Button(root,text="AC",activebackground='#96b9f2',bg='white',relief=GROOVE,command=ac)
    butac.place(relx=0.05,rely=0.7225,relheight=0.12,relwidth=0.15)

    butbra1=Button(root,text="(",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('('))
    butbra2=Button(root,text=")",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press(')'))
    butmod=Button(root,text="%",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('%'))
    butexp=Button(root,text="exp",activebackground='#96b9f2',bg='white',relief=GROOVE,command=lambda:press('^'))

    butbra1.place(relx=0.8,rely=0.25,relheight=0.12,relwidth=0.15)
    butbra2.place(relx=0.8,rely=0.4075,relheight=0.12,relwidth=0.15)
    butmod.place(relx=0.8,rely=0.565,relheight=0.12,relwidth=0.15)
    butexp.place(relx=0.8,rely=0.7225,relheight=0.12,relwidth=0.15)



    root.mainloop()