# from aoc2024.utils.utils import read_input
from aoc2025.utils.utils import read_input

def star1():
    # data = read_input(fileName="test.txt")
    data = read_input()
    data = [int(digit) for digit in data[0]]
    total = 0
    length = 0 

    for i in range(len(data)):
        length += int(data[i])

    # print(length)
    disk = [0] * length
    
    l, r = 0, len(data) - 1
    lid, rid = 0, len(data) // 2

    i = 0
    left = True
    blanks = 0

    while l <= r:
        if left:
            for _ in range(data[l]):
                disk[i] = lid
                i += 1
            l += 1
            lid += 1
            blanks = data[l]
            left = False
        else:
            for _ in range(blanks):
                if data[r] == 0:
                    r -= 2
                    rid -= 1
                disk[i] = rid
                i += 1
                data[r] -= 1
            l += 1
            left = True
    # print(disk)
    for i, v in enumerate(disk):
        total += v * i
    return total


# it works! But its super slow lol
def star2():
    
    # data = read_input(test=True, split=False)
    data = read_input( split=False)
    data = [int(digit) for digit in data]
    data_list = []
    data_map = {}
    for i, v in enumerate(data):
        if i % 2 == 0:
            data_map[i//2] = (len(data_list), v)
            data_list.extend([i//2]* v)
        else:
            data_list.extend([-1]* v)
    # print(data_list)
    
    for i, v in reversed(data_map.items()):
        # print(i, v)
        for k in range(0, v[0]):
            if data_list[k:k+v[1]].count(-1) == v[1]:
                data_list[k:k+v[1]] = [i]* v[1]
                data_list[v[0]:v[0]+v[1]] = [-1]* v[1]
                break
        # print(data_list)
        # print(i)
    
    
    total = 0
    for i, v in enumerate(data_list):
        if v != -1:
            total += v * i
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
