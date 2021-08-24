
class Board:
    def __init__(self) -> None:
        self._board = [['*' for _ in range(3)] for _ in range(3)]

    def draw(self):
        for row in self._board:
            print(row)
        
    def get_spot(self, coordinate):
        x,y = coordinate
        return self._board[x][y]
    
    def is_valid_move(self, move):
        if move == '*':
            return True 
        return False

    def make_move(self, move, letter):
        spot = self.get_spot(move)
        if self.is_valid_move(spot):
            self._board[move[0]][move[1]] = letter
            self.draw()
            return True
        return False


class Player:
    def __init__(self, letter) -> None:
        self.letter = letter
    
    def move(self, board):
        while(True):
            board.draw()
            spot = input(f"Pick a coordinate: ").split(" ")
            spot = (int(spot[0]),int(spot[1]))
            return spot
class Game:
    def __init__(self, p1: Player = Player('X'), p2: Player = Player('O'),board:Board = Board()) -> None:
        self.p1 = p1
        self.p2 = p2
        self.board = board
        self.p1_turn = True

    def start(self):
        while(True):
            if self.p1_turn:
                move = self.p1.move(self.board)
                self.board.make_move(move, self.p1.letter)
            else:
                move = self.p2.move(self.board)
                self.board.make_move(move, self.p2.letter)

def main():
    pass


main()