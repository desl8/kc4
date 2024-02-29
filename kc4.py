"""
A simple Connect 4 Gameboard class with full playability features

author: desl8
date: spring 2024
version: python 3.10.8
"""

# ------ import section ------

import copy

# ------ functions section ------

# ------ class section ------


class GameBoard:
    """A class for a Connect Four Gameboard"""

    def __init__(self, w=7, h=6, streak=4, board=None) -> None:
        """The initialization of the gameboard class
        All default values match those of a typical Connect Four board

        Args:
            w (int, optional): The width of the board. Defaults to 7.
            h (int, optional): The height of the board. Defaults to 6.
            streak (int, optional): The streak required to win the game. Defaults to 4.
            board (_type_, optional): A preexisting game board (integer array), if there is any. Defaults to None.
        """
        self.w = w
        self.h = h
        self.streak = streak
        if board == None:
            self.board = [[0 for j in range(self.w)] for i in range(self.w)]
        else:
            self.board = board

    def display(self, do_ascii=False) -> None:
        """Prints the gameboard to the terminal

        Args:
            do_ascii (bool, optional): Whether to return a stylized version of the board rather than the default number array. Defaults to False.
        """
        if do_ascii:
            asciiboard = copy.deepcopy(self.board)
            for i in range(self.h):
                for j in range(self.w):
                    if asciiboard[i][j] == 0:
                        asciiboard[i][j] = " "
                    if asciiboard[i][j] == 1:
                        asciiboard[i][j] = "●"
                    if asciiboard[i][j] == 2:
                        asciiboard[i][j] = "○"
            for i in range(self.h):
                print(asciiboard[i])
        else:
            for i in range(self.h):
                print(self.board[i])

    def get_occupant(self, coords: tuple) -> int:
        """Returns the current occupant of a cell

        Args:
            coords (tuple): The row-column coordinates of the cell

        Returns:
            int: The current occupant (0 for no occupant, 1 for P1, 2 for P2)
        """
        return self.board[coords[0]][coords[1]]

    def get_dims(self) -> tuple:
        """Returns the dimensions of the board

        Returns:
            tuple: (height, width) of the board
        """
        return (self.h, self.w)

    def get_board(self, do_ascii=False) -> list:
        """Returns the simple board object in its list form

        Args:
            do_ascii (bool, optional): Whether to return a stylized version of the board rather than the default number array. Defaults to False.

        Returns:
            list: The board object in its array form
        """
        if do_ascii:
            asciiboard = copy.deepcopy(self.board)
            for i in range(self.h):
                for j in range(self.w):
                    if asciiboard[i][j] == 0:
                        asciiboard[i][j] = " "
                    if asciiboard[i][j] == 1:
                        asciiboard[i][j] = "●"
                    if asciiboard[i][j] == 2:
                        asciiboard[i][j] = "○"
            return asciiboard
        else:
            return self.board

    def add_piece(self, c: int, p: int) -> bool:
        """Returns true if piece is placed successfully, false otherwise

        Args:
            c (int): The column to place in
            p (int): The player who is placing a piece

        Returns:
            bool: Whether the piece was placed or not
        """
        for i in range(self.h):
            if self.board[(self.h - i - 1)][c] == 0:
                self.board[(self.h - i - 1)][c] = p
                return True
        return False

    def game_over(self) -> int:
        """Returns whether the game is over and in what state

        Returns:
            int: 0 for not over, 1 for P1 won, 2 for P2 won, 3 for tie
        """
        if self.is_winner(1):
            return 1
        else:
            if self.is_winner(2):
                return 2
            else:
                isfull = True
                for i in range(self.h):
                    for j in range(self.w):
                        if self.board[i][j] == 0:
                            isfull = False
                if isfull:
                    return 3
                else:
                    return 0

    def is_winner(self, p: int) -> bool:
        """Returns true or false based on whether the player has won

        Args:
            p (int): Player 1 or 2

        Returns:
            bool: Whether the player has won or not
        """
        # Horizontal
        for i in range(self.h):
            for j in range(self.w - (self.streak - 1)):  # Only check up to a certain x
                # coordinate because subsequent "streaks" would wrap around the board
                if self.board[i][j] == p:
                    checkstate = True
                    for k in range(self.streak - 1):
                        if not self.board[i][j + k + 1] == p:
                            checkstate = False
                    if checkstate:
                        return True
        # Vertical
        for i in range(self.h - (self.streak - 1)):  # Same property applied vertically
            for j in range(self.w):
                if self.board[i][j] == p:
                    checkstate = True
                    for k in range(self.streak - 1):
                        if not self.board[i + k + 1][j] == p:
                            checkstate = False
                    if checkstate:
                        return True
        # ↓→ Diagonal
        for i in range(self.h - (self.streak - 1)):
            for j in range(self.w - (self.streak - 1)):
                if self.board[i][j] == p:
                    checkstate = True
                    for k in range(self.streak - 1):
                        if not self.board[i + k + 1][j + k + 1] == p:
                            checkstate = False
                    if checkstate:
                        return True
        # ↑→ Diagonal
        for i in range(self.h - (self.streak - 1)):
            for j in range(self.w - (self.streak - 1)):
                if self.board[i + (self.streak - 1)][j] == p:
                    checkstate = True
                    for k in range(self.streak - 1):
                        if (
                            not self.board[i - k + (self.streak - 1) - 1][j + k + 1]
                            == p
                        ):
                            checkstate = False
                    if checkstate:
                        return True
        return False

    def get_next_player(self) -> int:
        """Returns a 1 or a 2 based on which player should go next

        Returns:
            int: Which player is going next
        """
        counts = [0, 0]  # How many pieces each player has on the board
        for i in range(self.h):
            for j in range(self.w):
                if (
                    occ := self.get_occupant((i, j))
                ) > 0:  # I used the walrus operator Shayan! Are you proud of me?
                    counts[occ - 1] += 1
        return counts.index(min(counts))


# ------ main function ------


def main():
    print("You implement the gameplay yourself! :)")


# ------ executable section ------
if __name__ == "__main__":
    main()
