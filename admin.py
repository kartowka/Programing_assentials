from tkinter import *
import backend
from ParliamentaryQuestion import main

class Admin():
    def __init__(self,window):
        self.window=window
        menubar=Menu(window)
        window.config(menu=menubar)
        self.frame=Frame(self.window,width=800,height=450)
        self.frame.pack()
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        file.add_command(label="ParliamentaryQuestion", command= lambda:main(window) )
        #file.add_separator()
        file.add_command(label ='Exit', command = window.destroy)


        self.Label=Label(self.frame,text="Admin user",font=('Georgia',30,'bold')).place(x=150,y=20,width=400,height=50)
        self.label_first = Label(self.frame, text='First Name: ',font=('Georgia',14,'bold')).place(x=0,y=100,width=120,height=30)
        self.label_last = Label(self.frame, text='Last Name: ',font=('Georgia',14,'bold')).place(x=0,y=150,width=120,height=30)
        self.label_username = Label(self.frame, text='Username: ',font=('Georgia',14,'bold')).place(x=350,y=100,width=120,height=30)
        self.label_password = Label(self.frame, text='Password: ',font=('Georgia',14,'bold')).place(x=350,y=150,width=120,height=30)

        self.first_text=StringVar()
        self.entry_first = Entry(self.frame, fg='gray',textvariable=self.first_text,width=25,font=('Arial',12,'bold'))
        self.entry_first.place(x=120,y=100,width=150,height=30)

        self.last_text=StringVar()
        self.entry_last = Entry(self.frame, fg='gray',textvariable=self.last_text,width=25,font=('Arial',12,'bold'))
        self.entry_last.place(x=120,y=150,width=150,height=30)

        self.username_text=StringVar()
        self.entry_username = Entry(self.frame, fg='gray',textvariable=self.username_text,width=25,font=('Arial',12,'bold'))
        self.entry_username.place(x=470,y=100,width=150,height=30)

        self.password_text=StringVar()
        self.entry_password = Entry(self.frame, fg='gray',textvariable=self.password_text,width=25,font=('Arial',12,'bold'),show='*')
        self.entry_password.place(x=470,y=150,width=150,height=30)

        self.var=IntVar()
        Radiobutton(self.frame,text="Admin",variable=self.var,value=1,font=('Georgia',14,'bold')).place(x=100,y=200)
        Radiobutton(self.frame,text="Lecturer",variable=self.var,value=2,font=('Georgia',14,'bold')).place(x=230,y=200)
        Radiobutton(self.frame,text="Student",variable=self.var,value=3,font=('Georgia',14,'bold')).place(x=380,y=200)

        self.listbox = Listbox(self.frame)
        self.listbox.place(x=100,y=240,width=500,height=100)

        self.button_view = Button(self.frame,text='View users', command=self.view_command)
        self.button_view.place(x=100,y=320,width=100,height=40)

        self.button_search = Button(self.frame,text='Search ', command=self.search_command)
        self.button_search.place(x=200,y=320,width=100,height=40)

        self.button_add = Button(self.frame,text='Add user', command=self.add_command)
        self.button_add.place(x=300,y=320,width=100,height=40)

        self.button_update = Button(self.frame, text='Update entry', command=self.update_command)
        self.button_update.place(x=400, y=320,width=100,height=40)

        self.button_delete = Button(self.frame, text='Delete entry', command=self.delete_command)
        self.button_delete.place(x=500, y=320,width=100,height=40)

        self.button_issue = Button(self.frame, text='Clear Fields', command=self.clear_command)
        self.button_issue.place(x=100, y=360,width=100,height=40)

    def clear_command(self):
        self.entry_first.delete(0,END)
        self.entry_last.delete(0,END)
        self.entry_username.delete(0,END)
        self.entry_password.delete(0,END)

    def view_command(self):
        self.listbox.delete(0,END)
        for row in backend.view():
            self.listbox.insert(END,row) # END ensures that every new entry is stored at end of the all rows


    def search_command(self):
        self.listbox.delete(0,END)
        for row in backend.search(self.first_text.get(),self.last_text.get(),self.username_text.get()):
            self.listbox.insert(END,row)


    def add_command(self):
        backend.insert(self.first_text.get(),self.last_text.get(),self.username_text.get(),self.password_text.get(),self.var.get())
        self.listbox.delete(0,END)
        self.listbox.insert(END,(self.first_text.get(),self.last_text.get(),self.username_text.get(),self.password_text.get(),self.var.get()))


    def delete_command(self):
        selected_tuple=self.listbox.curselection()
        value = self.listbox.get(selected_tuple)
        backend.delete(value[0])    # i have to use value[0] here or at backend use id[0]
        self.entry_first.delete(0,END)
        self.entry_first.insert(END,value[1])
        self.entry_last.delete(0,END)
        self.entry_last.insert(END,value[3])
        self.entry_username.delete(0,END)
        self.entry_username.insert(END,value[2])
        self.entry_password.delete(0,END)
        self.entry_password.insert(END,value[4])


    def update_command(self):
        selected_tuple=self.listbox.curselection()
        value = self.listbox.get(selected_tuple)
        self.entry_first.delete(0,END)
        self.entry_first.insert(END,value[0])
        self.entry_last.delete(0,END)
        self.entry_last.insert(END,value[2])
        self.entry_username.delete(0,END)
        self.entry_username.insert(END,value[1])
        self.entry_password.delete(0,END)
        self.entry_password.insert(END,value[3])
        backend.update(value[0],self.first_text.get(),self.last_text.get(),self.username_text.get(),self.password_text.get(),self.var.get())

#window=Tk()
#obj=Admin(window)
#window.mainloop()
