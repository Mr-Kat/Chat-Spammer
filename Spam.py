import pyautogui as pa
import time
import tkinter.messagebox
from tkinter import *
win=Tk() 
win.iconbitmap('icon.ico')
win.title('Chat Spammer v.1') 
win.geometry('400x300')
win.resizable(width=0, height=0)
Label(win, text='Spam Text: ').grid(row=0)
ent1 = Entry(win) 
ent1.grid(row=0, column=1)
Label(win, text='Times: ',).grid(row=1)
ent2 = Entry(win) 
ent2.grid(row=1, column=1, pady=10)
Label(win, text='Delay:').grid(row=2)
ent3 = Entry(win) 
ent3.grid(row=2, column=1)
def msgbox():
    tkinter.messagebox.showinfo("Chat Spammer v.1","You have 5 seconds to point your cursor to text input field!")
    time.sleep(5)
    spam_count=0
    while spam_count<int(ent2.get()):
    	try:
    		delay=int(ent3.get())
    	except:
    		delay=0
    	pa.write(ent1.get())
    	pa.press('enter')
    	time.sleep(delay)
    	spam_count+=1
btn=Button(win,text="Spam", width=20,height=2,font=("Consolas 12 bold"),borderwidth=4,bg='red',command=msgbox)
btn.place(x=80,y=120)
win.mainloop()