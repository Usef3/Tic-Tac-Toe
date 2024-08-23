import os
def clear_screen():
    os.system("cls")
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
 
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only) : ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please enter letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name} , choose your sembol (only single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please enter a single letter .")


class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O game ! ")
        print("1- Start Game .")
        print("2- Quit Game .")
        choice = input("Enter your choice (1 or 2) : ")
        return choice

    def desplay_endgame_menu(self):
        print("Welcome to my X-O game ! ")
        print("1- Start Game .")
        print("2- Quit Game .")
        choice = input("Enter your choice (1 or 2) : ")
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def desplay_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i : i + 3]))
            if i < 6:
                print("-" * 5)

    def update_board(self, choice, symbol):
        if self.isvalid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def isvalid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):

        for numper, player in enumerate(self.players,start=1):
            print(f"Player {numper},enter your details :")
            player.choose_name()
            player.choose_symbol()
            # clear_screen()

    def play_game():
        pass

    def quit_game():
        pass


game = Game()
game.start_game()
