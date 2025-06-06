from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #using single list to rep 3x3 borad i.e a list of 9 elements, one for each cell in a 3x3 grid
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)] : # self.board[0:3] -> row1; self.board[3:6]-> row2; self.board[6:9]-> row3
            print(' | ' + ' | '.join(row) + ' | ')
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc. (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' '] # for every index i, if the spot at the index is empty, add 'i' to the list

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if it is a valid move then make the move and return true. If invalid, return false.
        if self.board[square] == ' ' :
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # 3 in a row
        row_ind = square // 3 # // --> discards remainder (eg 0//3 --> 0, 1//3 --> o, 2//3 -->1  => first row)
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all ([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3 # gives the remainder ( eg: 0%3-->0, 3%3-->0, 6%3-->0 => first column)
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True

        #check diagonal (square is an even number (0,2,4,6,8) --> possible moves for a diagonal)
        if square % 2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right diagonal
            if all ([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all ([spot == letter for spot in diagonal2]):
                return True

        # if all fails
        return False

def play(game, x_player, o_player, print_game = True):
    #return the winner of the game or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter;
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to {square}')
                game.print_board()
                print('') #empty line

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!!')
                return letter


            #alternating the letters after making the move
            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
    if print_game:
        print('It\'s a tie!')
    return None

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O') # o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)

