import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

        #for players to get their next move
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False # a flag to control the loop. set to False so that the user keeps getting prompted  until they input a valid move
        val = None # stores the converted integer value of the user's input once its valid
        while not valid_square: #while valid_square is false (loop continues until the user provides a vaiid input)
            square = input(f'{self.letter} \'s turn. Input move (0-8): ') # x or o,s turn
            # checking if the input number is valid
            try:
                val = int(square) # square is the input by the user. If the input cannot be cast into an integer (eg:x,y,z), it's gonna raise an error
                if val not in game.available_moves(): #if value is not available in the game.available_moves
                    raise ValueError
                valid_square = True #if val is in game.available_moves(), true is passed
            except ValueError:
                print('Invalid square.Try again')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9: # if all the spaces are available
            square = random.choice(game.available_moves())
        else:
            #get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X'

        # checking if the previous move is a winner
        # Base Case
        if state.current_winner == other_player:
            # returning position and score because we need to keep track of the score for minimax to work
            # if the last move leads to a win by the opponent, return a negative score and if it's a draw , return score = 0 and it the player wins return a positive score
            # GeniusComputerProgram is the maximizer as it tries to get the highest score possible
            # human is the minimizer: who tries to get the maximizer to get the lowest score
            return {'position': None, 'score': 1* (state.num_empty_square() +1) if other_player == max_player else -1* (state.num_empty_square() + 1)}

        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}


        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}#each score should minimize
        for possible_move in state.available_moves():
            # making a move and try that spot
            state.make_move(possible_move, player)

            # recurse using minimax to stimulate a game after making that move
            sim_score = self.minimax(state, other_player) # then we alternate players

            # undo the move
            state.board[possible_move] = ' ' # resetting it to an empty space
            state.current_winner = None
            sim_score['position'] = possible_move # setting what position we just moved to

            # updating dictionaries
            if player == max_player: # maximizing the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else :
                if sim_score['score'] < best['score']:
                        best = sim_score

        return best




