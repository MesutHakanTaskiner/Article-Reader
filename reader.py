from tkinter import *
import requests
from bs4 import BeautifulSoup
import wikipedia
import random
import sqlite3

main_page = Tk()

main_page.title('Reader')
main_page.resizable(width = False, height = False)

main_page.configure(background = "#92badc")

conn = sqlite3.connect('Articles_Library.db')

cursor = conn.cursor()

'''
cursor.execute("""CREATE TABLE MyLibrary (
        Topics text
)""")
'''
control = 0
mylabel = NONE
topic = NONE
mybutton = NONE
root = NONE
random_label = NONE
random_window = NONE
random_label_2 = NONE
topic_random = NONE
topics = NONE
delete_box = NONE
my_listbox = NONE

def select():
    global mylabel
    global topic
    global mybutton
    global root
    
    root = Toplevel()
    root.title('Wikipedia')
    root.geometry("350x40")
    root.configure(background = "#92badc")

    mylabel = Label(root, text = "")

    topic = Entry(root, width = 20)
    topic.grid(row = 0, column = 0, ipady = 5)
    topic.place(x = 10, y = 3)

    mybutton = Button(root, text = "Enter Your Topic", command = lambda : summary(), bg = "#bed6ea")
    mybutton.grid(row = 0, column = 1)
    mybutton.place(x = 150, y = 0)


def random():
    global random_label
    global random_window
    global random_label_2
    
    random_window = Toplevel()
    random_window.title('Random Topic')
    random_window.geometry("170x30")
    random_window.configure(background = "#92badc")

    random_label = Label(random_window, text = "")
    random_label_2 = Label(random_window, text = "")

    random_button = Button(random_window, text = "Click It For Random Topic", command = lambda : random_select(), bg = "#bed6ea")
    random_button.grid(row = 0, column = 0)
    random_button.place(x = 10, y = 0)

def random_select():
    global random_label
    global random_window
    global random_label_2
    global topic_random
    global control

    random_window.geometry("500x500")

    topic_random = wikipedia.random()

    random_label.grid_forget()
    random_label.destroy()

    random_label_2.grid_forget()
    random_label_2.destroy()

    random_label = Label(random_window, text = "Topic : " + topic_random, bg = "#5b97ca")
    random_label.grid(row = 1, column = 0)
    random_label.place(x = 160, y = 30)

    random_label_2 = Label(random_window, text = wikipedia.summary(topic_random, sentences = 20), wraplength = 400, bg = "#5b97ca")
    random_label_2.grid(row = 1, column = 0)
    random_label_2.place(x = 50, y = 50)

    exit_button = Button(random_window, text = "Exit.", command = random_window.destroy, bg = "#bed6ea")
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

    database_button = Button(random_window, text = "Add Your Library", command = database, bg = "#bed6ea")
    database_button.grid(row = 0, column = 0)
    database_button.place(x = 260, y = 0)

    control = 1

def summary():
    global mylabel
    global topic
    global root
    global control

    mylabel.grid_forget()
    mylabel.destroy()
          
    root.geometry("500x500")
 
    mylabel = Label(root, text = wikipedia.summary(topic.get(), sentences = 20), wraplength = 400, bg = "#dde9f4")
    mylabel.grid(row = 1, column = 0)
    mylabel.place(x = 50, y = 50)

    exit_button = Button(root, text = "Exit.", command = root.destroy, bg = "#bed6ea")
    exit_button.grid(row = 2, column = 0)
    exit_button.place(x = 400, y = 0)

    database_button = Button(root, text = "Add Your Library", command = database, bg = "#bed6ea")
    database_button.grid(row = 0, column = 0)
    database_button.place(x = 260, y = 0)

    control = 2

def database():
    global topic
    global topic_random
    global control
    global topics

    conn = sqlite3.connect('Articles_Library.db')

    cursor = conn.cursor()

    if control == 2:
        topics = topic.get()
    else:
        topics = topic_random
    
    cursor.execute('INSERT INTO MyLibrary VALUES (?)', (topics,))

    conn.commit()

    conn.close()

    if control == 2:
        topic.delete(0, END)

    control = 0

def library():
    global delete_box
    global my_listbox

    library = Tk()
    library.title('Your Library')
    library.configure(background = "#92badc")

    my_listbox = Listbox(library, bg="#92badc")
    my_listbox.grid(row = 0, column = 0, padx = 100, ipadx = 100)

    conn = sqlite3.connect('Articles_Library.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM MyLibrary")
    records = cursor.fetchall()

    for item in records:
        my_listbox.insert(END, str(item[0]))

    delete_button = Button(library, text = "Delete Record From Table", command = delete, bg="#92badc")
    delete_button.grid(row = 1, column = 0, padx = 100, pady = 10, ipadx = 100)

    exit = Button(library, text = "Exit", command = library.destroy, bg="#92badc")
    exit.grid(row = 2 , column = 0, pady = 20)

    conn.commit()

    conn.close()

def delete():
    conn = sqlite3.connect('Articles_Library.db')

    cursor = conn.cursor()

    query = """DELETE from MyLibrary WHERE Topics = ?"""

    cursor.execute(query, (my_listbox.get(ANCHOR),))
    
    my_listbox.delete(ANCHOR)

    conn.commit()

    conn.close()

main_page_label = Label(main_page, text = "Welcome To The My Reader", bg = "#92badc")
main_page_label.grid(row = 0, column = 0)
main_page_label.config(font=("Courier", 20))

main_page_button = Button(main_page, text = "If You Want To Select Your Topic Click It", command = select, bg = "#bed6ea")
main_page_button.grid(row = 1, column = 0, pady = 10)

main_page_button2 = Button(main_page, text = "If You Want A Random Topic Click It", command = random, bg = "#bed6ea")
main_page_button2.grid(row = 2, column = 0, pady = 10, ipadx = 10)

show_library = Button(main_page, text = "Your Library", command = library, bg = "#bed6ea")
show_library.grid(row = 3, column = 0, pady = 10, ipadx = 10)

exit_button = Button(main_page, text = "Exit.", command = main_page.quit, bg = "#bed6ea")
exit_button.grid(row = 4, column = 0)

conn.commit()

conn.close()

main_page.mainloop()