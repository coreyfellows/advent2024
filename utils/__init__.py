
from itertools import chain
from typing import Generic, Callable
from collections.abc import Iterable

T = TypeVar("T", bound=Callable[[str]])

class Grid(Generic[T]):    
    def __init__(self, fp, cls: T):
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
    
    def __getitem__(self, coords) -> T:
        x,y=coords
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        return self.grid[y][x]
    
    def __iter__(self) -> Iterable[tuple[T, int, int]]:
        for y in range(self.height):
            for x in range(self.width):
                yield self[y,x], y, x

    def __str__(self) -> str:
        lines = []
        for y in range(self.height):
            line = []
            for x in range(self.width):
                line.append(str(self[x,y]))
            lines.append("".join(line))
        return "\n".join(lines)

    def select_neighbors(self, x, y, relative_positions) -> Iterable[tuple[T, int, int]]:
        for dx, dy in relative_positions:
            if self[x+dx, y+dy]:
                yield self[x+dx, y+dy], x+dx, y+dy

    def cardinal_neighbors(self, x, y) -> Iterable[tuple[T, int, int]]:
        return self.select_neighbors(x,y, [(1,0), (0,1), (-1,0), (0,-1)])
    
    def diagonal_neighbors(self, x, y) -> Iterable[tuple[T, int, int]]:
        return self.select_neighbors(x,y, [(1,1), (-1,-1), (-1,1), (1,-1)])
    
    def neighbors(self, x ,y) -> Iterable[tuple[T, int, int]:
        return chain(self.cardinal_neighbors(x,y), self.diagonal_neighbors(x,y))
