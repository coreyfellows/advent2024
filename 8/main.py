from sys import exit
from collections import namedtuple
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()

class Position:
    def __init__(self, value):
        self.visited = False
        if value == ".":
            self.value = None
            return
        self.value = value
        
    def __str__(self):
        if self.value:
            return self.value
        if self.antinode:
            return "#"
        return "."
        
def load_input(filename):
    with open(filename, "r") as f:
        return utils.Grid(f, Position)
    
def solution_1(grid):
    antinodes = set()
    for pos, x ,y in grid:
        if pos.visited:
            continue
        if not (value := pos.value):
            continue
        pos.visited = True
        for pos2, x2, y2 in grid:
            if pos2.value != value or pos2.visited:
                continue
            dx, dy = x-x2, y-y2
            if grid.get(x+dx, y+dy):
                antinodes.add((x,y))
            if grid.get(x2-dx, y2-dy):
                antinodes.add((x2,y2))
    return len(antinodes)


def solution_2(grid):
    antinodes = set()
    for pos, x ,y in grid:
        if pos.visited:
            continue
        if not (value := pos.value):
            continue
        pos.visited = True
        for pos2, x2, y2 in grid:
            x1,y1 = x,y
            if pos2.value != value or pos2.visited:
                continue
            dx, dy = x1-x2, y1-y2
            while grid.get(x1, y1):
                antinodes.add((x1,y1))
                x1+=dx
                y1+=dy
            while grid.get(x2, y2):
                antinodes.add((x2,y2))
                x2-=dx
                y2-=dy
    return len(antinodes)        

def main():
    grid = load_input("input.txt")
    print(f"{solution_1(grid)=}")
    grid = load_input("input.txt")
    print(f"{solution_2(grid)=}")
    return 0

if __name__ == "__main__":
    exit(main())