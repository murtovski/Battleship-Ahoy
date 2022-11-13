from random import randint


class game_board:
    """
    This is where I will store the board characteristics
    Including size and the guesses
    """

    def __init__(self, size, player_ships, enemy_ships, type):
        self.size = size
        self.board = [["." for x in range(size) for y in range(size)]]
        self.player_ships = player_ships
        self.enemy_ships = enemy_ships
        self.enemy_ship_location = []

    def print_player_board(self):
        print('     1 2 3 4 5')
        print('     ------------')
        for row in self.board:
            print(f'{row}    |'.join(row))

    def locations(self, type="enemy"):
        for ind in range(self.enemy_ships):
            self.enemy_ship_location.append(randint(0, (self.size - 1)), randint(0, (self.size - 1)))
        if type == "player":
            board


