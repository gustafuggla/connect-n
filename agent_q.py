from collections import defaultdict
import numpy as np
from player import Player
import utils


class AgentQ(Player):
    def __init__(self, name, is_training=True, policy=None, 
                 learning_rate=0.1, gamma=0.9, epsilon=0.7):
        super().__init__(name)
        self.is_bot=True
        self.is_training = is_training
        self.visited_states = []
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon

        if policy is None:
            self.q_table = defaultdict(int)
        else:
            self.q_table = policy

    def get_move(self, board: np.ndarray, legal_moves: list[int]):
        if self.is_training:
            pre_move_game_state = utils.get_current_state(board)
            self.visited_states.append(pre_move_game_state)
        
        max_value = -np.inf
        if np.random.uniform(0, 1) < self.epsilon:
            for candidate_col in legal_moves:
                temp_board = board.copy()
                candidate_row = utils.get_row(temp_board, candidate_col)
                temp_board[candidate_row, candidate_col] = self.marker
                candidate_game_state = utils.get_current_state(temp_board)
                candidate_value = self.q_table[candidate_game_state]

                if candidate_value > max_value:
                    max_value = candidate_value
                    col = candidate_col
        else:
            col = np.random.choice(legal_moves)

        if self.is_training:
            row = utils.get_row(board, col)
            board[row, col] = self.marker
            post_move_game_state = utils.get_current_state(board)
            self.visited_states.append(post_move_game_state)
        
        return col
    
    def give_reward(self, reward):
        for game_state in reversed(self.visited_states):
            self.q_table[game_state] += self.learning_rate * \
                (self.gamma * reward - self.q_table[game_state])
            
            reward = self.q_table[game_state]
        
        self.visited_states = []