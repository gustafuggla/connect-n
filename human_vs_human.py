import arcade
from connect_n_gui import ConnectNGUI
from player import Player


class ConnectN(ConnectNGUI):
    def on_key_press(self, symbol: int, modifiers: int):
        if (not self.game.game_over and
                not self.game.active_player.is_bot and
                (symbol - arcade.key.KEY_1) in self.game.get_legal_moves()):
            self.make_move(symbol - arcade.key.KEY_1)
        if (self.game.game_over and symbol == arcade.key.SPACE):
            self.setup()

player_1 = Player('Player1')
player_2 = Player('Player2')

n_rows = 3
n_cols = 4
condition = 3

game = ConnectN(player_1, player_2, n_rows, n_cols, condition)
game.setup()
arcade.run()