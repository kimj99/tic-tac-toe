import math
from enum import Enum

class Types(Enum):
    X = 1
    O = 2


class Board:
    def __init__(self) -> None:
        self._board = [['*' for _ in range(3] for _ in range(3)]
        #self._board = [['X','*','O'],['*','X','X'],['*','*','O']]


    def draw(self):
        for row in self._board:
            print(row)
        
    def get_spot(self, coordinate):
        x,y = coordinate

        if x < len(self._board) and y < len(self._board):
            return self._board[x][y]
        else:
            return 0
    
    def is_valid_move(self, spot):
        if spot == '*':
            return True 
        return False

    def make_move(self, move, letter):
        x,y = move
        spot = self.get_spot(move)
        if self.is_valid_move(spot):
            self._board[x][y] = letter.name
            return True
        return False

    def reset_move(self, move):
        x,y = move
        self._board[x][y] = '*'
        return True

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
        if self.num_spaces() == 0:
            return 0
        return None

    def num_spaces(self):
        count = 9
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == '*':
                    count -= 1
        return count

    def available_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == '*':
                    moves.append((i,j))
        return moves
    
    def get_current_state(self):
        copy = self
        
        return copy
class Player:
    def __init__(self, letter: Types) -> None:
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
    def __init__(self, letter, other_letter) -> None:
        super().__init__(letter)
        self.other_letter = other_letter
    
    def move(self, board):
        board.draw()
        print("AI Move: ",self.letter)
        best_score = -math.inf
        possible_state = board.get_current_state()

        for i,j in possible_state.available_moves():
            possible_state.make_move((i,j),self.letter)
            score = self.minmax(possible_state,True)
            possible_state.reset_move((i,j))
            if score > best_score:
                best_score = score
                best_spot = (i,j)
        print(f"chosen spot: {best_spot} with a score of {best_score}")
        return best_spot


    def minmax(self, board, max_player):
        winner = board.check_victory()

        board.draw()
        if winner: 
            if winner == self.letter:
                return 1 * board.num_spaces() + 10
            if winner == self.other_letter:
                return -1 * board.num_spaces() + 10
            if winner == 0:
                return 0
        
        if max_player:
            max_eval = -math.inf
            for move in board.available_moves():
                board.make_move(move,self.letter)
                eval = self.minmax(board, False)
                board.draw()

                board.reset_move(move)
                max_eval = max(max_eval,eval)
            return max_eval
        else:
            min_eval = math.inf
            for move in board.available_moves():
                board.make_move(move,self.other_letter)
                eval = self.minmax(board, True)
                board.reset_move(move)
                min_eval = min(min_eval, eval)
            return min_eval



class Game:
    def __init__(self,board:Board = Board()) -> None:
        self.p2 = Player(Types.O)
        self.p1 = AI(Types.X, self.p2.letter)
        self.board = board
        self.p1_turn = True

    def start(self):
        moves = 0
        while(True):
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