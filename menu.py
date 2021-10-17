from player import Player, Weak, Normal, Strong


class Menu:
    board_size = 0
    player_one = None
    player_two = None

    available_ai = {
        "weak": Weak,
        "normal": Normal,
        "strong": Strong,
    }

    def __init__(self):
        self.splash()
        self.board_size_set()
        self.game_type()

    def splash(self) -> None:
        """Splash screen"""

        print(
            "===============", "Tic Tac Toe", "By: ArnNied", "===============", sep="\n"
        )

    def pvp(self) -> None:
        self.player_one = Player("X", "Player One")
        self.player_two = Player("O", "Player Two")

    def pve(self):
        available_ai = [strength.title() for strength in self.available_ai.keys()]

        while True:
            ai_strength = input(f"Strength - {' | '.join(available_ai)}? ").lower()
            if ai_strength not in self.available_ai:
                print("Error: AI Not Found")
                continue
            else:
                break

        while True:
            first = input("First turn - Me | AI? ").lower()

            if first == "me":
                self.player_one = Player("X", "Player")
                self.player_two = self.available_ai[ai_strength]("O")
            elif first == "ai":
                self.player_one = self.available_ai[ai_strength]("X")
                self.player_two = Player("O", "Player")
            else:
                print("Error: Invalid Input")
                continue

            break

    def game_type(self):
        """Set the opponent type whether it's another human or an AI"""

        game_type = input("Opponent - PvE | PvP? ").lower()
        if game_type == "pve":
            self.pve()
        elif game_type == "pvp":
            self.pvp()

    def board_size_set(self):
        """Set the board size"""

        board_size = int(input("Board size (x by x)? "))
        self.board_size = board_size

    def start(self) -> tuple:
        return self.board_size, self.player_one, self.player_two
