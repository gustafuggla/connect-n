import arcade
import time
import utils
from connect_n_base import ConnectNBase


class ConnectNGUI(arcade.Window):
    def __init__(self, player_1, player_2, n_rows, n_cols, condition):
        super().__init__(n_cols*100, n_rows*100, f'Connect{condition}')
        self.background_color = (0, 0, 0)

        self.game = ConnectNBase(player_1, player_2, n_rows, n_cols, condition)
        self.tokens = {
            player_1.id: 'sprites/pink.png',
            player_2.id: 'sprites/blue.png'
        }

    def setup(self):
        self.game.setup()
        self.sprite_list = arcade.SpriteList()

    def on_update(self, delta_time: float):
        if not self.game.game_over:
            self.game.check_win_condition()
        else:
            if self.game.winner is not None:
                print(self.game.winner.name)
            else:
                print('Draw')
            time.sleep(2)
            self.setup()

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
    
    def make_move(self, col: int):
        row = utils.get_row(self.game.board, col)
        self.game.board[row, col] = self.game.active_player.marker
        x, y = self.get_token_coordinates(col, row)
        token = arcade.Sprite(self.tokens[self.game.active_player.id], 1)
        token.position = (x, y)
        self.sprite_list.append(token)
        self.game.switch_active_player()

    def get_token_coordinates(self, col, row):
        x = col * 100 + 50
        y = self.game.n_rows * 100 - (row * 100 + 50)

        return x, y
