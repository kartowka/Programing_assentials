from tkinter import *
from tkinter import Radiobutton,IntVar
import searchdatabase

class Rating():
    def __init__(self, root,val):
        self.root = root
        self.root=Toplevel()
        self.root.title("Question Rating")
        self.root.geometry('700x500')
        self.var=val
        self.number = int(val[3])
        self.radiobuttons = [[0 for x in range(5)] for y in range(self.number)]
        self.buttons = []
        self.radiobutton=[]
        self.v=[IntVar() for x in range(10)]
        self.languages = [1,2,3,4,5]
        j=0
        q=0
        for i in range(self.number):
            q=0
            self.buttons.append(Label(self.root, text="Question No. "+str(i+1)+":"))#, command=lambda c=i: self.command(c)))
            self.buttons[i].place(x=0,y=0+j)
            for k in range(5):
                self.radiobuttons[i][k]=(Radiobutton(self.root,text=self.languages[k],variable=self.v[i],padx=20,value=self.languages[k]))
                self.radiobuttons[i][k].place(x=140+q,y=0+j)
                q=q+100
            j=j+30

        self.submit=Button(self.root,text="submit",command=self.sub)
        self.submit.place(x=0,y=400)
    def sub(self):
        searchdatabase.updateRating(self.var[0],self.v[0].get(),self.v[1].get(),self.v[2].get(),self.v[3].get(),self.v[4].get(),self.v[5].get(),self.v[6].get(),self.v[7].get(),
        self.v[8].get(),self.v[9].get())
        self.root.destroy()
