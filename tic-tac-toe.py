class Type:
    O = 0
    X = 1
    
class Board:
    def __init__(self) -> None:
        self._board = [['*' for _ in range(3)] for _ in range(3)]

    def draw(self):
        for row in self._board:
            print(row)


def main():
    board = Board()
    board.draw()

main()