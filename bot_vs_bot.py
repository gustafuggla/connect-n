import arcade
import time
import pickle
from connect_n_gui import ConnectNGUI
from agent_q import AgentQ
import utils


class ConnectN(ConnectNGUI):
    def __init__(self, player_1, player_2, n_rows, n_cols, condition):
        super().__init__(player_1, player_2, n_rows, n_cols, condition)
        self.elapsed_time = 0
        self.wait_time = 0.3

    def on_update(self, delta_time: float):
        if not self.game.game_over:
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

n_rows = 3
n_cols = 4
condition = 3

with open(utils.get_policy_path(1, n_rows, n_cols, condition), 'rb') as f:
    policy_1 = pickle.load(f)
with open(utils.get_policy_path(2, n_rows, n_cols, condition), 'rb') as f:
    policy_2 = pickle.load(f)

bot_1 = AgentQ('Bot1', is_training=False, policy=policy_1, epsilon=0.7)
bot_2 = AgentQ('Bot2', is_training=False, policy=policy_2, epsilon=0.7)

game = ConnectN(bot_1, bot_2, n_rows, n_cols, condition)
game.setup()
arcade.run()