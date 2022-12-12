import heapq, sys

DIR = [(1,0), (-1,0), (0,1), (0,-1)]

def dijkstra(g, s, t):
    '''
    https://stackoverflow.com/a/58833232
    '''
    q = []
    d = {k: sys.maxsize for k in g.keys()}
    p = {}

    d[s] = 0 
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w # equivalent to d[curr_v] + n_w 
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))

    return d[t]

def solve(grid, start, dest):
    return dijkstra(grid, start, dest)

def create_grid(data):
    grid = dict()

    for row in range(len(data)):
        for col in range(len(data[0])):
            weights = []
            
            for dir in DIR:
                dest = (row + dir[0], col + dir[1])
                if 0 <= dest[0] <= len(data) - 1 and \
                   0 <= dest[1] <= len(data[0]) - 1:
                    if data[row][col] == 'n':
                        pass
                    src_ascii = ord(data[row][col])
                    dest_ascii = ord(data[row + dir[0]][col + dir[1]])
                    if (dest_ascii - src_ascii) <= 1:
                        weight = 1
                    else:
                        weight = 999_999
                    weights.append([dest, weight])
                
            grid[(row,col)] = weights
    return grid


def part1(data, start, dest):
    grid = create_grid(data)
    return solve(grid, start, dest)

def part2(data):
    pass

if __name__ == "__main__":
    with open('day12/data.txt') as f:
        data = f.read().splitlines()

    for idx, line in enumerate(data):
        if 'S' in line:
            start = (idx, line.find('S'))
            data[idx] = line.replace('S', 'a')
    for idx, line in enumerate(data):    
        if 'E' in line:
            dest = (idx, line.find('E'))
            data[idx] = line.replace('E', 'z')

    print(part1(data, start, dest))
    print(part2(data))