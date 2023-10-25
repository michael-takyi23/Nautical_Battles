import random

class Board:
    def __init__(self, size):
        # Initialize a grid with 'O' which represents water/empty space.
        self.grid = [['O' for _ in range(size)] for _ in range(size)]
        self.size = size

    def display(self, hide_ships=False):
        """Display the board. If hide_ships is True, ships are hidden."""
        for row in self.grid:
            for cell in row:
                if hide_ships and cell == 'B':
                    print('.', end=' ')
                else:
                    print(cell, end=' ')
            print()

    def place_ships(self, num_ships):
        """Place a given number of ships randomly on the board."""
        for _ in range(num_ships):
            while True:
                rows = random.randint(0, self.size - 1)
                cols = random.randint(0, self.size - 1)
                if self.grid[rows][cols] == 'O':
                    self.grid[rows][cols] = 'B'
                    break

    def valid_guess(self, row, col):
        """Check if a given guess is within the board boundaries."""
        return 0 <= row < self.size and 0 <= col < self.size


# Player class represents a human player in the game.
class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.score = 0

    def make_guess(self):
        """Allow the player to make a guess on the opponent's board."""
        while True:
            try:
                guess_input = input("Enter your guess(row col): ")
                row, col = map(int, guess_input.split())
                if self.board.valid_guess(row, col):
                    return row, col
                else:
                    print("Invalid guess. Try again.")
            except ValueError:
                print("Invalid input. Enter your guess as 'row column'.")


# ComputerPlayer class represents the computer opponent.
class ComputerPlayer:
    def __init__(self, board, grid_size):
        self.name = "Computer"
        self.board = board
        self.grid_size = grid_size
        self.score = 0

    def make_guess(self):
        """Computer makes a random guess on the opponent's board."""
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if self.board.grid[row][col] not in ('H', 'M'):
                return row, col



if __name__ == "__main__":