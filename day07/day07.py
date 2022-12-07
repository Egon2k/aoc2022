def solve(data, open_folders, all_folders):
    for line in data:
        if line.startswith('$ cd '):            # change directory
            parameter = line.split(' ')[-1]
            if parameter == '..':               # leave folder
                all_folders.append(open_folders.pop())
            else:                               # enter folder
                open_folders.append(0)
        elif line.startswith('$ ls'):           # list 
            continue                            # skip
        else:
            if line.startswith('dir'):          # is directory
                continue                        # skip
            else:                               # is file
                file_size = int(line.split(' ')[0])
                for i, _ in enumerate(open_folders):
                    open_folders[i] += file_size

def part1(data):
    open_folders = []
    all_folders = []

    solve(data, open_folders, all_folders)
    
    sum = 0
    for folder in open_folders + all_folders:
        if folder < 100_000:
            sum += folder
    return sum

def part2(data):
    open_folders = []
    all_folders = []

    solve(data, open_folders, all_folders)
    
    folders = open_folders + all_folders
    space_required = 40_000_000
    space_taken = max(folders)
    for folder in sorted(folders):
        if space_taken - folder < space_required:
            return folder

if __name__ == "__main__":
    with open('day07/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))
