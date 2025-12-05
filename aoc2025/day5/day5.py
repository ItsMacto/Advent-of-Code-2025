from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    ranges = []
    ids = []
    next = False
    for line in data:
        if line == "":
            next = True
            continue
        if not next:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
        else:
            ids.append(int(line))
    
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break
            


    return count

def star2() -> int:
    data = read_input()
    ranges = []
    for line in data:
        if line == "":
            break
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
        
    count = 0
    ranges.sort()
    last_id = ranges[0][0] - 1
    for start, end in ranges:
        if start > last_id:
            count += end - start + 1
        elif end > last_id:
            count += end - last_id
        last_id = max(last_id, end)


    return count


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
