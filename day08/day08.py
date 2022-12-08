def pivot_data(data):
    new_data = []
    for i, _ in enumerate(data):
        new_line = []
        for _, line in enumerate(data):
            new_line.append(line[i])
        new_data.append(''.join(new_line))
    return new_data

def part1(data):
    pivot = pivot_data(data)                    # pivot data (switch cols and rows)
    
    sum = len(data) * 4 - 4                     # count all edge trees
    
    for r_idx in range(1,len(data)-1):          # ignore first tree and last tree in row since already regarded as edge
        for c_idx in range(1,len(data[0])-1):   # ignore first tree and last tree in col since already regarded as edge
            row = data[r_idx]
            col = pivot[c_idx]
            tree = data[r_idx][c_idx]
            if tree > max(row[:c_idx]) or \
               tree > max(row[c_idx+1:]) or \
               tree > max(col[:r_idx]) or \
               tree > max(col[r_idx+1:]): 
                sum += 1 
    return sum

def look(tree, sight):
    if sight == "":
        return 0
    res = 0
    for s in sight:
        if int(tree) > int(s):
            res += 1
        else:
            res += 1
            break
    return res

def check_sight(tree, r_idx, c_idx, row, col):
    up = look(tree, col[:r_idx][::-1]) # looking up ([::1] reverses the string)
    left = look(tree, row[:c_idx][::-1]) # looking left
    right = look(tree, row[c_idx+1:]) # looking right
    down = look(tree, col[r_idx+1:]) # looking down
    return up * down * left * right

def part2(data):
    pivot = pivot_data(data)
    res = 0
    for r_idx in range(len(data)):
        for c_idx in range(len(data[0])):
            tree = data[r_idx][c_idx]
            res = max(res, check_sight(tree, r_idx, c_idx, data[r_idx], pivot[c_idx]))
    return res

if __name__ == "__main__":
    with open('day08/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))