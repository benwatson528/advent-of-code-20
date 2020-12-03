from typing import List

TREE = '#'
Position = (int, int)
grid = []
grid_width = 0
grid_height = 0
num_trees_hit = 0


def move(current_position: Position, right_steps: int, down_steps: int) -> Position:
    global num_trees_hit
    (x, y) = current_position
    if y + down_steps < grid_height and grid[y + down_steps][(x + right_steps) % grid_width] == TREE:
        num_trees_hit += 1
    return x + right_steps, y + down_steps


def solve(g: List[str], right_steps: int, down_steps: int) -> int:
    global grid, grid_width, grid_height, num_trees_hit
    grid = g
    grid_width = len(g[0])
    grid_height = len(g)
    num_trees_hit = 0
    position = (0, 0)
    while position[1] <= len(grid):
        #  draw_grid(position)
        position = move(position, right_steps, down_steps)
    return num_trees_hit


def draw_grid(current_position: Position):
    print(f"Drawing grid at current position {current_position}")
    for j in range(grid_height):
        for i in range(grid_width):
            print("X", end='') if current_position[0] % grid_width == i and current_position[1] == j else print(
                grid[j][i], end='')
        print()
    print()
