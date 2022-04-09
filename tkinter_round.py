import tkinter as tk
from math import cos, sin, radians

root = tk.Tk()

root.title('Round_move_complete')


canvas = tk.Canvas(root, width=600, height=600, bg='black')
canvas.pack()

# image = tk.PhotoImage(file="plane.png")
# image = image.subsample(1, 1)
dot = canvas.create_oval(0, 0, 0, 0, fill='red')
s = 10  # speed
clockwise = False  # True - по часовой, False - против часовой


def create_circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline='purple')


def move(angle):
    global s, clockwise
    if angle >= 360:
        angle = 0
    if clockwise:
        x = 100 * cos(radians(angle))
        y = 100 * sin(radians(angle))
    else:
        y = 100 * cos(radians(angle))
        x = 100 * sin(radians(angle))
    angle += 1
    canvas.coords(dot, 295 + x, 295 + y, 305 + x, 305 + y)
    root.after(s, move, angle)


create_circle(300, 300, 100, canvas)
root.after(0, move, 0)

root.mainloop()
