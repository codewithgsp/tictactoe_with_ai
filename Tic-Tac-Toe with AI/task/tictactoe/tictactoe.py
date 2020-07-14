from random import choice


class TicTacToe:

    def __init__(self):
        self.game = [[' ' for _ in range(3)] for _ in range(3)]
        self.count_x = 0
        self.count_o = 0
        self.count_u = 0
        self.element_status = 1
        self.choice_list = [1, 2, 3]

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

    def add_element(self):
        while True:
            # check for non numeric characters and raise alert
            if self.element_status <= 9:
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
                if self.substitute_in_grid('X', i, j):
                    break
                else:
                    print('This cell is occupied! Choose another one!')
                    continue
            else:
                print('Draw')
                exit(0)

    def play_easy_version(self):
        print('Making move level "easy"')
        while True:
            x, y = self.generate_computer_coordinates()
            i, j = self.calc_matrix_value(x, y)
            if self.substitute_in_grid('O', i, j):
                break

    def computer_move(self):
        self.play_easy_version()

    def play(self):
        self.display_game()
        while True:
            # User move
            self.add_element()
            self.display_game()
            if self.analyse_result():
                break

            # computer move
            self.computer_move()
            self.display_game()
            if self.analyse_result():
                break


tic_tac_toe = TicTacToe()
tic_tac_toe.play()
