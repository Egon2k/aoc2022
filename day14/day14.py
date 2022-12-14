def sum_tuple(a,b):
    return (a[0] + b[0], a[1] + b[1])

def ripple_sand(sand):
    '''
    check if sand corn is falling streight or ripple to the side
    '''
    new_sand = sum_tuple(sand, (0, 1))

    if dg.get(new_sand, '.') == '.':
        return new_sand, True
    new_sand = sum_tuple(sand, (-1, 1))

    if dg.get(new_sand, '.') == '.':
        return new_sand, True
    new_sand = sum_tuple(sand, (1, 1))

    if dg.get(new_sand, '.') == '.':
        return new_sand, True

    return sand, False

def part1(dg):
    sum = 0
    abyss = 0
    for k, _ in dg.items():
        _, y = k
        abyss = max(abyss, y)

    sand = (500, 0)
    
    while True:
        old_sand = sand
        sand, rippled = ripple_sand(sand)

        if sand[1] >= abyss:
            break
        
        if rippled:
            dg[old_sand] = '.'
            dg[sand] = '+'
        else:
            dg[sand] = 'o'
            sum += 1
            sand = (500, 0)

    return sum
  
def part2(data):
    pass

if __name__ == "__main__":
    with open('day14/data.txt') as f:
        data = f.read().splitlines()
    
    dg = {}

    for i, line in enumerate(data):
        tokens = [tuple(int(y) for y in x.split(',')) for x in line.split(' -> ')]

        x1, y1 = tokens[0]

        for x2, y2 in tokens[1:]:
            dg[(x1, y1)] = '#'
            dg[(x2, y2)] = '#'

            while (x1, y1) != (x2, y2):
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                elif y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1
                dg[(x1, y1)] = '#'
    
    print(part1(dg))
    print(part2(data))