import re

def part1(crates, data):
    for instr in data:
        temp = re.search(r'move (\d+) from (\d+) to (\d+)', instr).groups()     # get groups from regex
        temp = [int(t) for t in temp]                                           # convert to int
        
        for _ in range(temp[0]):
            crates[temp[2] - 1].append(crates[temp[1] - 1].pop())               # pop from source and append on destination

    return "".join([crate.pop() for crate in crates])                           # return joined string

def part2(crates, data):
    for instr in data:
        temp = re.search(r'move (\d+) from (\d+) to (\d+)', instr).groups()     # get groups from regex
        temp = [int(t) for t in temp]                                           # convert to int
        
        for x in range(temp[0]):
            idx = - temp[0] + x
            crates[temp[2] - 1].append(crates[temp[1] - 1][idx])                # append on destination
            del crates[temp[1] - 1][idx]                                        # delete (pop) from source

    return "".join([crate.pop() for crate in crates])                           # return joined string

def init_crates():
    return [
        ['D', 'L', 'V', 'T', 'M', 'H', 'F'],
        ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P'],
        ['R', 'S', 'D', 'M', 'P', 'H' ],
        ['L', 'B', 'V', 'F'],
        ['N', 'H ', 'G ', 'L ', 'Q'],
        ['W', 'B', 'D', 'G', 'R', 'M', 'P'],
        ['G', 'M', 'N', 'R', 'C', 'H', 'L', 'Q'], 
        ['C', 'L', 'W'],
        ['R', 'D', 'L', 'Q', 'J', 'Z', 'M', 'T']
    ]

if __name__ == "__main__":
    with open('day05/data.txt') as f:
        data = f.read().splitlines()

    # cut off the top lines
    while not data[0].startswith('move'):
        data.pop(0)

    print(part1(init_crates(), data))
    print(part2(init_crates(), data))