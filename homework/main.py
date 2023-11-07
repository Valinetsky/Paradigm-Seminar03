from tictactoe import TicTacToe


def main():
    game = TicTacToe()
    while True:
        game.draw_board()
        print('Игрок', game.current_player, 'ваш ход')
        position = int(input('Выберите ячейку для хода (от 1 до 9): ')) - 1
        game.make_move(position)
        if game.check_winner():
            game.draw_board()
            print('Игрок', game.current_player, 'проиграл!')
            break
        elif ' ' not in game.board:
            game.draw_board()
            print('Ничья!')
            break
 
if __name__ == '__main__':
    main()