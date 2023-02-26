import pyautogui as pg
import numpy as np
import time
'''
This is a Sudoku solver that uses backtracking to solve the puzzle.
Uses pyautoGUI to solve the puzzle and inputs it into any online sudoku game
Author: William Du
Last Modified: 2/26/2023
---------------------------
'''

grid = []
backtracks = 0
#Gets row inputs from the user
def getUserInput():
    ''' 
     """
    Takes in the user input and stores it in a 2D list, then appends it to the grid list.
    
    Returns:
        True if the input is valid, False if the input is invalid.
    """
    '''
    for i in range(1, 10): 
        row = list(input(f'Row {i}: '))
        
        #Do some testing with the list and append to the grid
        if (len(row) != 9): 
            return False
        #Turn the list of characters into a list of ints for later comparisions
        ints = [int(i) for i in row if i.isdigit()]
        
        #Append to the grid 
        grid.append(ints)
    return True
          

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

def solve():
    """
    This function solves the Sudoku grid using backtracking.

    Returns:
        True if the grid is solved, False if the grid is unsolvable.
    """
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

def fillGrid(matrix): 
    ''' 
    Using pyautogui, this function will fill in the grid with the solved puzzle
    '''
    for row in matrix:
        for num in row:
            pg.press(str(num))
            pg.hotkey('right')
        pg.hotkey('left', 'left', 'left', 'left', 'left', 'left', 'left', 'left')
        pg.hotkey('down')
    
    
def main(): 
    ''' 
    Main function that runs the program
    '''
    if getUserInput():
        time.sleep(4)  
        solve()
        if solve():
            for row in grid:
                print(row)
                print(backtracks)
            fillGrid(grid)
        return
    else:
        print("Error with user input!")

main()


#Enter inputs
'''
200000008
700090000
605030000
300000600
008407900
100680000
003200001
050000006
000800040
'''
