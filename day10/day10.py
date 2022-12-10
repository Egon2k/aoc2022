def part1(data):
    cycles = 0
    register = 1
    sum = 0
    
    for line in data:
        cycles_old = cycles
        if line.startswith('add'):
            instr, val = line.split(' ')
            cycles += 3
            register += int(val)
        else:
            instr = 'noop'
            cycles += 1

        if cycles % 20 == 0:
            sum += (cycles // 20) * 20 * register
     
    return sum
        

def part2(data):
    pass

if __name__ == "__main__":
    with open('day10/testdata.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))