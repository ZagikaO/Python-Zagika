import random
from tkinter import *


class My15:
    def __init__(self, size):
        self.my_15 = self._generate_15()
        self._row, self._col = self._get_space()
        self._size = size

    def _generate_15(self):
        my_15 = []
        all_values = [str(i) for i in range(1, size*size)] + [""]
        random.shuffle(all_values)
        for row_number in range(size):
            my_15.append(all_values[size * row_number: size * (row_number + 1)])
        return my_15

    def _print_15(self):
        for row in self.my_15:
            line = " ".join([f"{val:2}" for val in row])
            print(line)

    def _get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self.my_15):
            if '' in row:
                row_ = i
                for j, col in enumerate(row):
                    if '' == col:
                        col_ = j
        return row_, col_

    def move_down(self):
        if self._row == size - 1:
            return
        self.my_15[self._row][self._col], self.my_15[self._row + 1][self._col] = self.my_15[self._row + 1][self._col], self.my_15[self._row][self._col]
        self._row += 1

    def move_up(self):
        if self._row == 0:
            return
        self.my_15[self._row][self._col], self.my_15[self._row - 1][self._col] = self.my_15[self._row - 1][self._col], self.my_15[self._row][self._col]
        self._row -= 1

    def move_right(self):
        if self._col == size - 1:
            return
        self.my_15[self._row][self._col], self.my_15[self._row][self._col + 1] = self.my_15[self._row][self._col + 1], self.my_15[self._row][self._col]
        self._col += 1

    def move_left(self):
        if self._col == 0:
            return
        self.my_15[self._row][self._col], self.my_15[self._row][self._col - 1] = self.my_15[self._row][self._col - 1], self.my_15[self._row][self._col]
        self._col -= 1


def draw_15_table(my_15):
    for row_index, row in enumerate(my_15.my_15):
        for col_index, col in enumerate(row):
            label = Entry(root, width=2, fg='white', bg='black', font=('Arial', 50, 'bold'), justify='center')
            label.config(highlightbackground="black")
            label.grid(row=row_index, column=col_index)
            label.insert(END, col)


def left(event):
    my_15.move_left()
    draw_15_table(my_15)


def right(event):
    my_15.move_right()
    draw_15_table(my_15)


def up(event):
    my_15.move_up()
    draw_15_table(my_15)


def down(event):
    my_15.move_down()
    draw_15_table(my_15)


size = 6
assert size <= 10, "size not in limit"
assert size >= 4, "size not in limit"

my_15 = My15(size=size)
root = Tk()
root.title("15")
root.geometry(f"{70*size}x{70*size}")
root.configure(background='black')
draw_15_table(my_15)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()