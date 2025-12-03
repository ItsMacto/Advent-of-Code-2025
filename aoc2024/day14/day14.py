from aoc2025.utils.utils import read_input
import math

BOARD_WIDTH = 101
BOARD_HEIGHT = 103
class Robot:
    
    def __init__(self, p, v) -> None:
        self.p_x = p[0]
        self.p_y = p[1]

        self.v_x = v[0]
        self.v_y = v[1]
    
    def move(self) -> None:
        new_x = self.p_x + self.v_x
        if new_x > BOARD_WIDTH - 1 or new_x < 0:
            new_x = new_x % BOARD_WIDTH
        self.p_x = new_x
        
        new_y = self.p_y + self.v_y
        if new_y > BOARD_HEIGHT - 1 or new_y < 0:
            new_y = new_y % BOARD_HEIGHT
        self.p_y = new_y
    
    def move_back(self) -> None:
        new_x = self.p_x - self.v_x
        if new_x > BOARD_WIDTH - 1 or new_x < 0:
            new_x = new_x % BOARD_WIDTH
        self.p_x = new_x
        
        new_y = self.p_y - self.v_y
        if new_y > BOARD_HEIGHT - 1 or new_y < 0:
            new_y = new_y % BOARD_HEIGHT
        self.p_y = new_y
            
    def __str__(self) -> str:
        return f"Robot Position: ({self.p_x}, {self.p_y}) Velocity: ({self.v_x}, {self.v_y})"
    
def print_board(robots: list[Robot]) -> None:
    board = [["." for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    for robot in robots:
        if board[robot.p_y][robot.p_x] == ".":
            board[robot.p_y][robot.p_x] = "#"
    for row in board:
        print("".join(row))


        
def star1() -> int:
    NUM_MOVES = 100
    data = read_input()
    robots = []
    for line in data:
        p, v = line.split()
        
        p = (int(p[2:p.find(",")]), int(p[p.find(",") + 1:]))
        v = (int(v[2:v.find(",")]), int(v[v.find(",") + 1:]))
        robot = Robot(p, v)
        robots.append(robot)
        
    for _ in range(NUM_MOVES):
        for robot in robots:
            robot.move()

    quadrant_counts = [0, 0, 0, 0]
    for robot in robots:
        if robot.p_x < BOARD_WIDTH // 2 and robot.p_y < BOARD_HEIGHT // 2:
            quadrant_counts[0] += 1
        elif robot.p_x > BOARD_WIDTH // 2 and robot.p_y < BOARD_HEIGHT // 2:
            quadrant_counts[1] += 1
        elif robot.p_x < BOARD_WIDTH // 2 and robot.p_y > BOARD_HEIGHT // 2:
            quadrant_counts[2] += 1
        elif robot.p_x > BOARD_WIDTH // 2 and robot.p_y > BOARD_HEIGHT // 2:
            quadrant_counts[3] += 1
    print(f"Quadrant counts: {quadrant_counts}")
    safety_fac = math.prod(quadrant_counts)
    return safety_fac

# tried a bunch of stuff to step and visualize the output to find the easter egg message
# saw a pattern at a interval and just printed that
# first time i turned on the vs code mini map
def star2() -> int:
    data = read_input()
    robots = []
    for line in data:
        p, v = line.split()
        
        p = (int(p[2:p.find(",")]), int(p[p.find(",") + 1:]))
        v = (int(v[2:v.find(",")]), int(v[v.find(",") + 1:]))
        robot = Robot(p, v)
        robots.append(robot)
    seconds = 0
    min_occupied = BOARD_WIDTH * BOARD_HEIGHT
    seconds_at_min = 0
    with open("aoc2024/day14/output.txt", "w") as f:
        for i in range(10000):
            if i % 101 == 23:
                board = [["." for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
                for robot in robots:
                    if board[robot.p_y][robot.p_x] == ".":
                        board[robot.p_y][robot.p_x] = "#"
            # count_occupied = sum(row.count("#") for row in board)
            # if count_occupied < min_occupied:
            #     min_occupied = count_occupied
            #     seconds_at_min = seconds
            #     print(f"New min occupied: {min_occupied} at second {seconds_at_min}")
                f.write(f"Second: {seconds}\n")

                for row in board:
                    f.write("".join(row) + "\n")
            for robot in robots:
                robot.move()
            seconds += 1
    return seconds_at_min

    # while True:
    #     print(f"Second: {seconds}")
    #     print_board(robots)
    #     for robot in robots:
    #         robot.move()
    #     seconds += 1
    #     # wait .25 seconds
    #     import time
    #     time.sleep(0.25)

    # for _ in range(4971):
    #     for robot in robots:
    #         robot.move()
    #     seconds += 1
    # while True:
    #     print(f"Second: {seconds}")
    #     print_board(robots)
    #     # get manual input to proceed to next move
    #     inp = input("arrows to move forward/backward, q to quit: ")

    #     if inp == "q":
    #         break
    #     elif inp == ".":
    #         for robot in robots:
    #             robot.move()
    #         seconds += 1
    #     elif inp == ",":
    #         for robot in robots:
    #             robot.move_back()
    #         seconds -= 1
    return 0


if __name__ == "__main__":
    print(f"Star 1: {star1()}")
    print(f"Star 2: {star2()}")


