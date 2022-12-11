class Monkey():
    def __init__(self, items : list, op : str, test : int, t : int, f : int):
        self.items = items[:]
        self.op = self.parse_op(op)
        self.test = test
        self.t = t
        self.f = f
        self.inspected_items = 0

    def parse_op(self, op_string):
        if op_string.endswith('old'):
            op = ['square', 0]
        elif "+" in op_string:
            op = ['+', int(op_string.split(' ')[-1])]
        elif "*" in op_string:
            op = ['*', int(op_string.split(' ')[-1])]
        return op

    def inspect_p1(self):
        if len(self.items) > 0:
            self.inspected_items += 1
            if (self.op[0] == '+'):
                self.items[0] += self.op[1]
            elif (self.op[0] == '*'):
                self.items[0] *= self.op[1]
            elif (self.op[0] == 'square'):
                self.items[0] *= self.items[0]
            self.items[0] = int(self.items[0] / 3)
    
    def inspect_p2(self, lcm):
        if len(self.items) > 0:
            self.inspected_items += 1
            if (self.op[0] == '+'):
                self.items[0] += self.op[1]
            elif (self.op[0] == '*'):
                self.items[0] *= self.op[1]
            elif (self.op[0] == 'square'):
                self.items[0] *= self.items[0]
            self.items[0] = int(self.items[0]) % lcm

    def throw_item(self):
        if len(self.items) > 0:
            if self.items[0] % self.test == 0:
                return self.t, self.items.pop(0)
            else:
                return self.f, self.items.pop(0)

    def catch_item(self, item):
        self.items.append(item)

def parse_monkeys(data):
    monkeys = []
    
    for idx, line in enumerate(data):
        if idx % 7 == 1:
            items = line[len('  Starting items: '):].split(', ')
            items = [int(i) for i in items]
        if idx % 7 == 2:
            op = line[len('  Operation: new = '):]
        if idx % 7 == 3:
            test = line[len('  Test: divisible by '):]
            test = int(test)
        if idx % 7 == 4:
            t = line[len('    If true: throw to monkey '):]
            t = int(t)
        if idx % 7 == 5:
            f = line[len('    If false: throw to monkey '):]
            f = int(f)
        if idx % 7 == 6:
            monkeys.append(Monkey(items, op, test, t, f))

    monkeys.append(Monkey(items, op, test, t, f))               # dont forget about last monkey
    return monkeys

def part1(monkeys):
    for _ in range(20):
        for monkey in monkeys: 
            while(monkey.items != []):
                monkey.inspect_p1()
                receiver, item = monkey.throw_item()
                monkeys[receiver].catch_item(item)

    solution = sorted([monkey.inspected_items for monkey in monkeys])
    return solution[-2] * solution[-1]


def part2(monkeys):
    import math
    lcm = math.lcm(*[monkey.test for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys: 
            while(monkey.items != []):
                monkey.inspect_p2(lcm)
                receiver, item = monkey.throw_item()
                monkeys[receiver].catch_item(item)

    solution = sorted([monkey.inspected_items for monkey in monkeys])
    return solution[-2] * solution[-1]

if __name__ == "__main__":
    with open('day11/data.txt') as f:
        data = f.read().splitlines()

    monkeys = parse_monkeys(data)
    print(part1(monkeys))
    monkeys = parse_monkeys(data)
    print(part2(monkeys))