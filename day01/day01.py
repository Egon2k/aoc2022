def helper(data):
    sum = 0
    sumList = []
    for line in data:
        if line != "":
            sum += int(line.strip())
        else:
            sumList.append(sum)
            sum = 0
    return sumList

def part1(data):
    return max(helper(data))

def part2(data):
    sumList = helper(data)
    return sum(sorted(sumList)[-3:])

if __name__ == "__main__":
    data = []

    with open('day01/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))