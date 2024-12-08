from  tictactoestimulator import TicTacToeSimulator

if __name__ == '__main__':
    # Create a new instance of TicTacToeSimulator
    # and start the game
    player1_name = input('Enter player 1 name: ')
    player2_name = input('Enter player 2 name: ')
    t = TicTacToeSimulator(3, player1_name, player2_name)
    t.start_game()
    print('Game over')
