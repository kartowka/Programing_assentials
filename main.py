from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
import main_backend
from admin import Admin
from student import Student
#creating login page along with the register page.
class login:
     def __init__(self,window):

        self.window = window
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        #file.add_separator()
        file.add_command(label ='Exit', command = window.destroy)
        # Adding Edit Menu and commands
        login = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Login', menu = login)
        login.add_command(label ='Login', command = self.loginfn)
        #login.add_command(label ='Create User', command = None)
        self.frame = Frame(self.window,width=700,height=400)  #creating frame
        self.frame.pack()


     def loginfn(self):
        self.label = Label(self.frame,text='Log In',font=('Georgia',36,'bold'))

        self.name = Label(self.frame,text='Enter Username : ',font=('Arial',18,'bold'))

        self.namee_text=StringVar()
        self.namee = Entry(self.frame,textvariable=self.namee_text,width=25,font=('Arial',16,'bold'))

        self.password1 = Label(self.frame,text='Enter Password : ',font=('Arial',18,'bold'))

        self.password1e_text=StringVar()
        self.password1e = Entry(self.frame,textvariable=self.password1e_text,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

        self.buttonlogin = Button(self.frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2', command=self.login_admin)


        # placing

        self.label.place(x=40,y=40,width=200,height=80)

        self.name.place(x=100,y=140,width=240,height=60)

        self.namee.place(x=380,y=150,width=200,height=30)

        self.password1.place(x=100,y=220,width=240,height=30)

        self.password1e.place(x=380,y=215,width=200,height=30)

        self.buttonlogin.place(x=180,y=300,width=140,height=50)

        self.frame.pack()

     def login_admin(self):
        result=None
        if len(self.namee.get()) ==0:
            messagebox.showinfo("ERROR", "Mendatory Field is empty")
        elif  len(self.password1e.get()) == 0:
            messagebox.showinfo("ERROR", "Mendatory Field is empty")
        else:
            result=main_backend.check(self.namee_text.get(),self.password1e_text.get())
        if result!=None:
            # 1 - means Admin privilege
            # 2 - means Lecturer privilege
            # 3 - means Student
            #result[5] - sqlite3 create tuple - result[5]-> return check privilege
            if result[5]==1:
                self.frame.destroy()
                obj=Admin(window)
            elif result[5]==3:
                self.frame.destroy()
                obj=Student(window)
        else:
            messagebox.showinfo("ERROR","Username or Password incorrect.")


# creating the window
if __name__=="__main__":
    window = Tk()
    menubar=Menu(window)
    window.title('SCE - Search Engine')
    window.geometry('1400x600')
    window.config(menu=menubar)
    # creating object to login class
    obj = login(window)
    #obj.loginfn()
    window.mainloop()
