import arcade
from connect_n_gui import ConnectNGUI
from player import Player


class ConnectN(ConnectNGUI):
    def on_key_press(self, symbol: int, modifiers: int):
        # KEY_1 = 49
        if not self.game.game_over and (symbol - 49) in self.game.get_legal_moves():
            self.make_move(symbol - 49)

player_1 = Player('Player1')
player_2 = Player('Player2')

n_rows = 3
n_cols = 4
condition = 3

game = ConnectN(player_1, player_2, n_rows, n_cols, condition)
game.setup()
arcade.run()