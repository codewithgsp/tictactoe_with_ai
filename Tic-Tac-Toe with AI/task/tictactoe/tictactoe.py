from random import choice


class TicTacToe:

    def __init__(self):
        self.game = [[' ' for _ in range(3)] for _ in range(3)]
        self.element_status = 1
        self.choice_list = [1, 2, 3]
        self.command_options = ['easy', 'user', 'medium']
        self.opposite_symbol_map = {'X': 'O', 'O': 'X'}

    def display_dash(self):
        print('-' * 9)

    def display_game(self):
        self.display_dash()
        for row in self.game:
            print('|', " ".join(row), '|')
        self.display_dash()

    def check_win_scenario(self, symbol):
        # check for each row for a symbol
        for i in range(len(self.game)):
            if self.game[i][0] == self.game[i][1] == self.game[i][2] == symbol:
                return True
        # check for each column for a symbol
        for i in range(len(self.game)):
            if self.game[0][i] == self.game[1][i] == self.game[2][i] == symbol:
                return True
        # check for main diagonal and secondary diagonal
        if ((self.game[0][0] == self.game[1][1] == self.game[2][2] == symbol)
                or (self.game[2][0] == self.game[1][1] == self.game[0][2] == symbol)):
            return True
        # if no condition match, return False
        return False

    def analyse_result(self):
        if self.check_win_scenario('X'):
            print('X wins')
            return True
        if self.check_win_scenario('O'):
            print('O wins')
            return True
        if self.element_status > 9:
            print('Draw')
            return True
        return False

    def calc_matrix_value(self, x, y):
        return 3 - y, x - 1

    def substitute_in_grid(self, symbol, x, y):
        if self.game[x][y] == ' ':
            self.game[x][y] = symbol
            self.element_status += 1
            return True
        return False

    def generate_computer_coordinates(self):
        return choice(self.choice_list), choice(self.choice_list)

    def user_move(self, symbol):
        while True:

            # check for non numeric characters and raise alert
            try:
                x, y = map(int, input('Enter the coordinates:').split())
            except ValueError:
                print('You should enter numbers!')
                continue

            # check for x or y co-ordinates for more than value 3
            if not (1 <= x <= 3 and 1 <= y <= 3):
                print('Coordinates should be from 1 to 3!')
                continue

            # assign the value as per matrix
            i, j = self.calc_matrix_value(x, y)

            # search for the cell location and substitute
            if self.substitute_in_grid(symbol, i, j):
                break
            else:
                print('This cell is occupied! Choose another one!')
                continue

    def random_move(self, symbol):
        while True:
            x, y = self.generate_computer_coordinates()
            i, j = self.calc_matrix_value(x, y)
            if self.substitute_in_grid(symbol, i, j):
                break

    def check_win_block_step(self, symbol):

        # check for each row for a symbol
        for i in range(len(self.game)):
            row_list = [self.game[i][0], self.game[i][1], self.game[i][2]]
            if (len([sym for sym in row_list if sym == symbol]) == 2
                    or len([sym for sym in row_list if sym == self.opposite_symbol_map.get(symbol)]) == 2):
                if ' ' in row_list:
                    index = row_list.index(' ')
                    self.game[i][index] = symbol
                    return True

        # check for each column for a symbol
        for i in range(len(self.game)):
            column_list = [self.game[0][i], self.game[1][i], self.game[2][i]]
            if (len([sym for sym in column_list if sym == symbol]) == 2
                    or len([sym for sym in column_list if sym == self.opposite_symbol_map.get(symbol)]) == 2):
                if ' ' in column_list:
                    index = column_list.index(' ')
                    self.game[index][i] = symbol
                    return True

        # check for main diagonal and secondary diagonal
        for i in range(2):
            diagonal = []
            if i == 0:
                diagonal = [self.game[i][i], self.game[i + 1][i + 1], self.game[i + 2][i + 2]]
            elif i == 1:
                diagonal = [self.game[i + 1][i - 1], self.game[i][i], self.game[i - 1][i + 1]]
            if (len([sym for sym in diagonal if sym == symbol]) == 2
                    or len([sym for sym in diagonal if sym == self.opposite_symbol_map.get(symbol)]) == 2):
                if ' ' in diagonal:
                    index = diagonal.index(' ')
                    if i == 0:
                        self.game[i + index][i + index] = symbol
                        return True
                    if i == 1:
                        if index == 0:
                            self.game[i + 1][i - 1] = symbol
                            return True
                        if index == 1:
                            self.game[i][i] = symbol
                            return True
                        if index == 2:
                            self.game[i - 1][i + 1] = symbol
                            return True
        # if no condition match, return False
        return False

    def play_medium_version(self, symbol):
        print('Making move level "medium"')
        if self.check_win_block_step(symbol):
            self.element_status += 1
        else:
            self.random_move(symbol)

    def play_easy_version(self, symbol):
        print('Making move level "easy"')
        self.random_move(symbol)

    def computer_move(self, symbol, option='easy'):
        if option == 'easy':
            self.play_easy_version(symbol)
        elif option == 'medium':
            self.play_medium_version(symbol)

    def get_user_command(self):
        while True:
            # Ask for the command:
            command = input('Input command:')
            if command.startswith('start'):
                split_parameters = command.split(' ')
                if len(split_parameters) == 3:
                    mode_1, mode_2 = split_parameters[1], split_parameters[2]
                    if mode_1 in self.command_options and mode_2 in self.command_options:
                        return mode_1, mode_2
                    else:
                        print('Bad parameters!')
                        continue
                else:
                    print('Bad parameters!')
                    continue
            elif command.startswith('exit'):
                exit(0)

    def move(self, mode, symbol):
        if mode == 'user':
            self.user_move(symbol)
        else:
            self.computer_move(symbol, option=mode)

    def reset_game(self):
        self.element_status = 1
        self.game = [[' ' for _ in range(3)] for _ in range(3)]

    def start_play(self, mode_1, mode_2):
        self.display_game()
        while True:

            # player mode_1
            self.move(mode_1, 'X')
            self.display_game()
            if self.analyse_result():
                break

            # player mode_2
            self.move(mode_2, 'O')
            self.display_game()
            if self.analyse_result():
                break

    def play(self):
        while True:
            self.reset_game()
            play_mode_1, play_mode_2 = self.get_user_command()
            self.start_play(play_mode_1, play_mode_2)


tic_tac_toe = TicTacToe()
tic_tac_toe.play()
