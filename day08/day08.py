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

def check_sight(r_idx, c_idx, row, col):
    pass

def part2(data):
    pivot = pivot_data(data)
    for r_idx in range(len(data)):
        for c_idx in range(len(data[0])):
            check_sight(r_idx, c_idx, data[r_idx], pivot[c_idx])

if __name__ == "__main__":
    with open('day08/testdata.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))