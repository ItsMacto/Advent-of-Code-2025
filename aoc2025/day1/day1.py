from aoc2025.utils.utils import read_input


def star1() -> int:
    data = read_input()
    # print(data)
    
    STARTING_POS = 50
    pos = STARTING_POS
    count = 0
    for line in data:

        direction, value = line[0], line[1:]
        value = int(value)
        value = value % 100  # Normalize value to within 0-99
        if direction == "R":
            pos += value
        elif direction == "L":
            pos -= value
        pos = pos % 100  # Wrap around the circular track
        # print(direction, value, pos)

        if pos == 0:
            count += 1
    return count


def star2() -> int:
    data = read_input()
    
    # data = read_input(test=True)
    # print(data)
    
    STARTING_POS = 50
    pos = STARTING_POS
    count = 0
    for line in data:
        direction, value = line[0], line[1:]
        value = int(value)
        
        if direction == "R":
            pos += value
            rotations, pos = divmod(pos, 100)
            # print(rotations, pos)
            count += rotations
        elif direction == "L":
            s_pos = pos
            pos -= value
            rotations, pos = divmod(pos, 100)
            # print(-rotations, pos)
            if s_pos == 0 and pos != 0:
                rotations += 1
            count -= rotations
            if pos == 0: 
                count += 1
        
        # print(direction, value, pos)
    return count


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
