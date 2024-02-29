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
        """
        constructor method with appropriate initialization of instance variables
        Board is a rudimentary (nested list) 2d array of 0s, 1s, and 2s to indicate the
        occupant of cells on the board
        """
        self.w = w
        self.h = h
        self.streak = streak
        if board == None:
            self.board = [[0 for j in range(self.w)] for i in range(self.w)]
        else:
            self.board = board

    def display(self, do_ascii=False) -> None:
        """displays the gameboard"""
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

    def get_occupant(self, r: int, c: int) -> int:
        """to return a "0", "1" or "2" indicating which player ("0" if space is empty) occupies the current r (row) and c (column) location. r is the row (0 at top) c is the column (0 at left)"""
        return self.board[r][c]

    def add_piece(self, c: int, p: int) -> bool:
        # to return True if successful for adding a p (player "1" or "2") piece to c
        # (column) location. False otherwise
        # c is the column (0 at left)
        # p is the player (1 or 2)
        didplace = False
        for i in range(self.h):
            if self.board[(self.h - i - 1)][c] == 0:
                self.board[(self.h - i - 1)][c] = p
                didplace = True
                break
        return didplace

    def game_over(self) -> int:
        # to return a "0", "1", "2", or "3" indicating which player has won ("0" if no one one,
        # "3" if no more room on board).
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
        """
        Returns True or False if player (p) has won.
        p is the player (1 or 2)
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


# ------ main function ------


def main():
    print("You implement the gameplay yourself! :)")


# ------ executable section ------
if __name__ == "__main__":
    main()
