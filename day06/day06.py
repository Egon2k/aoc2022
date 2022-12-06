def solve(str, n):
    for idx, _ in enumerate(str[:-n]):
        sub_str = [*str[idx:idx + n]]
        if len(set(sub_str)) == n:
            return idx + n

def part1(str):
    return solve(str, 4)

def part2(str):
    return solve(str, 14)

if __name__ == "__main__":
    with open('day06/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data[0]))
    print(part2(data[0]))