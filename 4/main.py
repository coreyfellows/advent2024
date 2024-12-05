from sys import exit

def load_input(filename):
    with open(filename, "r") as f:
        lines = [[c for c in l.strip()] for l in f.readlines()]
    
    return lines, len(lines), len(lines[0])

def solution_1(lines, width, height):
    total = 0
    directions = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not x and not y:
                continue
            directions.append((x,y))

    def check_direction(remainder: list[str], x, y, dx, dy):
        y += dy
        x += dx
        if not remainder:
            return 1
        if y < 0 or y >= height:
            return 0
        if x < 0 or x >= width:
            return 0
        if lines[x][y] != remainder[-1]:
            return 0
        remainder.pop()
        return check_direction(remainder, x, y, dx, dy)
        

    for x in range(width):
        for y in range(height):
            if lines[x][y] == "X":
                for combo in directions:
                    total += check_direction(["S", "A", "M"], x, y, *combo)
    return total


def solution_2(lines, width, height):
    total = 0
    for x in range(1, width-1):
        for y in range(1, height-1):
            if lines[x][y] == "A":
                #check top left bottom right
                a, b = lines[x-1][y-1], lines[x+1][y+1]
                if not(a in ["M", "S"] and b in ["M", "S"] and a != b):
                    continue
                # check bottom left and top right
                a, b = lines[x+1][y-1], lines[x-1][y+1]
                if not(a in ["M", "S"] and b in ["M", "S"] and a != b):
                    continue
                total += 1
    return total


def main():
    lines, width, height = load_input("input.txt")
    print(f"{solution_1(lines, width, height)=}")
    print(f"{solution_2(lines, width, height)=}")
    return 0

if __name__ == "__main__":
    exit(main())