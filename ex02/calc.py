import tkinter as tk
import tkinter.messagebox as tkm
import math

root = tk.Tk()
root.title("電卓っぽいもの")
root.geometry("380x410")

entry = tk.Entry(root, width=10, font=("",40),justify="right")
entry.grid(row = 0,column=0, columnspan = 3)


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    try:
        if txt == "=":
            siki = entry.get()
            ans = eval(siki)
            entry.delete(0,tk.END)
            entry.insert(tk.END,ans)
        elif txt == "C":
            mozi = len(entry.get())-1
            entry.delete(mozi,tk.END)
        elif txt == "AC":
            entry.delete(0,tk.END)
        elif txt == "1000+":
            p = entry.get()
            pa = eval(p)
            pb = pa
            while pb // 1000 == 0:
                pb += pa
            entry.delete(0,tk.END)
            entry.insert(tk.END,pb)

        else:
            entry.insert(tk.END,txt)
    except:
        entry.delete(0,tk.end)
        entry.insert(tk.END,"Error")

num_list=[n for n in range(10)]

for num in num_list:
    button = tk.Button(root,text=str(num), 
                    font=("",30),
                    width=4,height=1)
    button.bind("<1>", button_click)
    if num % 3 == 0:
        button.grid(row = 4 - math.ceil(num/3), column = 0)
    elif num % 3 == 1:
        button.grid(row = 4 - math.ceil(num/3), column = 2)
    elif num % 3 == 2:
        button.grid(row = 4 - math.ceil(num/3), column = 1)

button = tk.Button(root, text ="+",font = ("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>", button_click)
button.grid(row = 1, column = 3)

button = tk.Button(root, text="=", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>", button_click)
button.grid(row = 4, column = 2)

button = tk.Button(root, text="-", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>", button_click)
button.grid(row = 2, column = 3)

button = tk.Button(root, text="*", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>", button_click)
button.grid(row = 3, column = 3)

button = tk.Button(root, text="/", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>", button_click)
button.grid(row = 4, column = 3)

button = tk.Button(root, text="00", font=("",30),width = 4,height = 1)
button.bind("<1>",button_click)
button.grid(row = 4, column = 1)

button = tk.Button(root, text="AC", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>",button_click)
button.grid(row = 5, column = 0)

button = tk.Button(root, text="C", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>",button_click)
button.grid(row = 5, column = 1)

button = tk.Button(root, text="**", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>",button_click)
button.grid(row = 5, column = 2)

button = tk.Button(root, text="1000+", font=("",30),width = 4,height = 1,bg="#a9a9a9")
button.bind("<1>",button_click)
button.grid(row = 5, column = 3)

root.mainloop()

