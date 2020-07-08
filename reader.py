from tkinter import *
import requests
from bs4 import BeautifulSoup
import wikipedia
import random

main_page = Tk()

main_page.title('Reader')


def select():
    global mylabel
    global topic
    global mybutton
    global root
    
    root = Toplevel()
    root.title('Wikipedia')
    root.geometry("350x40")


    mylabel = Label(root, text = "")


    topic = Entry(root, width = 20)
    topic.grid(row = 0, column = 0, ipady = 5)
    topic.place(x = 0, y = 3)

    mybutton = Button(root, text = "Enter your topic what dou you want to read", command = lambda : summary())
    mybutton.grid(row = 0, column = 1)
    mybutton.place(x = 100, y = 0)


def random():
    global mylabel
    global mybutton
    global random_window
    
    random_window = Toplevel()
    random_window.title('Random Topic')

    mylabel = Label(random_window, text = "")

    random_button = Button(random_window, text = "Click It For Random Topic", command = lambda : random_select())
    random_button.grid(row = 0, column = 0)
    random_button.place(x = 10, y = 0)

def random_select():
    global mylabel
    global random_window

    #mylabel = Label(random_window, text = wikipedia.summary(, sentences = 20), wraplength = 400)
    #mylabel.grid(row = 1, column = 0)
    #mylabel.place(x = 50, y = 50)

    exit_button = Button(random_window, text = "Exit.", command = random_window.destroy)
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

def summary():
    global mylabel
    global topic
    global root

    mylabel.grid_forget()#
    mylabel.destroy()
            
    topic.get()
    #r = requests.get("https://tr.wikipedia.org/wiki/" + topic.get() + "")
            
    root.geometry("500x500")

    mylabel = Label(root, text = wikipedia.summary(topic.get(), sentences = 20), wraplength = 400)
    mylabel.grid(row = 1, column = 0)
    mylabel.place(x = 50, y = 50)

    exit_button = Button(root, text = "Exit.", command = root.destroy)
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

    topic.delete(0 , END)

    

#r = requests.get("https://tr.wikipedia.org/wiki/Google")

#soup = BeautifulSoup(r.content, "html.parser")

main_page_label = Label(main_page, text = "Welcome To The My Reader")
main_page_label.grid(row = 0, column = 0)
main_page_label.config(font=("Courier", 20))

main_page_button = Button(main_page, text = "If You Want To Select Your Topic Click It", command = select)
main_page_button.grid(row = 1, column = 0, pady = 10)

main_page_button2 = Button(main_page, text = "If You Want A Random Topic Click It", command = random)
main_page_button2.grid(row = 2, column = 0, pady = 10, ipadx = 10)


main_page.mainloop()