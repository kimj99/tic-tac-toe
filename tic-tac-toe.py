
class Board:
    def __init__(self) -> None:
        self._board = [['*' for _ in range(3)] for _ in range(3)]

    def draw(self):
        for row in self._board:
            print(row)
        
    def get_spot(self, coordinate):
        x,y = coordinate
        if x in range(len(self._board)) or y in range(len(self._board)):
            return self._board[x][y]
        else:
            return 0
    
    def is_valid_move(self, move):
        if move == '*':
            return True 
        return False

    def make_move(self, move, letter):
        spot = self.get_spot(move)
        if self.is_valid_move(spot):
            self._board[move[0]][move[1]] = letter
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
            if board.get_spot(spot) == 0:
                if not board.is_valid_move(board.get_spot(spot)):
                    print("Invalid Move!")
                    print("Try Again")
                    continue
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
                self.p1_turn = False
            else:
                move = self.p2.move(self.board)
                self.board.make_move(move, self.p2.letter)
                self.p1_turn = True
def main():
    game = Game()
    game.start()


main()