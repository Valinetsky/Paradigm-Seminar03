class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def draw_board(self):
        cell = 1
        print("-------------")
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print(
                "| "
                + " | ".join(row)
                + " | ----->"
                + " | "
                + str(cell)
                + " | "
                + str(cell + 1)
                + " | "
                + str(cell + 2)
                + " |"
            )
            print("-------------")
            cell += 3

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],  # горизонтальные
            [3, 4, 5],
            [6, 7, 8],  
            [0, 3, 6],  # вертикальные
            [1, 4, 7],
            [2, 5, 8],  
            [0, 4, 8],  # диагональные
            [2, 4, 6],  
        ]

        for combination in winning_combinations:
            if (
                self.board[combination[0]]
                == self.board[combination[1]]
                == self.board[combination[2]]
                != " "
            ):
                return True

        return False
