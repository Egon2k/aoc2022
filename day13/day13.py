from functools import cmp_to_key

def solve(left, right):
    for l, r in zip(left, right):

        if type(l) == list and type(r) == list:
            result = solve(l, r)
            if result == True or result == False:
                return result
        elif type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                pass 
        elif type(l) == int and type(r) == list:
            result = solve([l], r)
            if result == True or result == False:
                return result
        elif type(r) == int and type(l) == list:
            result = solve(l, [r])
            if result == True or result == False:
                return result

    if len(left) > len(right):
        return False
    elif len(right) > len(left):
        return True

def part1(packets):
    sum = 0
    for idx, packet in enumerate(packets):
        left, right = packet
        if solve(left, right):
            sum += (idx + 1)
    return sum
    

def part2(packets):
    prod = 1
    all_packets = [[[2]], [[6]]]
    for packet in packets:
        left, right = packet
        all_packets.append(left)
        all_packets.append(right)
    
    all_packets.sort(key=cmp_to_key(lambda a, b: -1 if solve(a, b) else 1))         # handle return value of solve as -1 and 1 instead of True and False to satisfy the cmp_to_key function
    
    for idx, packet in enumerate(all_packets):
        if packet in [[[2]], [[6]]]:
            prod *= (idx + 1)
    return prod

if __name__ == "__main__":
    with open('day13/data.txt') as f:
        data = f.read().splitlines()
    
    packets = []

    for idx, line in enumerate(data):
        if idx % 3 == 0:
            left = eval(line)
        if idx % 3 == 1:
            right = eval(line)
        if idx % 3 == 2 or idx == len(data) - 1:
            packets.append([left, right])

    print(part1(packets))
    print(part2(packets))