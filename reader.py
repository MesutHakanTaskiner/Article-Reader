from tkinter import *
import requests
from bs4 import BeautifulSoup
import wikipedia
import random

main_page = Tk()

main_page.title('Reader')
main_page.resizable(width = False, height = False)

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
    global random_label
    global random_window
    global random_label_2
    
    random_window = Toplevel()
    random_window.title('Random Topic')
    random_window.geometry("170x30")

    random_label = Label(random_window, text = "")
    random_label_2 = Label(random_window, text = "")

    random_button = Button(random_window, text = "Click It For Random Topic", command = lambda : random_select())
    random_button.grid(row = 0, column = 0)
    random_button.place(x = 10, y = 0)

def random_select():
    global random_label
    global random_window
    global random_label_2

    random_window.geometry("500x500")

    topic = wikipedia.random()

    random_label.grid_forget()
    random_label.destroy()

    random_label_2.grid_forget()
    random_label_2.destroy()

    random_label = Label(random_window, text = "Topic : " + topic)
    random_label.grid(row = 1, column = 0)
    random_label.place(x = 160, y = 20)

    random_label_2 = Label(random_window, text = wikipedia.summary(topic, sentences = 20), wraplength = 400)
    random_label_2.grid(row = 1, column = 0)
    random_label_2.place(x = 50, y = 50)

    exit_button = Button(random_window, text = "Exit.", command = random_window.destroy)
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

def summary():
    global mylabel
    global topic
    global root

    mylabel.grid_forget()
    mylabel.destroy()
            
    root.geometry("500x500")

    mylabel = Label(root, text = wikipedia.summary(topic.get(), sentences = 20), wraplength = 400)
    mylabel.grid(row = 1, column = 0)
    mylabel.place(x = 50, y = 50)

    exit_button = Button(root, text = "Exit.", command = root.destroy)
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

    topic.delete(0 , END)


main_page_label = Label(main_page, text = "Welcome To The My Reader")
main_page_label.grid(row = 0, column = 0)
main_page_label.config(font=("Courier", 20))

main_page_button = Button(main_page, text = "If You Want To Select Your Topic Click It", command = select)
main_page_button.grid(row = 1, column = 0, pady = 10)

main_page_button2 = Button(main_page, text = "If You Want A Random Topic Click It", command = random)
main_page_button2.grid(row = 2, column = 0, pady = 10, ipadx = 10)

exit_button = Button(main_page, text = "Exit.", command = main_page.quit)
exit_button.grid(row = 3, column = 0)

main_page.mainloop()