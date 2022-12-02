lose = [('A','Z'),('B','X'),('C','Y')]
draw = [('A','X'),('B','Y'),('C','Z')]
win = [('A','Y'),('B','Z'),('C','X')]

points = {'X':1, 'Y':2, 'Z':3}

def part1(data):
    score = 0
    for line in data:
        play = tuple(line.split(' '))
        score += points[play[1]]
        if play in draw:
            score += 3
        elif play in win:
            score += 6

    return score

def part2(data):
    pass

if __name__ == "__main__":
    data = []

    with open('day02/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))