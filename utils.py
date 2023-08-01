import numpy as np
import pickle


def get_current_state(board: np.ndarray) -> str:
    return str(board.flatten())


def get_row(board: np.ndarray, col: int) -> int:
    return max(np.argwhere(board[:, col] == 0))


def get_policy_path(bot_number, n_rows, n_cols, condition):
    return f'policies/Bot{bot_number}_{n_rows}_{n_cols}_{condition}.pkl'


def load_policy(bot_number, n_rows, n_cols, condition):
    policy_path = get_policy_path(bot_number, n_rows, n_cols, condition)
    with open(policy_path, 'rb') as f:
        policy = pickle.load(f)
    
    return policy