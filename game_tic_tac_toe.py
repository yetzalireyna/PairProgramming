'''
comments
'''
import TicTacToe as game
import math

def play(game, x_player, o_player, print_game=True):
  # return the winner of the game or None for a tie
  if print_game:
    game.print_board_nums()
  letter = 'X'
  
  while game.empty_squares():
    if letter == 'O':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)
    
    if game.make_move(square, letter):
      if print_game:
        print(letter + f' makes a move to square {square}')
        game.print_board()
        print(' ') 
        
      letter = 'O' if letter == 'X' else 'X'
      
  
