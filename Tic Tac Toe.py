import os
from colorama import init, Fore, Style

init()
 

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input(
                f"{Fore.BLUE}Enter your name (letters only): {Style.RESET_ALL}"
            )
            if name.isalpha():
                self.name = name
                break
            print(
                f"{Fore.RED}Invalid name. Please enter letters only.{Style.RESET_ALL}"
            )

    def choose_symbol(self):
        while True:
            symbol = input(
                f"{Fore.BLUE}{self.name}, choose your symbol (only single letter): {Style.RESET_ALL}"
            )
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print(
                f"{Fore.RED}Invalid symbol. Please enter a single letter.{Style.RESET_ALL}"
            )


class Menu:
    def display_main_menu(self):
        print(f"{Fore.YELLOW}Welcome to my X-O game!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1- Start Game.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2- Quit Game.{Style.RESET_ALL}")
        choice = input(f"{Fore.BLUE}Enter your choice (1 or 2): {Style.RESET_ALL}")
        return choice

    def display_endgame_menu(self):
        print(f"{Fore.YELLOW}Welcome to my X-O game!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}1- Start Game.{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2- Quit Game.{Style.RESET_ALL}")
        choice = input(f"{Fore.BLUE}Enter your choice (1 or 2): {Style.RESET_ALL}")
        return choice


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print(f"{Fore.MAGENTA}+{'-' * 11}+{Style.RESET_ALL}")
        for i in range(0, 9, 3):
            print(f"{Fore.MAGENTA}| {' | '.join(self.board[i:i+3])} |{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}+{'-' * 11}+{Style.RESET_ALL}")

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
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
        for number, player in enumerate(self.players, start=1):
            print(f"{Fore.YELLOW}Player {number}, enter your details:{Style.RESET_ALL}")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                self.board.display_board()
                if self.check_win():
                    winner = self.players[self.current_player_index]
                    print(
                        f"{Fore.GREEN}{winner.name} ({winner.symbol}) has won the game!{Style.RESET_ALL}"
                    )
                else:
                    print(f"{Fore.YELLOW}It's a draw!{Style.RESET_ALL}")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{Fore.BLUE}{player.name}'s turn ({player.symbol}){Style.RESET_ALL}")
        while True:
            try:
                cell_choice = int(
                    input(f"{Fore.BLUE}Choose a cell (1-9): {Style.RESET_ALL}")
                )
                if 1 <= cell_choice <= 9 and self.board.update_board(
                    cell_choice, player.symbol
                ):
                    break
                else:
                    print(f"{Fore.RED}Invalid move, try again.{Style.RESET_ALL}")
            except ValueError:
                print(
                    f"{Fore.RED}Please enter a number between 1 to 9.{Style.RESET_ALL}"
                )
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        player_symbol = self.players[self.current_player_index].symbol
        for combo in win_combinations:
            if (
                self.board.board[combo[0]] == player_symbol
                and self.board.board[combo[1]] == player_symbol
                and self.board.board[combo[2]] == player_symbol
            ):
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def quit_game(self):
        print(f"{Fore.YELLOW}Thank you for playing!{Style.RESET_ALL}")


game = Game()
game.start_game()
