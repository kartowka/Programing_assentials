# importing only  those functions
# which are needed
from tkinter import *
from tkinter.ttk import *
import login as lg
from login import main
# creating tkinter window
root = Tk()
root.title('SCE - Menu')
root.geometry('350x200')

# Creating Menubar
menubar = Menu(root)
def new_window():
    root=Toplevel(lg.main(lg.loginScreen))
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
login = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Login', menu = login)
login.add_command(label ='Login', command = new_window)#lg.main(root))
login.add_command(label ='Create User', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
root.config(menu = menubar)
root.mainloop()
