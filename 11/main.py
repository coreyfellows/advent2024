from sys import exit
from os import path
import sys
from typing import List

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()
       
def load_input(filename) -> List[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().strip().split(" ")))


def apply_rules(value: int) -> List[int]:
    if value == 0:
        return [1,]
    if len(stringified := str(value)) % 2 == 0:
        length = len(stringified)
        return [int(stringified[0:length//2]), int(stringified[length//2:length])]
    return [2024 * value,]

def solution(stones, blinks) -> int:
    while blinks:
        new_stones: List[int] = []
        for stone in stones:
            new_stones.extend(apply_rules(stone))
        stones = new_stones
        blinks -= 1
        print(blinks, len(stones))
        
    return len(stones)

def main():
    stones = load_input("sample.txt")
    print(f"{solution(stones, 25)=}")
    print(f"{solution(stones, 75)=}")
    return 0

if __name__ == "__main__":
    exit(main())