

class TicTacToe:

    def __init__(self, userinput):
        self.user_input = userinput
        self.game = [['*' for _ in range(3)] for _ in range(3)]
        self.count_x = 0
        self.count_o = 0
        self.count_u = 0

    def split_input_to_matrix(self):
        count = 0
        for i in range(3):
            for j in range(3):
                self.game[i][j] = self.user_input[count]
                count += 1

    def display_dash(self):
        print('-' * 9)

    def display_game(self, initial=False):
        self.display_dash()
        if initial:
            self.split_input_to_matrix()
        for row in self.game:
            print('|', " ".join(row), '|')
        self.display_dash()

    def check_count_of_xo(self):

        self.count_x = 0
        self.count_o = 0
        self.count_u = 0

        for i in range(len(self.game)):
            for j in range(len(self.game)):
                if self.game[i][j] == 'X':
                    self.count_x += 1
                elif self.game[i][j] == 'O':
                    self.count_o += 1
                elif self.game[i][j] == '_':
                    self.count_u += 1

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
        self.check_count_of_xo()
        if self.check_win_scenario('X'):
            print('X wins')
            return
        if self.check_win_scenario('O'):
            print('O wins')
            return
        if self.count_u == 0:
            print('Draw')
            return
        if 0 <= abs(self.count_x - self.count_o) <= 1 and self.count_u > 0:
            print('Game not finished')
            return

    def add_element(self):
        self.check_count_of_xo()
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
            i, j = 3 - y, x - 1

            # search for the cell location and substitute
            if self.game[i][j] == '_':
                if self.count_x > self.count_o:
                    self.game[i][j] = 'O'
                else:
                    self.game[i][j] = 'X'
                break
            else:
                print('This cell is occupied! Choose another one!')
                continue

    def play(self):
        self.display_game(initial=True)
        self.add_element()
        self.display_game()
        self.analyse_result()


user_input = input('Enter cells:')
tic_tac_toe = TicTacToe(user_input)
tic_tac_toe.play()
