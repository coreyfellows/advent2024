
class Grid:
    def copy(self):
        grid = []
        for line in self.grid:
            grid.append([e.copy() for e in line])
        return Grid(grid)
    
    def __init__(self, grid):
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
                yield self.get(y,x)

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.get(x,y), end="")
            print("")
