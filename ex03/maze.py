import tkinter as tk
import maze_maker

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
    canvas.coords("koukaton",cx, cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack()
    maze_list = maze_maker.make_maze(15,9)
    mx, my = 1,1
    cx , cy = mx * 100 +50 , my * 100 + 50
    maze_maker.show_maze(canvas, maze_list)
    image = tk.PhotoImage(file="fig/3.png")
    canvas.create_image(cx,cy,image=image, 
                        tag="koukaton")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()