import time
import pickle
import arcade
from connect_n_gui import ConnectNGUI
from player import Player
from agent_q import AgentQ
import utils


class ConnectN(ConnectNGUI):
    def __init__(self, player_1, player_2, n_rows, n_cols, condition):
        super().__init__(player_1, player_2, n_rows, n_cols, condition)
        self.elapsed_time = 0
        self.wait_time = 0.3

    def on_update(self, delta_time: float):
        if not self.game.game_over:
            if self.game.active_player.is_bot:
                self.elapsed_time += delta_time
                if self.elapsed_time > self.wait_time:
                    move = self.game.active_player.get_move(
                        self.game.board.copy(),
                        self.game.get_legal_moves()
                    )
                    self.make_move(move)
                    self.elapsed_time = 0
            self.game.check_win_condition()
        else:
            if self.game.winner is not None:
                print(self.game.winner.name)
            else:
                print('Draw')
            time.sleep(2)
            self.setup()

    def on_key_press(self, symbol: int, modifiers: int):
        # KEY_1 = 49
        if (not self.game.game_over and
                not self.game.active_player.is_bot and
                (symbol - 49) in self.game.get_legal_moves()):
            self.make_move(symbol - 49)

player = Player('Player')

n_rows = 3
n_cols = 4
condition = 3

with open(utils.get_policy_path(2, n_rows, n_cols, condition), 'rb') as f:
    policy_2 = pickle.load(f)

bot = AgentQ('Bot', is_training=False, policy=policy_2, epsilon=1)

game = ConnectN(player, bot, n_rows, n_cols, condition)
game.setup()
arcade.run()