from sys import exit
from collections import defaultdict

def load_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    a, b = [], []
    for line in lines:
        l, r = line.strip().split("   ")
        a.append(int(l))
        b.append(int(r))

    return a,b


def solution_2(a,b):
    count_mapping = defaultdict(int)
    for n in b:
        count_mapping[n] += 1
    return sum(n * count_mapping[n] for n in a)


def solution_1(a, b):
    return sum(abs(l-r) for l, r in zip(sorted(a), sorted(b)))


def main():
    a,b = load_input("input.txt")
    print(f"{solution_1(a,b)=}")
    print(f"{solution_2(a,b)=}")
    return 0

if __name__ == "__main__":
    exit(main())