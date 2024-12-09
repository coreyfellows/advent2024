from sys import exit
from collections import namedtuple
from itertools import product, zip_longest, chain
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()

Equation = namedtuple("Equation", ["target", "values"])

def load_input(filename):
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    equations = []
    for line in lines:
        target, values = line.split(":")
        equations.append(Equation(int(target), [int(v.strip()) for v in values.strip().split(" ")]))

    print(equations)
    return equations

def evauluate(expression: list):
    expression.reverse()
    total = expression.pop()
    while len(expression):
        op = expression.pop()
        if op == "*":
            total *= expression.pop()
        elif op == "+":
            total += expression.pop()
        elif op == "|":
            rhs = expression.pop()
            total = total * pow(10, len(str(rhs))) + rhs
    return total
    
def solution(equations, operators):
    total = 0
    for eq in equations:
        for combination in product(operators, repeat=len(eq.values)-1):
            expression = list(zip_longest(eq.values, combination))
            expression = [x for x in chain(*expression) if x]
            result = evauluate(expression)

            if result == eq.target:
                total += eq.target
                break
    return total

def solution_1(equations):
    return solution(equations, "+*")

def solution_2(equations):
    return solution(equations, "+*|")

def main():
    equations = load_input("input.txt")
    print(f"{solution_1(equations)=}")
    print(f"{solution_2(equations)=}")
    return 0

if __name__ == "__main__":
    exit(main())