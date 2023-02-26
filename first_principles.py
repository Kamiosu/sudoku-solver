'''
This is a Sudoku solver that uses backtracking to solve the puzzle.
Uses pyautoGUI to solve the puzzle 
Author: William Du
'''

# Define the initial Sudoku grid global variable
grid = [[0, 4, 0, 0, 0, 8, 0, 6, 7], 
        [9, 6, 0, 0, 4, 2, 0, 5, 0],
        [0, 5, 0, 1, 0, 0, 4, 2, 0],
        [5, 1, 2, 0, 9, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 2, 0, 1, 4, 5],
        [0, 8, 5, 0, 0, 1, 0, 7, 0],
        [0, 2, 0, 4, 3, 0, 0, 8, 6],
        [6, 7, 0, 5, 0, 0, 0, 1, 0]]

backtracks = 0

# Define a function to check if a number is possible in a given position
def isValid(row, col, n):
    # Check if the number is possible in a row
    if n in grid[row]:
        return False
        
    # Check if the number is possible in a column
    for i in range(0, 9):
        if grid[i][col] == n:
            return False
        
    # Check if the number is possible in a 3x3 box
    # Find the top left corner of the box
    x = (col // 3) * 3
    y = (row // 3) * 3
    
    for i in range(0, 3): 
        for j in range(0, 3): 
            if grid[y+i][x+j] == n: 
                return False
    
    return True

# Define a function to solve the Sudoku grid
def solve():
    global grid
    global backtracks
    # Find the next empty cell
    for row in range(0, 9):
        for col in range(0, 9):
            
            if grid[row][col] == 0:
                # Try filling in each number from 1-9
                for n in range(1, 10):
                    if isValid(row, col, n):
                        # Fill in the number and recursively call solve()
                        grid[row][col] = n
                        if solve():
                            backtracks += 1 
                            return True
                        grid[row][col] = 0
                # If none of the numbers work, backtrack
                return False
    # If no empty cells remain, the Sudoku is solved
    return True

# Call the solve() function and print the solution
if solve():
    for row in grid:
        print(row)
    print(backtracks)
else:
    print("No solution exists.")
