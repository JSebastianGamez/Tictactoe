# Classic Tic-tac-toe game

"""
topL|topM|topR
--------------
midL|midM|midR
--------------
botL|botM|botR
"""

# Tic-tac-toe grid
grid = {
    'topL': " ", 'topM': " ", 'topR': " ",
    'midL': " ", 'midM': " ", 'midR': " ",
    'botL': " ", 'botM': " ", 'botR': " "
    }

# Function to play the game
def play(grid):
    turn = 'X'
    for i in range (9):
        while True:
            position = input("Player " + turn + ''' enter location:
                topL, topM, topR, midL, midM, midR, botL, botM, botR''')
            if position in grid:
                if grid[position] == " ":
                    grid[position] = turn
                    break
                else:
                    print("This postion has already been taken! \n")
            else:
                print("Invalid position \n")

        printgrid(grid)

        if victory(grid) == True:
            print("Player " + turn + " has won!")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    if victory(grid) == False:
        print("It's a tie")

# Function to print the grid
def printgrid(grid):
    print(grid['topL'] + '|' + grid['topM'] + '|' + grid['topR'])
    print('-----')
    print(grid['midL'] + '|' + grid['midM'] + '|' + grid['midR'])
    print('-----')
    print(grid['botL'] + '|' + grid['botM'] + '|' + grid['botR'])
    print('\n')

# Function to check possible victory
def victory(grid):
    if (  grid['topL'] == grid['topM'] == grid['topR'] != " " # top row
    ) or (grid['midL'] == grid['midM'] == grid['midR'] != " " # middle row
    ) or (grid['botL'] == grid['botM'] == grid['botR'] != " " # bottom row
    ) or (grid['topL'] == grid['midL'] == grid['botL'] != " " # left column
    ) or (grid['topM'] == grid['midM'] == grid['botM'] != " " # middle column
    ) or (grid['topR'] == grid['midR'] == grid['botR'] != " " # right column
    ) or (grid['topL'] == grid['midM'] == grid['botR'] != " " # left diag
    ) or (grid['topR'] == grid['midM'] == grid['botL'] != " " # right diag
    ):
        return True
    else:
        return False

play(grid)
