import numpy as np


def get_current_state(board: np.ndarray) -> str:
    return str(board.flatten())


def get_row(board: np.ndarray, col: int) -> int:
    return max(np.argwhere(board[:, col] == 0))


def get_policy_path(bot_number, n_rows, n_cols, condition):
    return f'policies/Bot{bot_number}_{n_rows}_{n_cols}_{condition}.pkl'