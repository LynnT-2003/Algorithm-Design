# You are given a 3x3 grid filled with numbers from 1 to 8 and an empty space represented by '0'. 
# The grid is initially in a random configuration. 
# You can perform a "slide" operation, which moves the empty space to an adjacent cell (either horizontally or vertically). 
# Your goal is to transform the grid into the following goal state:
# 1 2 3
# 4 5 6
# 7 8 0
# Write a Python program that calculates the minimum number of sliding operations required to reach the goal state 
# from the given initial configuration.

from collections import deque

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define possible moves (up, down, left, right)
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
move_names = ['Left', 'Right', 'Up', 'Down']  # Corresponding move names

# Function to find the empty space ('0') coordinates in the grid
def find_empty(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j

# Function to perform a sliding move
def slide(grid, move):
    empty_x, empty_y = find_empty(grid)
    new_x, new_y = empty_x + move[0], empty_y + move[1]

    if 0 <= new_x < 3 and 0 <= new_y < 3:
        grid[empty_x][empty_y], grid[new_x][new_y] = grid[new_x][new_y], grid[empty_x][empty_y]

# Function to check if the grid is in the goal state
def is_goal(grid):
    return grid == goal_state

# Breadth-First Search to find the minimum number of moves
def min_moves(initial_grid):
    visited = set()
    queue = deque([(initial_grid, 0)])  # (grid, moves)

    while queue:
        current_grid, moves_count = queue.popleft()
        visited.add(tuple(map(tuple, current_grid)))

        print(f"Move {moves_count}:")
        for row in current_grid:
            print(row)
        print()

        if is_goal(current_grid):
            return moves_count

        for move, move_name in zip(moves, move_names):
            new_grid = [row[:] for row in current_grid]  # Create a copy of the grid
            slide(new_grid, move)

            if tuple(map(tuple, new_grid)) not in visited:
                queue.append((new_grid, moves_count + 1))
                print(f"Applying {move_name} Move:")
                for row in new_grid:
                    print(row)
                print(f"Moves Count: {moves_count + 1}")
                print()

    return -1  # Goal state cannot be reached

# Input: Initial grid configuration
initial_grid = [[1, 3, 0], [4, 2, 5], [7, 8, 6]]

# Calculate and print the minimum number of moves
result = min_moves(initial_grid)
print("Minimum number of sliding operations to reach the goal state:", result)