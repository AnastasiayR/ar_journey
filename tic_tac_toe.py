class Board:
    def __init__(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

    def current_step(self, cell, sign):
        for i_str in self.board:
            for i_col in i_str:
                if i_col == cell:
                    self.board[self.board.index(i_str)][i_str.index(i_col)] = sign

    def found_cell(self, cell):
        count_cell = 0
        for i_str in self.board:
            for i_col in i_str:
                count_cell += 1
                if count_cell == cell:
                    return self.board[self.board.index(i_str)][i_str.index(i_col)]

    def check(self):
        for i_str in self.board:
            if i_str[0] == i_str[1] == i_str[2]:
                print('Собрана строка')
                return True
        for k in range(len(self.board)):
            if self.board[0][k] == self.board[1][k] == self.board[2][k]:
                print('Собран столбец')
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
                self.board[2][0] == self.board[1][1] == self.board[0][2]:
            print('Собрана диагональ')
            return True
        return False

    def print_board(self):
        num_cell = 1
        for i in range(9):
            for j in range(2):
                if i in (0, 3, 6, 8):
                    print('     |', end='')
                elif i in (1, 4, 7):
                    sign = self.found_cell(num_cell)
                    print(' ', sign, ' |', end='')
                    num_cell += 1
                else:
                    print('_____|', end='')
            if i in (0, 3, 6, 8):
                print('      ', end='')
            elif i in (1, 4, 7):
                sign = self.found_cell(num_cell)
                print(' ', sign, ' ', end='')
                num_cell += 1
            else:
                print('______', end='')

            print('')


class Player:
    list_sign = {'X': 'крестики', '0': 'нолики'}

    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.team = self.list_sign[sign]


class Game:
    def __init__(self, board, *players):
        self.players = players
        self.board = board
        self.history_cell = []

    def party(self):
        self.board.print_board()
        continued = True
        while continued:
            for i_pl in self.players:
                self.one_step(i_pl)
                if self.board.check():
                    print('Победил игрок', i_pl.name, '-', i_pl.team, )
                    continued = False
                    break
                elif len(self.history_cell) == 9:
                    print('Ходов больше нет. Ничья!')
                    continued = False
                    break

        print('Конец игры')

    def one_step(self, player):
        print('Ход игрока: {} ({})'.format(player.name, player.team))
        step = int(input('Сделать ход в ячейку: '))
        if step not in self.history_cell:
            self.board.current_step(step, player.sign)
            self.board.print_board()
            self.history_cell.append(step)
        else:
            print('Ячейка занята')
            self.one_step(player)


gameboagd = Board()
play_1 = Player('Anna', '0')
play_2 = Player('Petr', 'X')
game = Game(gameboagd, play_1, play_2)
game.party()
