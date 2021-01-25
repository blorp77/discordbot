# minesweeper.py
import random

class Minesweeper:

    def __init__(self):
        self.grid = {}

    def new_game(self, width, height, mines):
        self.grid = [[0 for i in range(width)] for i in range(height)]

        for i in range(mines):
            self.add_mine(width, height)

    def add_mine(self, width, height):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if self.grid[x][y] >= 9:
            self.add_mine(width, height)
        else:
            self.increment_grid(x, y, 9)
            self.increment_grid(x-1, y-1, 1)
            self.increment_grid(x-1, y, 1)
            self.increment_grid(x-1, y+1, 1)
            self.increment_grid(x, y-1, 1)
            self.increment_grid(x, y+1, 1)
            self.increment_grid(x+1, y-1, 1)
            self.increment_grid(x+1, y, 1)
            self.increment_grid(x+1, y+1, 1)

    def increment_grid(self, x, y, n):
        if x < 0 or y < 0:
            return
        try:
            self.grid[x][y] += n
        except IndexError:
            return

    def print_to_discord(self):
        text = ""
        for row in self.grid:
            for col in row:
                text += self.encode_for_discord(col)
            text += "\r\n"
        return text

    def encode_for_discord(self, n):
        if n == 0:
            return "||:white_large_square:||"
        if n == 1:
            return "||:one:||"
        if n == 2:
            return "||:two:||"
        if n == 3:
            return "||:three:||"
        if n == 4:
            return "||:four:||"
        if n == 5:
            return "||:five:||"
        if n == 6:
            return "||:six:||"
        if n == 7:
            return "||:seven:||"
        if n == 8:
            return "||:eight:||"
        if n >= 9:
            return "||:boom:||"


if __name__ == "__main__":
    mine = Minesweeper()
    mine.new_game(8, 8, 10)
    for i in mine.grid:
        print(i)
    print(mine.print_to_discord())
