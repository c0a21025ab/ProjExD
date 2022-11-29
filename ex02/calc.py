import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓っぽいな")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo("効果",f"{txt}のボタンがクリックされました")

button_1 = tk.Button(root,text="1", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_1.bind("<1>",button_click)
button_1.grid(row=2,column=2)

button_2 = tk.Button(root,text="2", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_2.bind("<1>",button_click)
button_2.grid(row=2,column=1)

button_3 = tk.Button(root,text="3", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_3.bind("<1>",button_click)
button_3.grid(row=2,column=0)

button_4 = tk.Button(root,text="4", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_4.bind("<1>",button_click)
button_4.grid(row=1,column=2)

button_5 = tk.Button(root,text="5", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_5.bind("<1>",button_click)
button_5.grid(row=1,column=1)

button_6 = tk.Button(root,text="6", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_6.bind("<1>",button_click)
button_6.grid(row=1,column=0)

button_7 = tk.Button(root,text="7", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_7.bind("<1>",button_click)
button_7.grid(row=0,column=2)

button_8 = tk.Button(root,text="8", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_8.bind("<1>",button_click)
button_8.grid(row=0,column=1)

button_9 = tk.Button(root,text="9", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_9.bind("<1>",button_click)
button_9.grid(row=0,column=0)

button_0 = tk.Button(root,text="0", 
                    font=("",30),
                    width=4,height=2,
                    command=button_click
                )
button_0.bind("<1>",button_click)
button_0.grid(row=3,column=0)



root.mainloop()

