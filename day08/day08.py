def pivot_data(data):
    new_data = []
    for i, _ in enumerate(data):
        new_line = []
        for _, line in enumerate(data):
            new_line.append(line[i])
        new_data.append(''.join(new_line))
    return new_data

def part1(data):
    pivot = pivot_data(data)        # pivot data (switch cols and rows)
    
    sum = len(data) * 4 - 4         # count all edge trees
    
    for row in range(1,len(data)-1):
        for col in range(1,len(data[0])-1):
            tree_row = data[row]
            tree_col = pivot[col]
            tree = data[row][col]
            if tree > max(tree_row[:col]) or \
               tree > max(tree_row[col+1:]) or \
               tree > max(tree_col[:row]) or \
               tree > max(tree_col[row+1:]): 
                sum += 1 
    return sum

def part2(data):
    ...

if __name__ == "__main__":
    with open('day08/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))