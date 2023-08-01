import pickle
from connect_n_base import ConnectNBase
from agent_q import AgentQ
import utils


bot_1 = AgentQ('Bot1')
bot_2 = AgentQ('Bot2')

n_rows = 3
n_cols = 4
condition = 3

game = ConnectNBase(bot_1, bot_2, n_rows, n_cols, condition)
game.setup()

for n in range(1000):
    if n % 1000 == 0:
            print(n)
    while True:
        if not game.game_over:
            game.make_move(
                game.active_player.get_move(game.board.copy(), game.get_legal_moves())
                )
            game.check_win_condition()
        else:
            if game.winner is not None:
                game.winner.give_reward(1)
                game.loser.give_reward(-1)
            else:
                game.player_1.give_reward(0)
                game.player_2.give_reward(0)
            game.setup()
            break

for bot, bot_number in zip([bot_1, bot_2], [1, 2]):
    with open(utils.get_policy_path(bot_number, n_rows, n_cols, condition), 'wb') as f:
        pickle.dump(bot.q_table, f)
