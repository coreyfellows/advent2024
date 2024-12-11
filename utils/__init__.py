
from itertools import chain

class Grid:
    def copy(self):
        grid = []
        for line in self.grid:
            grid.append([e.copy() for e in line])
        return Grid(grid)
    
    def __init__(self, fp, cls):
        lines = [l.strip() for l in fp.readlines()]
        grid = []
        for line in lines:
            ln = []
            grid.append(ln)
            for ch in line:
                ln.append(cls(ch))

        self.grid = grid
        self.width = len(grid)
        self.height = len(grid[0])
        
    def get(self, x, y):
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        return self.grid[y][x]
    
    def __iter__(self):
        for y in range(self.height):
            for x in range(self.width):
                yield self.get(y,x), y, x

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.get(x,y), end="")
            print("")

    def select_neighbors(self, x, y, deltas):
        for dx, dy in deltas:
            if self.get(x+dx, y+dy):
                yield self.get(x+dx, y+dy), x+dx, y+dy

    def cardinal_neighbors(self, x, y):
        return self.select_neighbors(x,y, [(1,0), (0,1), (-1,0), (0,-1)])
    
    def diagonal_neighbors(self, x, y):
        return self.neighbors(x,y, [(1,1), (-1,-1), (-1,1), (1,-1)])
    
    def neighbors(self, x ,y):
        return chain(self.cardinal_neighbors(x,y), self.diagonal_neighbors(x,y))