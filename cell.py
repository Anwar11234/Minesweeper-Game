from tkinter import Button , Label
import random
import settings
import ctypes

LEFT_CLICK = '<Button-1>'
RIGHT_CLICK = '<Button-3>'
DEFAULT_BUTTON_BG = 'SystemButtonFace'
class Cell:
    all = []
    cell_count_label = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x , y , is_mine=False):
        self.x = x 
        self.y = y
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn = None
        Cell.all.append(self)

    def create_btn(self , location):
        btn = Button(
          location , 
          width=12,
          height=4
        )
        btn.bind(LEFT_CLICK , self.left_click_actions)
        btn.bind(RIGHT_CLICK , self.right_click_actions)
        self.cell_btn = btn
    
    @classmethod
    def create_cell_count_label(cls , location):
        lbl = Label(
            location ,
            bg="black",
            fg="white",
            font=("Helvetica",30),
            text=f"Cells Left: {Cell.cell_count}")
        cls.cell_count_label = lbl

    def left_click_actions(self , event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mines_count == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0 , "You Won!!!" , "Game Over" , 0)

        self.cell_btn.unbind(LEFT_CLICK)
        self.cell_btn.unbind(RIGHT_CLICK)
    
    def show_mine(self):
        self.cell_btn.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0 , "You clicked on a mine" , "Game Over" , 0)
        exit()
    
    def get_cell_by_coordinates(self , x , y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_coordinates(self.x - 1, self.y -1),
            self.get_cell_by_coordinates(self.x - 1, self.y),
            self.get_cell_by_coordinates(self.x - 1, self.y + 1),
            self.get_cell_by_coordinates(self.x, self.y - 1),
            self.get_cell_by_coordinates(self.x + 1, self.y - 1),
            self.get_cell_by_coordinates(self.x + 1, self.y),
            self.get_cell_by_coordinates(self.x + 1, self.y + 1),
            self.get_cell_by_coordinates(self.x, self.y + 1)
        ]
        return [cell for cell in cells if cell is not None]
    
    @property
    def surrounding_mines_count(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn.configure(text=f"{self.surrounding_mines_count}")
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(text=f"Cells Left: {Cell.cell_count}")
            self.cell_btn.configure(bg=DEFAULT_BUTTON_BG)
            self.is_opened = True

    def right_click_actions(self , event):
        if not self.is_mine_candidate:
            self.cell_btn.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn.configure(bg=DEFAULT_BUTTON_BG)
            self.is_mine_candidate = False
    
    @staticmethod
    def randomize_mines():
        mine_cells = random.sample(Cell.all , settings.MINES_COUNT)
        for cell in mine_cells:
            cell.is_mine = True
        
    def __repr__(self):
        return f"Cell({self.x} , {self.y})"