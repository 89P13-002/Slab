from collections import deque

# Structure to represent a cell
class Cell:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

# Function to check if a cell is valid
def is_valid(row, col, n, maze, visited):
    return (row >= 0 and col >= 0 and row < n and col < n and maze[row][col] == 0 and not visited[row][col])

# Function to find shortest path using BFS
def find_shortest_path(src_row, src_col, dest_row, dest_col, n, maze):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()

    # Mark the source cell as visited
    visited[src_row][src_col] = True
    q.append(Cell(src_row, src_col, 0))

    while q:
        cell = q.popleft()

        row = cell.row
        col = cell.col
        dist = cell.dist

        # If we have reached the destination cell, return the distance
        if row == dest_row and col == dest_col:
            return dist

        # Check all 8 possible directions
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            new_row = row + dx[i]
            new_col = col + dy[i]

            if is_valid(new_row, new_col, n, maze, visited):
                visited[new_row][new_col] = True
                q.append(Cell(new_row, new_col, dist + 1))

    # If destination is not reachable
    return -1

if __name__ == "__main__":
    n = int(input("Enter the size of the maze (n): "))

    maze = []
    print("Enter the maze (1 for open path, 0 for obstacle):")
    for _ in range(n):
        row = list(map(int, input().split()))
        maze.append(row)

    src_row, src_col = map(int, input("Enter source cell (row col): ").split())
    dest_row, dest_col = map(int, input("Enter destination cell (row col): ").split())

    shortest_distance = find_shortest_path(src_row-1, src_col-1, dest_row-1, dest_col-1, n, maze)

    if shortest_distance != -1:
        print(f"Shortest distance from source to destination: {shortest_distance}")
    else:
        print("Destination is not reachable.")
