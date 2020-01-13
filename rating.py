from tkinter import *
from tkinter import Radiobutton,IntVar
import searchdatabase
import logging

logging.basicConfig(filename="log.log",filemode='a+',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logger.info("Rating.py run as expected.")


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
        numberOfRates=searchdatabase.getNumberOfRaters(self.var[0])
        self.average(numberOfRates)
        searchdatabase.updateRating(self.var[0],self.v[0],self.v[1],self.v[2],self.v[3],self.v[4],self.v[5],self.v[6],self.v[7],
        self.v[8],self.v[9])
        self.root.destroy()

    def average(self,numOfRates):
        for i in range(10):
            temp=self.v[i].get()
            self.v[i]=((temp+numOfRates[0][i+1])/(numOfRates[0][11]+1))
