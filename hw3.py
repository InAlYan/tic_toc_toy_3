class CrossOneZeroGame:

    def __init__(self, game_board, player1, player2):
        self.game_board = game_board
        self.player1 = player1
        self.player2 = player2

    def play(self):

        new_game = ''
        player = player1
        while new_game != 'y':
            self.game_board.clear_board()
            self.game_board.show_board()

            # Пока никто не победил
            while not self.game_board.is_win():
                x, y = player.cell_input()
                correct_data = self.game_board.set_cell(x, y, player.symbol)
                # Проверяем, что введены корректные данные не больше размеров игрового поля и ещё не заполненные
                while not correct_data:
                    x, y = player.cell_input()
                    correct_data = self.game_board.set_cell(x, y, player.symbol)

                self.game_board.show_board()
                # Меняем игрока
                player = player2 if player == player1 else player1

            # Поздравления
            if player == player2:
                player1.score += 1
                print(f'Поздравляем {player1.name}!\nВаш счет: {player1.score}')
            else:
                player2.score += 1
                print(f'Поздравляем {player2.name}!\nВаш счет: {player2.score}')

            new_game = input("Закончить? (y)")


class Player:

    def __init__(self, name, symbol, score = 0):
        self.name = name
        self.symbol = symbol
        self.score = score

    def cell_input(self):
        """
        : Ввод строки и столбца игрока в консоли
        :return:
        """
        cell = input(f'{self.name}, введите номер строки и номер столбца через пробел: ')
        x, y = cell.strip().split(' ')

        while not x.isdigit() or not y.isdigit():
            cell = input(f'{self.name}, введите номер строки и номер столбца через пробел: ')
            x, y = cell.strip().split(' ')

        return int(x), int(y)


class GameBoard:

    def __init__(self, dimension):
        self.dimension = dimension
        self.board = []

        # создаем одномерный массив размерностью количества ячеек
        for i in range(self.dimension ** 2):
            self.board.append(None)

    def show_board(self):
        # Для одномерного массива
        for i in range(self.dimension ** 2):
            arr_val = "_" if self.board[i] is None else self.board[i]
            print(f'{arr_val} ', end='')
            if ((i + 1) % self.dimension) == 0:
                print()

    def clear_board(self):
        for i in range(len(self.board)):
            self.board[i] = None

    def is_win(self):
        """
        : Перебираем массив и находим победили ли мы или нет
        :return: bool
        """
        # Проверки для одномерного массива
        return self.__check_columns() or self.__check_rows() or self.__check_diagonal(1) or self.__check_diagonal(2)

    def __check_diagonal(self, diagonal_number):
        """
        : Проверяем условия победы по диагоналям
        :param diagonal_number: номер диагонали 1 или 2
        :return: bool
        """
        # Для одномерного массива
        # Формула для перебора по первой диагонали одномерного массива: i * (self.dimension + 1)
        # Формула для перебора по второй диагонали одномерного массива: (i + 1) * (self.dimension - 1)
        # Общая Формула для перебора по диагоналям одномерного массива: (i + adding) * (self.dimension + sign)
        sign, adding, first_elem = (1, 0, self.board[0]) if diagonal_number == 1 else (-1, 1, self.board[self.dimension - 1])

        if first_elem is None:
            return False
        for i in range(1, self.dimension):
            index = (i + adding) * (self.dimension + sign)
            if first_elem != self.board[index]:
                return False
        return True

    def __check_rows(self):
        """
        : Проверка по горизонтальным строкам
        :return: bool
        """
        # Для одномерного массива
        # Формула для перебора по строкам одномерного массива: i * self.dimension + j

        win_rows = False
        for i in range(self.dimension):  # Перебираем строки
            first_elem_row = self.board[i * self.dimension]

            win_row = True
            if first_elem_row is None:
                win_row = False
                continue

            for j in range(1, self.dimension):  # Перебираем конкретные ячейки строки
                if first_elem_row != self.board[i * self.dimension + j]:
                    win_row = False
            win_rows = win_rows or win_row

        return win_rows

    def __check_columns(self):
        """
        : Проверка по вертикальным колонкам
        :return: bool
        """
        # Для одномерного массива
        # Формула для перебора по столбцам одномерного массива: i + self.dimension * j

        win_columns = False
        for i in range(self.dimension):  # Перебираем колонки
            first_elem_column = self.board[i]

            win_column = True
            if first_elem_column is None:
                win_column = False
                continue

            for j in range(1, self.dimension):  # Перебираем конкретные ячейки колонки
                if first_elem_column != self.board[i + self.dimension * j]:
                    win_column = False
            win_columns = win_columns or win_column

        return win_columns

    def set_cell(self, x, y, val):
        """
        :Пытаемся вставить в массив в строку x (счет от 1) и в колонку y (счет от 1) значение val
        :param x: строки счет от 1
        :param y: колонки счет от 1
        :param val: вставляемое значение
        :return: bool
        """
        # Формула для преобразования x (строки) и y (колонки) в линейный номер массива: (x - 1) * self.dimension + (y - 1)
        if x <= self.dimension and y <= self.dimension and self.board[(x - 1) * self.dimension + (y - 1)] is None:
            self.board[(x - 1) * self.dimension + (y - 1)] = val
            return True
        return False


new_board = GameBoard(3)
player1 = Player('Player1', 'x')
player2 = Player('Player2', 'o')

new_game = CrossOneZeroGame(new_board, player1, player2)
new_game.play()