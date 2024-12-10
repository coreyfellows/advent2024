from sys import exit
from collections import namedtuple
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
import utils
sys.path.pop()

       
def load_input(filename):
    with open(filename, "r") as f:
        return list(map(int, f.read().strip()))
    

def checksum(memory):
    total = 0
    for idx, v in enumerate(memory):
        if v is not None:
            total += idx * v 

    return total

def checksum_blocks(memory):
    total = 0
    idx = 0
    for v in memory:
        if v.file_id is None:
            idx += v.width
            continue
        for i in range(v.width):
            total += (idx+i) * v.file_id
        idx += v.width
    return total

def solution_1(filesystem):
    file_id = 0
    on = True
    memory = []
    for v in filesystem:
        if on:
            memory.extend([file_id] * v)
            file_id+=1
        if not on:
            memory.extend([None] * v)
        on = not on

    idx = 0
    while idx < len(memory):
        if memory[idx] is not None:
            idx += 1
            continue
        while (final := memory.pop()) is None:
            pass

        if idx >= len(memory):
            memory.append(final)
        else:
            memory[idx] = final    
    return checksum(memory)

class Block:
    def __init__(self, width, file_id):
        self.width = width
        self.file_id = file_id

def solution_2(filesystem):
    file_id = 0
    on = True
    memory = []
    for v in filesystem:
        if on:
            memory.append(Block(v, file_id))
            file_id+=1
        if not on:
            memory.append(Block(v, None))
        on = not on

    idx = len(memory) - 1
    while idx:
        if memory[idx].file_id is None:
            idx-=1
            continue

        for seek in range(0, idx):
            if memory[seek].file_id is None and memory[seek].width >= memory[idx].width:
                memory[seek].file_id = memory[idx].file_id
                dw = memory[seek].width - memory[idx].width
                memory[seek].width = memory[idx].width
                memory[idx].file_id = None
                if dw:
                    memory.insert(seek+1, Block(dw, None))
                    idx += 1
                break
        idx-=1

    return checksum_blocks(memory)   

def main():
    filesystem = load_input("input.txt")
    print(f"{solution_1(filesystem)=}")
    print(f"{solution_2(filesystem)=}")
    return 0

if __name__ == "__main__":
    exit(main())