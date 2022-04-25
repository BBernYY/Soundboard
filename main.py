from playsound import playsound
from os import path, listdir
from tkinter import *
tk = Tk()
tk.title("Soundboard")
main_text = Label(tk, text="Beter soundboard")
btns = []
for i in range(len(listdir("audio"))):
    btns.append(Button(tk, text=listdir("audio")[i], command=lambda c=i: playsound('audio\\'+listdir("audio")[c])))
    btns[i].pack()
tk.mainloop()