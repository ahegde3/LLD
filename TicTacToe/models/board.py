
class Board:


    def __init__(self, size):
        self.size = size
        self.board = [[None for i in range(size)] for j in range(size)]
     

    def get_free_cells(self):
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    free_cells.append((i,j))
        return free_cells
    
    def make_entry(self,piece_pattern,row,col):
        self.board[row][col] = piece_pattern

    def is_valid_move(self,row,col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.board[row][col] != None:
            return False
        return True
    
    def check_winner(self):

        # check row wise
        for i in range(self.size):
            pattern = self.board[i][0]
            if pattern == None:
                break
            winner = True
            for j in range(self.size):
                if self.board[i][j] != pattern:
                    winner = False
                    break
            if winner:
                return True

        # check column wise
        for i in range(self.size):
            pattern = self.board[0][i]
            if pattern == None:
                break
            winner = True
            for j in range(self.size):
                if self.board[j][i] != pattern:
                    winner = False
                    break
            if winner:
                return True

        # check diagonal wise
        pattern = self.board[0][0]
        if pattern == None:
            return False
        winner = True
        for i in range(self.size):
            if self.board[i][i] != pattern:
                winner = False
                break
        
        if winner:
            return True

        return False

        