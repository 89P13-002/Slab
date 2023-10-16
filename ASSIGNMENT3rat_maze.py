# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:55:26 2023

@author: 91635
"""
# importing deque 
from collections import deque

# a structur to reprent each cell/palce of matrix
class Cell:
    def __init__(self, row_pos, col_pos, distance):
        self.row_pos = row_pos
        self.col_pos = col_pos
        self.distance = distance
        self.parent = None

# Function to check a place is valid or not to move
def check_valid(row, col, n, maze, visited):
    return (row >= 0 and col >= 0 and row < n and col < n and maze[row][col] == 0 and not visited[row][col])
    # checking that row and column number are within range , palce is valid to move (i.e 0) and not visited earlier

# Function to find shortest path by using BFS technique(i.e check all the neighbour of a cell if it turn out to be valid then push it in deque and if it not valid then don't push it  )
# Sarting from the source applying above algorithm and pop , push untill reach destination or (checking by line 40 )
# if deque become empty but we not reach destination then it is not reachable 
def to_get_shortest_path(src_row, src_col, dest_row, dest_col, n, maze):
    visited = [[False for _ in range(n)] for _ in range(n)] # creating a 2-D list to keep track of single visited or not (initialising all the place as False)
    q = deque() #  creates an empty double-ended queue

    # Mark the source cell as visited
    visited[src_row][src_col] = True # making place visited in 2-D array
    q.append(Cell(src_row, src_col, 0)) #pushing this cell to deque
# loop either rech destination or deque become empty
    while q:
        cell = q.popleft()
        row = cell.row_pos
        col = cell.col_pos
        dist = cell.distance

        # If we have reached the destination cell, return the distance
        if row == dest_row and col == dest_col: # check reached destination or not
            path = []  # initializing an empty list to keep track of the path taken
            current = cell # assigns val of cell to varaiable current
            # To backtrack from destination to source 
            while current is not None:
                path.append((current.row_pos+1,current.col_pos+1))
                current = current.parent
            return dist, path[::-1]  # Return distance and path in reverse order

        # Check all 8 possible directions
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            new_row = row + dx[i]
            new_col = col + dy[i]

            if check_valid(new_row, new_col, n, maze, visited): # check valid to move or not
                visited[new_row][new_col] = True
                new_cell = Cell(new_row, new_col, dist + 1)
                new_cell.parent = cell  # Set the parent cell
                q.append(new_cell)

    # If destination is not reachable
    return -1, []

if __name__ == "__main__":
    n = int(input("Enter the size of the maze (n): "))

    maze = []
    print("Enter the maze (0 for open path, 1 for obstacle):")
    for _ in range(n):
        row = list(map(int, input().split()))
        maze.append(row)

    src_row, src_col = map(int, input("Enter source cell (row col): ").split())
    dest_row, dest_col = map(int, input("Enter destination cell (row col): ").split())

    shortest_distance, path = to_get_shortest_path(src_row-1, src_col-1, dest_row-1, dest_col-1, n, maze)
# check destination reachable or not
    if shortest_distance != -1: # if reachable
        print(f"Shortest distance from source to destination: {shortest_distance}")
        print(f"Path taken: {path}")
    else:
        print("Destination is not reachable.")
