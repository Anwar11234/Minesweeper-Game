from tkinter import *
import settings
import utils
from cell import Cell
 
root = Tk()
root.configure(bg="black")
root.title("Minesweeper")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False , False)

top_frame = Frame(
    root , 
    bg="black",
    width=settings.WIDTH,
    height=utils.height_percentage(25)             
)
top_frame.place(x=0,y=0)

game_title = Label(
    top_frame , 
    text='Minesweeper Game',
    bg="black",
    fg="white",
      font=("Helvetica",48)
)
game_title.place(x=utils.width_percentage(25) , y=10)
left_frame = Frame(
    root , 
    bg="black",
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)             
)
left_frame.place(x=0,y=utils.height_percentage(25))

center_frame = Frame(
    root , 
    bg = "black",
    width=utils.width_percentage(75),
    height=utils.height_percentage(75)
)
center_frame.place(x=utils.width_percentage(25) , y=utils.height_percentage(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x , y)
        c.create_btn(center_frame)
        c.cell_btn.grid(row=y,column=x)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=10,y=200)
Cell.randomize_mines()

root.mainloop()