from aoc2025.utils.utils import read_input, to_grid, grid_get


def star1() -> int:
    def num_edges(point, grid):
        r, c, val = point
        edges = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = grid_get(grid, r + dr, c + dc)
            if neighbor is None or neighbor != val:
                edges += 1
        return edges
    
    
    # data = read_input(test=True)
    data = read_input()
    grid = to_grid(data)
    points = set()
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            points.add((r, c, val))
    
    seen = set()
    regions = {} # key: [area, perimeter]
    for point in points:
        _, _, cur = point
        if point in seen:
            continue
        seen.add(point)
        area, perimeter = 0, 0
        stack = [point]
        while stack:
            current = stack.pop()
            area += 1
            perimeter += num_edges(current, grid)
            r, c, val = current
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n = grid_get(grid, r + dr, c + dc)
                
                if n == val:
                    neighbor = (r + dr, c + dc, n)
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        
        regions[point] = [area, perimeter]
    
        # size = regions.get(cur, [0, 0])
        # regions[cur] = [size[0] + area, size[1] + perimeter]
    
    total = 0
    for area, perimeter in regions.values():
        total += area * perimeter  
    return total


def star2() -> int:
    def num_prem_sides(point, grid):
        r, c, val = point
        prem_sides = 0
        edges = []
        for dr, dc, s in [(-1, 0, 'd'), (1, 0, 'u'), (0, -1, 'l'), (0, 1, 'r')]:
            neighbor = grid_get(grid, r + dr, c + dc)
            if neighbor != val:
                edges.append(s)
                
        if len(edges) == 0:
            return -1
        
        
        
    data = read_input(test=True)
    
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")
