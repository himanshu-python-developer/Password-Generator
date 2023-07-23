#importing the tkinter Module
from tkinter import*

#importing the pyperclip modules to use copy generated password clipboard
import pyperclip

# Random mudules will be used generating the rondom password
import random

# initializing the tkiner
root = Tk() 

# setting the width & Height of use the GUI
root.geometry('400x400')  # x is small case hear  

#declring a variable of a string type and the variable is use
# used to stord the password 
passstr = StringVar()

# declring a variable pf a integer type which will be used to stord the lenght of password enter bye a User 
passlen = IntVar()

#Setting the length of the password zero initializing 
passlen.set(0)

#function to generate the password
def generate():
    #storing the keys in the list which will be used to generate the password
    keylist=['a', 'b','c', 'd', 'e', 'f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z'
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N'
            'O','P','Q','R','S','T','U','V','W','X','Y','Z','~','!',
            '@','#','$','%', '^','&','*','( )','?','-','=','_','+',
            '|','<','>']
    
    #initializing an empty string for storing Password
    passgen=""
    
    # loop to generate the random password the length of the enter bye the user 
    for d in range(passlen.get()):
        password = password + random.choice(passgen)
    
    #setting the password to the widget 
    passstr.set(password)
    
    #function to copy the password to the cilpboard 
    def copyclipboard():
        random_password = passstr.get()
        pyperclip.copy(random_password)
        
    #creating a text label widget
    Label(root,text="Password Gerenate Appliction" , font="caliber 20 bold ").pack
   
    #creating text label widget 
    Label(root,text="Enter Password Length").pack(pady=3)
    
    #creating a enter widget take password length enter by a user 
    Entry(root,textvariable=passlen).pack(pady=3)
    
    # button to call the copytoclipboard function
    Button(root,text="Copy to Clip Board", command=copyclipboard).pack()
    
    #mainloop() is a infinite loop use to run the appliction when It's a Ready State
    root.mainloop()