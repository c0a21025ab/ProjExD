import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key =""

def main_proc():
    global mx, my
    if key == "Up":my -= 1
    if key == "Down":my += 1
    if key == "Left":mx -= 1
    if key == "Right":mx += 1
    if maze_list[mx][my] == 1:
        if key == "Up":my += 1
        if key == "Down":my -= 1
        if key == "Left":mx += 1
        if key == "Right":mx -= 1
    cx , cy = mx * 100 +50 , my * 100 + 50
    print(cx,cy)
    canvas.coords("ざんねんな鳥",cx, cy)
    goal()
    root.after(100,main_proc)

def goal():
    global mx, my, maze_list, cx, cy
    if mx == 13 and my == 7:
        tkm.showinfo("goal","たどり着きました")
        #canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
        #canvas.pack()
        maze_list = mm.make_maze(15,9)
        mx, my = 1,1
        cx , cy = mx * 100 +50 , my * 100 + 50
        mm.show_maze(canvas, maze_list)
        #image = tk.PhotoImage(file="fig/3.png")
        canvas.delete("ざんねんな鳥")
        canvas.create_image(cx,cy,image=image, 
                          tag="ざんねんな鳥")
        canvas.coords("ざんねんな鳥",cx, cy)
        key = ""
        root.bind("<KeyPress>",key_down)
        root.bind("<KeyRelease>",key_up)        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_list = mm.make_maze(15,9)
    mx, my = 1,1
    cx , cy = mx * 100 +50 , my * 100 + 50
    mm.show_maze(canvas, maze_list)
    image = tk.PhotoImage(file="fig/3.png")
    canvas.create_image(cx,cy,image=image, 
                        tag="ざんねんな鳥")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()