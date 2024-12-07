from sys import exit
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()

class Position:
    def __init__(self, obstacle):
        self.obstacle = obstacle
        self.visited = False
    def __str__(self):
        if self.obstacle:
            return "#"
        if self.visited:
            return "X"
        return "."

    def copy(self):
        return Position(self.obstacle)

def load_input(filename):
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    xformed = []

    for x, line in enumerate(lines):
        xline = []
        xformed.append(xline)
        for y, v in enumerate(line):
          xline.append(Position(v == "#"))
          if v == "^":
              start_position = y,x

    grid = utils.Grid(xformed)


    return grid, start_position
    

direction_rotation = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def solution_1(grid, position):
    x, y = position
    direction = 0
    dx, dy = direction_rotation[direction]
    while grid.get(x, y):
        grid.get(x,y).visited = True
        while grid.get(x+dx, y+dy) and grid.get(x+dx, y+dy).obstacle:
            direction+=1
            dx, dy = direction_rotation[direction%4]
        x += dx
        y += dy

    return sum(p.visited for p in grid)

def solve_grid_detect_loop(grid, x, y, direction):
    dx, dy = direction_rotation[direction%4]
    visited_positions = set()
    while grid.get(x, y):
        if (x,y,dx,dy) in visited_positions:
            return False
        visited_positions.add((x,y,dx,dy))
        while grid.get(x+dx, y+dy) and grid.get(x+dx, y+dy).obstacle:
            direction+=1
            dx, dy = direction_rotation[direction%4]
        x += dx
        y += dy
    return True

def solution_2(grid, start_position):
    x,y = start_position
    direction = 0
    dx, dy = direction_rotation[direction]
    obstruction_positions = set()
    while grid.get(x, y):
        while grid.get(x+dx, y+dy) and grid.get(x+dx, y+dy).obstacle:
            direction+=1
            dx, dy = direction_rotation[direction%4]
        
        cpy = grid.copy()
        if cpy.get(x+dx, y+dy):
            cpy.get(x+dx, y+dy).obstacle = True
            if not solve_grid_detect_loop(cpy,x,y,direction):
                obstruction_positions.add((x+dx, y+dy))
        x += dx
        y += dy
    return len(obstruction_positions)


def main():
    grid, start = load_input("input.txt")
    print(f"{solution_1(grid, start)=}")
    print(f"{solution_2(grid, start)=}")
    return 0

if __name__ == "__main__":
    exit(main())