from models.board import Board
from models.player import Player
from models.piece import Piece

class TicTacToeSimulator:

    def __init__(self,size,player_name,player_name2):
        self.board = Board(size)
        self.player1 = Player(player_name, 20, Piece('X'))
        self.player2 = Player(player_name2, 20, Piece('O'))
        self.turn = False


    def players_turn(self):
        self.turn = not  self.turn
        if self.turn:
            return self.player1
        else:
            return self.player2    

    def start_game(self):
        print('Game started')
        
        while True:

            free_cells = self.board.get_free_cells()
            if(len(free_cells) == 0):
                print('Tie')
                return
            print(free_cells)

            player = self.players_turn()

            row,col  = map(int,input(f'Enter row, col seperated by space by {player.get_name()}:').split())
            
            while not self.board.is_valid_move(row,col):
                row,col  = map(int,input(f'Enter valid row, col seperated by space by {player.get_name()}:').split())

            self.board.make_entry(player.get_piece_pattern(),row,col)

            if self.board.check_winner():
                print(f'{player.get_name()} wins')
                return


