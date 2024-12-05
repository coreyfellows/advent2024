from sys import exit
from collections import defaultdict
import re

def load_input(filename):
    with open(filename, "r") as f:
        lines = f.read().strip()
    
    return lines


            
def solution_1(inp):
    total = 0
    for m in re.finditer("mul\((\d+),(\d+)\)", inp):
        a,b = int(m.group(1)),int(m.group(2))
        total += a*b
    return total


def solution_2(inp):
    total = 0
    enabled = True
    for m in re.finditer("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", inp):
        operation = m.group(1)
        if operation == "don't()":
            enabled = False
            continue
        if operation == "do()":
            enabled = True
            continue
        if enabled:
            a,b = int(m.group(2)),int(m.group(3))
            total += a*b
        #total += a*b
    return total 

def main():
    lines = load_input("input.txt")
    print(f"{solution_1(lines)=}")
    print(f"{solution_2(lines)=}")
    return 0

if __name__ == "__main__":
    exit(main())