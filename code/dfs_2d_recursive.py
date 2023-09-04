#!/usr/bin/python3

def dfs(matrix, row, col, visited):
    # Define the possible moves (up, down, left, right)
    rows = [0, 0, -1, 1]
    cols = [-1, 1, 0, 0]
    
    # Mark the current cell as visited
    visited[row][col] = True
    
    # Process the current cell (print its value)
    print(matrix[row][col], end=" ")
    
    # Visit all the unvisited adjacent cells
    for i in range(4):
        newRow, newCol = row + rows[i], col + cols[i]
        
        if (newRow >= 0 and newRow < len(matrix) and
            newCol >= 0 and newCol < len(matrix[0]) and
            not visited[newRow][newCol]):
            dfs(matrix, newRow, newCol, visited)

def printMatrixDFS(matrix):
    # Initialize the visited array
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    # Start the DFS traversal from the top-left cell (0, 0)
    dfs(matrix, 0, 0, visited)
    print()

# Example usage:
# matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#printMatrixDFS(matrix)
