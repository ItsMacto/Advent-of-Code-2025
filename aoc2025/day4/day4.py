from aoc2025.utils.utils import read_input, to_grid, grid_print, grid_get


def star1() -> int:
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]   
    data = read_input()
    grid = to_grid(data)
    total = 0
    locations = []
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value != '@':
                continue
            count = 0
            for dy, dx in DIRECTIONS:
                neighbor = grid_get(grid,row=y + dy, col=x + dx, default='.')
                if neighbor == '@':
                    count += 1
                if count >= 4:
                    break
            total += 1 if count < 4 else 0
            if count < 4:
                locations.append((x, y))

            
            
    
    return total


def star2() -> int:
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]   
    data = read_input()
    grid = to_grid(data)
    total = 0
    
    can_move = [[0,0]]
    while can_move:
        can_move = []
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value != '@':
                    continue
                count = 0
                for dy, dx in DIRECTIONS:
                    neighbor = grid_get(grid,row=y + dy, col=x + dx, default='.')
                    if neighbor == '@':
                        count += 1
                    if count >= 4:
                        break
                if count < 4:
                    total += 1
                    can_move.append((x, y))
        for x, y in can_move:
            grid[y][x] = '.'

            
    return total


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
