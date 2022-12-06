import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    image = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300, 400
    canvas.create_image(cx,cy,image=image, 
                        tag="koukaton")
    canvas.pack()
    root.mainloop()