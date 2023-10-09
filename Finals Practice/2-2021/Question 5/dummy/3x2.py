board = []
for i in range(3):  # Update the range for a 3x2 board
    a = list(map(int, input().split()))
    board.extend(a)

# Update the adjacency list for a 3x2 board
adj = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]

class state():
    def __init__(self, board):
        self.board = board
        self.g = 0  # number of steps from start to this state
        self.parent = None

def successor(s):
    succ = []
    for x, y in adj:
        new_board = s.board.copy()
        new_board[x], new_board[y] = new_board[y], new_board[x]

        x = state(new_board)
        x.g = s.g + 1
        x.parent = s

        succ.append(x)

    return succ

def is_goal(s):
    return s.board == list(range(1, 7))

def BFS(s):
    Q = [s]
    Reached = set()
    Reached.add(tuple(s.board))

    while Q:
        node = Q.pop(0)
        print(f"This is how it looks now (Current State):")
        for i in range(0, 6, 2):  # Display the grid in a 3x2 format
            print(node.board[i:i+2])
        print()

        if is_goal(node):
            print("Goal state reached!")
            return node.g

        for suc in successor(node):
            if tuple(suc.board) not in Reached:
                Reached.add(tuple(suc.board))
                Q.append(suc)
                print(f"Trying a Move (Adding State to Queue):")
                for i in range(0, 6, 2):  # Display the grid in a 3x2 format
                    print(suc.board[i:i+2])
                print()
    return False

# Sample test case for a 3x2 board
# Input:
# 1 4
# 3 2
# 6 5
# Expected Output:
# Minimum number of swaps to reach the goal: 2
result = BFS(state(board))
if result:
    print(f"Minimum number of swaps to reach the goal: {result}")
else:
    print("Goal state cannot be reached.")
