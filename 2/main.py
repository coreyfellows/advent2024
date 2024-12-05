from sys import exit
from collections import defaultdict

def load_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    return [list(map(int, line.strip().split(" "))) for line in lines]

def calculate_line(line):
    ascending = None
    for i in range(len(line)):
        if i == 0:
            continue

        if line[i-1] == line[i]:
            return 0

        if ascending is None:
            ascending = line[i-1] < line[i]

        if ascending and line[i-1] > line[i]:
            return 0        
        if not ascending and line[i-1] < line[i]:
            return 0
        
        if abs(line[i-1] - line[i]) > 3:
            return 0

    return 1

            
def solution_1(lines):
    return sum(calculate_line(line) for line in lines)

def solution_2(lines):
    total = 0
    for line in lines:
        success = calculate_line(line)
        total += success

        if not success:
            for idx in range(len(line)):
                cp = line[:]
                cp.pop(idx)
                success = calculate_line(cp)
                total += success
                if success:
                    break
    return total

def main():
    lines = load_input("input.txt")
    print(f"{solution_1(lines)=}")
    print(f"{solution_2(lines)=}")
    return 0

if __name__ == "__main__":
    exit(main())