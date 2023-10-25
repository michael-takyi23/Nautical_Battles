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
                guess_input = input("Enter your guess(row col):\n ")
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


# Game class represents the main game logic.
class Game:
    def __init__(self, grid_size, num_ships):
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.player_board = Board(grid_size)
        self.computer_board = Board(grid_size)
        player_name = input("Please enter your name:\n ")
        self.player = Player(player_name, self.player_board)
        self.computer = ComputerPlayer(self.computer_board, grid_size)

    def play(self):
        """Main game loop."""
        self.player_board.place_ships(self.num_ships)
        self.computer_board.place_ships(self.num_ships)
        while (self.player.score < self.num_ships and
               self.computer.score < self.num_ships):
            self.display_boards()
            self.player_turn()
            self.computer_turn()
        self.end_game()

    def display_boards(self):
        """Display both player's and computer's boards."""
        print(f"\n{self.player.name}'s Board (B represents your ships):")
        self.player.board.display()
        print("\nComputer's Board:")
        self.computer.board.display(hide_ships=True)

    def player_turn(self):
        """Handle the player's turn."""
        row, col = self.player.make_guess()
        if self.computer.board.grid[row][col] == 'B':
            print("Congratulations! You hit a battleship!")
            self.player.score += 1
            self.computer.board.grid[row][col] = 'H'
        else:
            print("Sorry, it's a miss.")
            self.computer.board.grid[row][col] = 'M'
        self.display_scores()

    def computer_turn(self):
        """Handle the computer's turn."""
        row, col = self.computer.make_guess()
        print(f"Computer guessed ({row}, {col}).")
        if self.player.board.grid[row][col] == 'B':
            print("Computer hit one of your ships!")
            self.computer.score += 1
            self.player.board.grid[row][col] = 'H'
        else:
            print("Computer missed.")
            self.player.board.grid[row][col] = 'M'
        self.display_scores()

    def display_scores(self):
        """Display current scores for both player and computer."""
        print(f"{self.player.name}'s Score: {self.player.score}")
        print(f"{self.computer.name}'s Score: {self.computer.score}")
        print("."*35)

    def end_game(self):
        """Display the end game message based on who won."""
        print("\nGame Over!")
        if self.player.score == self.num_ships:
            print(f"Congratulations, {self.player.name}! You sank all of the "
                  f"computer's battleships.")
        else:
            print("Too bad, the computer sank all of your battleships.")


if __name__ == "__main__":
    game = Game(grid_size=8, num_ships=6)
    game.play()
    while True:
        play_again = input("Would you like to play again? (y/n):\n").lower()
        if play_again != 'y':
            break
        game = Game(grid_size=8, num_ships=6)
        game.play()