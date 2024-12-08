
class Player:

    def __init__(self, name, age, piece):
        self.name = name
        self.age = age
        self.piece = piece

    def get_name(self):
        return self.name    
    
    def get_piece_pattern(self):
        return self.piece.get_pattern()
    
    def __str__(self):
        return f'{self.name} ({self.age}) - {self.position}'