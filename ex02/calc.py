import tkinter as tk
import tkinter.messagebox as tkm
import math

root = tk.Tk()
root.title("電卓っぽいな")
root.geometry("280x500")

entry = tk.Entry(root, width=10, font=("",40),justify="right")
entry.grid(row = 0,column=0, columnspan = 3)


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        siki = entry.get()
        ans = eval(siki)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,txt)
    tkm.showinfo("効果",f"{txt}のボタンがクリックされました")

num_list=[n for n in range(10)]

for num in num_list:
    button = tk.Button(root,text=str(num), 
                    font=("",30),
                    width=4,height=2)
    button.bind("<1>", button_click)
    if num % 3 == 0:
        button.grid(row = 4 - math.ceil(num/3), column = 0)
    elif num % 3 == 1:
        button.grid(row = 4 - math.ceil(num/3), column = 2)
    elif num % 3 == 2:
        button.grid(row = 4 - math.ceil(num/3), column = 1)

button = tk.Button(root, text ="+",font = ("",30),width = 4,height = 2)
button.bind("<1>", button_click)
button.grid(row = 4, column = 1)

button = tk.Button(root, text="=", font=("",30),width = 4,height = 2)
button.bind("<1>", button_click)
button.grid(row = 4, column = 2)
root.mainloop()

