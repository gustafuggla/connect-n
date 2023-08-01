import numpy as np
import utils


class ConnectNBase:
    def __init__(self, player_1, player_2, n_rows, n_cols, condition):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1.marker = 1
        self.player_2.marker = -1
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.condition = condition
    
    def setup(self):
        self.board = np.zeros((self.n_rows, self.n_cols), dtype='int')
        self.active_player = self.player_1
        self.game_over = False
        self.winner = None
        self.loser = None
        self.winning_moves = None
    
    def get_legal_moves(self):
        return np.argwhere(self.board[0, :] == 0).flatten()
    
    def make_move(self, col: int):
        row = utils.get_row(self.board, col)
        self.board[row, col] = self.active_player.marker
        self.switch_active_player()
    
    def switch_active_player(self):
        if self.active_player == self.player_1:
            self.active_player = self.player_2
        else:
            self.active_player = self.player_1
    
    def check_win_condition(self):
        # Rows
        for row in range(self.n_rows):
            for col in range(self.n_cols - self.condition + 1):
                if np.sum(self.board[row, col:col+self.condition]) == self.condition:
                    self.winner = self.player_1
                    self.loser = self.player_2
                    self.winning_moves = [(row, col+i) for i in range(self.condition)]
                elif np.sum(self.board[row, col:col+self.condition]) == -self.condition:
                    self.winner = self.player_2
                    self.loser = self.player_1
                    self.winning_moves = [(row, col+i) for i in range(self.condition)]

        # Cols
        for row in range(self.n_rows - self.condition + 1):
            for col in range(self.n_cols):
                if np.sum(self.board[row:row+self.condition, col]) == self.condition:
                    self.winner = self.player_1
                    self.loser = self.player_2
                    self.winning_moves = [(row+i, col) for i in range(self.condition)]
                elif np.sum(self.board[row:row+self.condition, col]) == -self.condition:
                    self.winner = self.player_2
                    self.loser = self.player_1
                    self.winning_moves = [(row+i, col) for i in range(self.condition)]

        # Diagonals \
        for row in range(self.n_rows - self.condition + 1):
            for col in range(self.n_cols - self.condition + 1):
                diag = [self.board[row+i, col+i] for i in range(self.condition)]

                if np.sum(diag) == self.condition:
                    self.winner = self.player_1
                    self.loser = self.player_2
                    self.winning_moves = [(row+i, col+i) for i in range(self.condition)]
                elif np.sum(diag) == -self.condition:
                    self.winner = self.player_2
                    self.loser = self.player_1
                    self.winning_moves = [(row+i, col+i) for i in range(self.condition)]
        
        # Diagonals /
        for row in range(self.condition - 1, self.n_rows):
            for col in range(self.n_cols - self.condition + 1):
                diag = [self.board[row-i, col+i] for i in range(self.condition)]

                if np.sum(diag) == self.condition:
                    self.winner = self.player_1
                    self.loser = self.player_2
                    self.winning_moves = [(row-i, col+i) for i in range(self.condition)]
                elif np.sum(diag) == -self.condition:
                    self.winner = self.player_2
                    self.loser = self.player_1
                    self.winning_moves = [(row-i, col+i) for i in range(self.condition)]
        
        if self.winner is not None:
            self.game_over = True
        elif self.get_legal_moves().size == 0:
            self.game_over = True