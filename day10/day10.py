def part1(data):
    cycles = -20        # starting at -20 because 20 is the first time, an interesting signal 
                        # appears, after that we can calculate with modulo 40
    add_cycles = 3
    register = 1
    sum = 0
    
    for line in data:
        if line.startswith('add'):
            instr, val = line.split(' ')
            add_cycles = 2
        else:
            instr = 'noop'
            add_cycles = 1

        for _ in range(add_cycles):
            cycles += 1
            if cycles == 0 or (cycles % 40 == 0):
                sum += ((cycles + 20) // 20) * 20 * register
        
        if instr.startswith('add'):
            register += int(val)

    return sum
        

def part2(data):
    grid = [['.' for _ in range(40)] for _ in range(6)]
    cycles = 0
    register = 1
    
    for line in data:
        sprite = [register - 1, register, register +1]
    
        if line.startswith('add'):
            instr, val = line.split(' ')
            add_cycles = 2
        else:
            instr = 'noop'
            add_cycles = 1

        for _ in range(add_cycles):
            col = int(cycles % 40)
            row = int(cycles / 40)
            cycles += 1
            if col in sprite:
                grid[row][col] = '#'

        if instr.startswith('add'):
            register += int(val)

    return grid    

def print_grid(grid):
    for line in grid:
        for c in line:
            print(c, end = '')
        print('')

if __name__ == "__main__":
    with open('day10/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print_grid(part2(data))