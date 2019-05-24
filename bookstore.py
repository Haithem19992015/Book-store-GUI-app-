# Program iformation
"""
A program that stores this book information:
Title, Author
Year, ISBN

User can: 

View all records
Search an entry
Add an entry 
Update an entry 
Delete 
Close

"""
# The program 

from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
    
def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
        
def search_command():
    list1.delete(0,END) 
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command(): 
    if title_text.get() != '' and author_text.get()!= ''and year_text.get()!= ''and isbn_text.get()!= '':       
        backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    else: 
        pass        
    list1.delete(0,END)
    if title_text.get() != '' and author_text.get()!= ''and year_text.get()!= ''and isbn_text.get()!= '': 
        list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    else:
        pass 


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
window = Tk()

window.wm_title('Book Store')

# Labels
l1 = Label(window,text='Title')
l1.grid(row=0,column=0)
l2 = Label(window,text ='Year')
l2.grid(row=1,column=0)
l3 = Label(window,text='Author')
l3.grid(row=0,column=2)
l4 = Label(window,text = 'ISBN')
l4.grid(row=1,column=2)
# Entries 
title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

year_text = StringVar()
e2 = Entry(window,textvariable=year_text)
e2.grid(row=1,column=1)

author_text = StringVar()
e3 = Entry(window,textvariable=author_text)
e3.grid(row=0,column=3)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)
# ListBox
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

# Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

sb2 = Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=7,column=0,columnspan=3)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)
# Buttons
b1 = Button(window,text='View all',borderwidth=4,width=13,background='#d1d8e0',command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text='Search entry ',borderwidth=4,width=13,background='#d1d8e0',command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text='Add entry',borderwidth=4,width=13,background='#d1d8e0',command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text='Update selected',borderwidth=4,width=13,background='#d1d8e0',command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text='Delete selected',borderwidth=4,width=13,background='#d1d8e0',command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text='close',borderwidth=4,width=13,background='#d1d8e0',command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()