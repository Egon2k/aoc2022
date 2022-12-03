def calc_prio(char):
    if char.isupper():
        prio =  ord(char) - ord('A') + 1 + 26
    if char.islower():
        prio =  ord(char) - ord('a') + 1
    return prio

    
def find_intersect2(list1, list2):
    return list(set(list1).intersection(list2))

def find_intersect3(list1, list2, list3):
    return list(set(list1).intersection(list2).intersection(list3))

def split_rucksack(rucksack):
    # * = unpack operator
    comp1 = [*rucksack[:len(rucksack)//2]]
    comp2 = [*rucksack[len(rucksack)//2:]]
    return comp1,comp2

def split_into_groups(data):
    groups = [[*data[i:i+3]] for i in range(0, len(data), 3)]
    return groups

def part1(data):
    sum = 0
    for rucksack in data:
        comp1, comp2 = split_rucksack(rucksack)
        intersect = find_intersect2(comp1, comp2)
        sum += calc_prio(intersect[0])
    return(sum)

def part2(data):
    sum = 0
    groups = split_into_groups(data)
    for group in groups:
        intersect = find_intersect3(group[0], group[1], group[2])
        sum += calc_prio(intersect[0])
    return(sum)

if __name__ == "__main__":
    data = []

    with open('day03/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))