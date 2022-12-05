def get_elfs(line):
    elf1, elf2 = [pair.split('-') for pair in line.split(',')]
    elf1 = list(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2 = list(range(int(elf2[0]), int(elf2[1]) + 1))
    return elf1,elf2

def part1(data):
    sum = 0
    for line in data:
        elf1, elf2 = get_elfs(line)
        if all(elem in elf1 for elem in elf2) or all(elem in elf2 for elem in elf1):
            sum += 1
    return sum

def part2(data):
    sum = 0
    for line in data:
        elf1, elf2 = get_elfs(line)
        if any(elem in elf1 for elem in elf2) or any(elem in elf2 for elem in elf1):
            sum += 1
    return sum

if __name__ == "__main__":
    with open('day04/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))