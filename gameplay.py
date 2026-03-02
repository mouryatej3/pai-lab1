class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-----")

    def is_winner(self, player):
        win_positions = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # columns
            [0,4,8],[2,4,6]           # diagonals
        ]
        return any(all(self.board[i] == player for i in combo)
                   for combo in win_positions)

    def is_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_full()

    def get_available_moves(self):
        return [i for i, v in enumerate(self.board) if v == ' ']

    def make_move(self, move):
        self.board[move] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, move):
        self.board[move] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'


def minimax(board, maximizing_player, ai_player):
    opponent = 'O' if ai_player == 'X' else 'X'

    if board.is_game_over():
        if board.is_winner(ai_player):
            return 1
        elif board.is_winner(opponent):
            return -1
        else:
            return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, False, ai_player)
            board.undo_move(move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, True, ai_player)
            board.undo_move(move)
            min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(board):
    ai_player = board.current_player
    best_move = None
    best_eval = float('-inf')

    for move in board.get_available_moves():
        board.make_move(move)
        eval = minimax(board, False, ai_player)
        board.undo_move(move)

        if eval > best_eval:
            best_eval = eval
            best_move = move

    return best_move
