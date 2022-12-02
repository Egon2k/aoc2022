lose = [('A','Z'),('B','X'),('C','Y')]
draw = [('A','X'),('B','Y'),('C','Z')]
win = [('A','Y'),('B','Z'),('C','X')]

points = {'X':1, 'Y':2, 'Z':3}

def inc_score(play):
    inc = points[play[1]]
    if play in draw:
        inc += 3
    elif play in win:
        inc += 6
    return inc

def get_play(op_move, strategy_array):
    for play in strategy_array:
        if play[0] == op_move:
            return play

def part1(data):
    score = 0
    for line in data:
        play = tuple(line.split(' '))
        score += inc_score(play)

    return score

def part2(data):
    score = 0
    for line in data:
        op_move = line.split(' ')[0]
        strategy = line.split(' ')[1]

        if strategy == 'X': #lose
            play = get_play(op_move, lose)
        elif strategy == 'Y': #draw
            play = get_play(op_move, draw)
        elif strategy == 'Z': #win
            play = get_play(op_move, win)

        score += inc_score(play)
    return score

if __name__ == "__main__":
    data = []

    with open('day02/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))