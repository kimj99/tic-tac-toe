import math
class Board:
    def __init__(self) -> None:
        self._board = [['*' for _ in range(3)] for _ in range(3)]

    def draw(self):
        for row in self._board:
            print(row)
        
    def get_spot(self, coordinate):
        x,y = coordinate

        if x < len(self._board) and y < len(self._board):
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

    def check_victory(self):
        for row in self._board:
            if len(set(row)) == 1 and row[0] != '*':
                return row[0]
        for col in zip(*self._board):
            if len(set(col)) == 1 and col[0] != '*':
                return col[0]
        if self._board[0][0] == self._board[1][1] == self._board[2][2] or self._board[0][2] == self._board[1][1] == self._board[2][0]:
            if self._board[1][1] != '*':
                return self._board[1][1]

        return None
    def num_spaces(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == '*':
                    count += 1
        return count


class Player:
    def __init__(self, letter) -> None:
        self.letter = letter

    def move(self, board):
        while(True):
            board.draw()
            spot = input(f"Pick a coordinate: ").split(" ")
            try:
                spot = (int(spot[0]),int(spot[1]))
            except ValueError:
                print("Invalid input! ")
                continue
            if board.get_spot(spot) == 0 or not board.is_valid_move(board.get_spot(spot)):
                print("Invalid Move!")
                print("Try Again")
                continue
            return spot

class AI(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    
    def move(self, board):
        pass
    def minmax(self, board, max_player):
        winner = board.check_victory()
        if winner:
            if winner == 'O':
                return -1 * board.num_spaces() + 1
            else:
                return 1 * board.num_spaces() + 1
        if max_player:
            max_eval = -math.inf



class Game:
    def __init__(self, p1: Player = Player('X'), p2: Player = Player('O'),board:Board = Board()) -> None:
        self.p1 = p1
        self.p2 = AI('O')
        self.board = board
        self.p1_turn = True

    def start(self):
        moves = 0
        while(True):
            print(moves)
            if moves == 9:
                print("Its a tie!")
                break
            if self.p1_turn:
                move = self.p1.move(self.board)
                self.board.make_move(move, self.p1.letter)
                self.p1_turn = False
            else:
                move = self.p2.move(self.board)
                self.board.make_move(move, self.p2.letter)
                self.p1_turn = True
            winner = self.board.check_victory()
            if winner:
                print(f"Winner is {winner}")
                self.board.draw()
                break
            moves += 1
def main():
    game = Game()
    game.start()


main()