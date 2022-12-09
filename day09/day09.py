RIGHT = (1,0)
LEFT  = (-1,0)
UP    = (0,1)
DOWN  = (0,-1)

def add_tuples(x, y):
    return tuple(map(lambda i, j: i + j, x, y))

def is_touching(t,h):
    return (abs(h[0] - t[0]) <= 1) and \
           (abs(h[1] - t[1]) <= 1)

def follow(t, h):
    if t == h:
        return t            # overlap, do nothing
    elif is_touching(t,h):
        return t            # touching, do nothing
    else:
        if t[0] == h[0]:    # vertical
            if t[1] < h[1]:
                t = add_tuples(t, UP)
            else:
                t = add_tuples(t, DOWN)
        elif t[1] == h[1]:  # horizontal
            if t[0] < h[0]:
                t = add_tuples(t, RIGHT)
            else:
                t = add_tuples(t, LEFT)
        else:               # diagonal
            if t[0] < h[0] and t[1] < h[1]:
                t = add_tuples(t, RIGHT)
                t = add_tuples(t, UP)
            elif t[0] < h[0] and t[1] > h[1]:
                t = add_tuples(t, RIGHT)
                t = add_tuples(t, DOWN)
            elif t[0] > h[0] and t[1] < h[1]:
                t = add_tuples(t, LEFT)
                t = add_tuples(t, UP)
            elif t[0] > h[0] and t[1] > h[1]:
                t = add_tuples(t, LEFT)
                t = add_tuples(t, DOWN)
    return t

def print_test_grid(t,h):
    #for i in range(4,-1,-1):
    #    for j in range(0,6,1):
    for i in range(10,-10,-1):
        for j in range(-10,10,1):     
            if (j,i) == h:
                print("H", end = "")
            elif (j,i) == t:
                print("T", end = "")
            elif (j,i) == (0,0):
                print("s", end = "")
            else:
                print(".", end = "")
        print("\n", end = "")
    print("\n", end = "")

def part1(data):
    h = (0,0)
    t = (0,0)
    t_pos = []

    for line in data:
        dir_, len_ = line.split(' ')
        
        for _ in range(int(len_)):
            #print_test_grid(t,h)
            
            if dir_ == 'R':
                h = add_tuples(h, RIGHT)
            elif dir_ == 'L':
                h = add_tuples(h, LEFT)
            elif dir_ == 'U':
                h = add_tuples(h, UP)
            elif dir_ == 'D':
                h = add_tuples(h, DOWN)
        
            t = follow(t,h)
            t_pos.append(t)
    
    return len(set(t_pos))

def part2(data):
    pass

if __name__ == "__main__":
    with open('day09/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))