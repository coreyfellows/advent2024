from sys import exit
from collections import defaultdict
from itertools import permutations
from functools import cmp_to_key

def load_input(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    
    rules = []
    pages = None
    for line in lines:
        line = line.strip()

        if not line:
            pages = []
            continue
        if pages is not None:
            pages.append(list(map(int, line.split(","))))
            continue
        rules.append(list(map(int, line.split("|"))))

    return rules, pages
    
def fixed_page(key_func, page):
    sorted_page = list(sorted(page, key=key_func))
    return None if sorted_page == page else sorted_page

def solution_1(rules, pages):
    total = 0
    for page in pages:
        if not fixed_page(rules, page):
            total += page[int(len(page)/2)]
    return total


def solution_2(rules, pages):
    total = 0
    for page in pages:
        if sorted_page := fixed_page(rules, page):
            total += sorted_page[int(len(sorted_page)/2)]
    return total


def main():
    rules, pages = load_input("input.txt")
    cmp = cmp_to_key(lambda a, b: -1 if [a,b] in rules else 1)
    print(f"{solution_1(cmp, pages)=}")
    print(f"{solution_2(cmp, pages)=}")
    return 0

if __name__ == "__main__":
    exit(main())