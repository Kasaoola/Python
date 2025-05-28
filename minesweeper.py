import random
import re

class Board: # to initialize the board with given dimensions and bomb count
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board() # to represent how many bombs are in the neighbouring spaces

        # set to keep track of these parameters
        self.dug = set()

    def make_new_board(self): # creating the bomb with bombs placed randomly
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # planting the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # ** -> gives total number of cells in the grid (square: 5**2 -> 25)
            row = loc // self.dim_size # the no. of times dim_size goes into loc
            col = loc % self.dim_size

            if board[row][col] == '*': # plant the bomb
                continue # the bomb has already been planted so keep going

            board [row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self): # for each non-bomb cells, storing how many neighbouring bombs it has
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue # if bomb is already present we don't need to calculate anything
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c) # r corresponds to row and c to col

    def get_num_neighbouring_bombs(self, row, col): # looking at adjacent cells and counting how many bombs are near
        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size -1,row+1)+1): # for current row we are at, checking above and below
            for c in range(max(0,col-1), min(self.dim_size -1,col+1)+1): # for current row checking left and right
                if r == row and c == col: # original location; no need to check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs

    def dig(self, row, col):
        # dig at a location and return true if successful dig else false
        # scenarios:
        # hit a boms --> game over
        # dig at a location with neighbouring bombs --> finish dig (return True)
        # dig at a location with no neighbouring bombs (0) --> recursively dig neighbours
        self.dug.add((row,col)) # keeping track of dug location

        if self.board[row][col] == '*': # if a bomb is dug
            return False
        elif self.board[row][col] > 0: # dug at a location with neighbouring bombs
            return True

        for r in range(max(0,row-1), min(self.dim_size -1, row+1)+1): # not a boms and no neighbouring bombs present
            for c in range(max(0, col-1), min (self.dim_size -1, col+1)+1):
                if (r,c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r,c)
        return True

    def __str__(self):# a magic function : if there is ony call print on this object, it'll print out what this function returns

        # creating an array that the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '


        # preparing to print the board nicely
        # putting this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size): # loop to figure out how wide each column should be
            columns = map(lambda x: x[idx], visible_board) # map() extracts the idx-th item form each roe=w and forms a list of values in that columns
            widths.append(len(max(columns, key = len))) # to find the longest string in the column
        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep



def play(dim_size = 10, num_bombs = 10):
    # creating the board and planting the bombs
    board = Board(dim_size, num_bombs)

    safe = True
    while len(board.dug) < board.dim_size **2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input('Where would you like to dig? Input as row,col: ')) # comma tells the code to detect any available comma and (\\s) tells to detect any whitespaces and * says 0 or more of those
        row, col = int(user_input[0]), int(user_input[-1]) # row is assigned to user input 0 and col to user input -1.
        if row < 0 or row >= board.dim_size or col <0 or col >= board.dim_size:
            print('Invalid location. Try again.')
            continue

        # if it's valid, we dig
        safe = board.dig(row,col)
        if not safe:
            break # game over
    # ways to end loop
    if safe:
        print('Congratulations!! You are victorious.')
    else:
        print('Sorry game over :(')
        #revealing the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)] # taking every possible values of (r,c) and list it in the board
        print(board)

if __name__=='__main__': # if we have a big project and only want to run this file
    play()




