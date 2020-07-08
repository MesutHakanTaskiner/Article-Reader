from tkinter import *
import requests
from bs4 import BeautifulSoup
import wikipedia

main_page = Tk()
root = Tk()

root.title('Wikipedia')
root.geometry("350x40")

mylabel = Label(root, text = "")

def summary():
    global mylabel

    mylabel.grid_forget()
    mylabel.destroy()
    
    topic.get()
    #r = requests.get("https://tr.wikipedia.org/wiki/" + topic.get() + "")
    
    root.geometry("500x500")
    mylabel = Label(root, text = wikipedia.summary(topic.get(), sentences = 20), wraplength = 400)
    mylabel.grid(row = 1, column = 0)
    mylabel.place(x = 50, y = 50)

    topic.delete(0 , END)

#r = requests.get("https://tr.wikipedia.org/wiki/Google")

#soup = BeautifulSoup(r.content, "html.parser")

main_page_label = Label(main_page, text = "Welcome To The Our Reader")
main_page_label.grid(row = 0, column = 0)

main_page_button = Button(main_page, text = "If You Want To Select Your Topic Click It")
main_page_button.grid(row = 1, column = 0, pady = 10)

main_page_button2 = Button(main_page, text = "If You Want A Random Topic Click It")
main_page_button2.grid(row = 2, column = 0, pady = 10, ipadx = 10)

topic = Entry(root, width = 20)
topic.grid(row = 0, column = 0, ipady = 5)
topic.place(x = 0, y = 3)

mybutton = Button(root, text = "Enter your topic what dou you want to read", command = summary)
mybutton.grid(row = 0, column = 1)
mybutton.place(x = 100, y = 0)


root.mainloop()