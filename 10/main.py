from sys import exit
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()
       
def load_input(filename):
    with open(filename, "r") as f:
        grid = utils.Grid(f, int)
    return grid

def traverse(grid: utils.Grid, x: int, y: int, peaks: list=None):
    if peaks is None:
        peaks = []
    level = grid.get(x,y)
    if level == 9:
        peaks.append((x,y))
        return
    for _, next_x, next_y in filter(lambda cell: cell[0] == level+1, grid.cardinal_neighbors(x,y)):
        traverse(grid, next_x, next_y, peaks)
    return peaks

def solution_1(grid):
    total = 0
    for level, x, y in grid:
        if level == 0:
            peaks = traverse(grid, x, y)
            total += len(set(peaks))
    return total

def solution_2(grid):
    total = 0
    for level, x, y in grid:
        if level == 0:
            peaks = traverse(grid, x, y)
            total += len(peaks)
    return total

def main():
    grid = load_input("input.txt")
    print(f"{solution_1(grid)=}")
    print(f"{solution_2(grid)=}")
    return 0

if __name__ == "__main__":
    exit(main())