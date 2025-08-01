#Данный проект - это реализация игры в Крестики-нолики,
#где игрок (player) противостоит компьютеру (CPU)

#Глобальные константы
X = 'X'
O = 'O'
EMPTY = ' '
NUM_CELL = 9
TIE = 'TIE'

def greetRules():
    print('''
            Приветствуем тебя игрок в величайшем противостоянии всех времен и народов:
                                      КРЕСТИКИ-НОЛИКИ
  Ваша задача победить ИИ выстроив три Х или О в ряд по горизонтали/вертикали/диагонали.
  Выбор нужной клетки осуществляется с помощью цифр (0 - 8), которые расположены соответственно
  схеме:

      0 | 1 | 2
     -----------
      3 | 4 | 5 
     -----------
      6 | 7 | 8
                                      
                                  !!!ЖЕЛАЕМ УСПЕХОВ!!!''')

# Задаем вопрос с ответом Yes/No.
def ask_yes_no(_question):
    _answer = None
    while _answer not in ('y', 'n'):
        _answer = input(_question).lower()
    return _answer

# Запрашиваем ввод цифры из диапазона low - high.
def ask_number(_question, _low, _high):
    _answer = None
    while _answer not in range(_low, _high):
        _answer = int(input(_question))
    return _answer

# Выясняем, чей ход первый (игрока или компьютера)
def queue():
    _first_move = ask_yes_no("Желаете ходить первым? (y/n): ")
    if _first_move == "y":
        print("\nВ таком случае первый ход Ваш.")
        _player = X
        _CPU = O
    else:
        print("\nБудьте внимательны! С первым ходом Вы отдаёте инициативу.")
        _CPU = X
        _player = O
    return _CPU, _player

# Создаем новое игровое поле (список из 9 элементов со значением EMPTY).
def new_board():
    _board = []
    for cell in range(NUM_CELL):
        _board.append(EMPTY)
    return _board

# Выводим на экран переданную в функцию доску.
def board_scr(_board):
    print('\n\t ', _board[0], '|', _board[1], '|', _board[2])
    print('\t', '-----------')
    print('\t ', _board[3], '|', _board[4], '|', _board[5])
    print('\t', '-----------')
    print('\t ', _board[6], '|', _board[7], '|', _board[8], '\n')

# Создаем список доступных ходов.
def legal_moves(_board):
    _moves = []
    for _cell in range(NUM_CELL):
        if _board[_cell] == EMPTY:
            _moves.append(_cell)
    return _moves

# Возвращает номер поля, на которое хочет сходить игрок. Аргументы: доска, тип маркера игрока.
def player_move(_board, _player):
    _legal = legal_moves(_board)
    _move = None
    while _move not in _legal:
        _move = ask_number("На какую клетку желаете сходить? (0 - 8):", 0, NUM_CELL)
        if _move not in _legal:
            print("\nДанная клетка уже занята соперником. Выберите, пожалуйста, другую.\n")
    print("Хорошо...")
    return _move

# Возвращает номер поля, на которое ходит компьютер. Аргументы: доска, тип маркера компьютера и игрока.
def CPU_move(_board, _CPU, _player):
    # создаем локальную копию доски, чтобы избежать нежелательных эффектов в оригинале этой доски
    _board = _board[:]
    # устанавливаем порядок лучших ходов
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Компьютер выбирает клетку", end=" ")

    # Если следующий ход компьютера победный, то нужно сделать именно его
    for _move in legal_moves(_board):
        _board[_move] = _CPU
        if winner(_board) == _CPU:
            print(_move)
            return _move
        # выполнив проверку, отменяем все изменения
        _board[_move] = EMPTY

    # Если следующий ход игрока выигрышный, то его надо заблокировать
    for _move in legal_moves(_board):
        _board[_move] = _player
        if winner(_board) == _player:
            print(_move)
            return _move
        # выполнив проверку, отменяем все изменения
        _board[_move] = EMPTY

    # если ни игрок, ни компьютер не побеждает следующим ходом, то компьютер выбирает лучшую свободную клетку
    for _move in BEST_MOVES:
        if _move in legal_moves(_board):
            print(_move)
            return _move

# Смена хода. Принимает маркер последнего хода, возвращает маркер следующего хода.
def next_turn(_turn):
    if _turn == X:
        return O
    else:
        return X

# Определяем условия победы/ничьей. Возвращает Х/О в случае победы кого-то из игроков, TIE - если все поля заполнены,
# но никто не победил, None - если хотя бы одно поле не заполнено, а победитель не определён.
def winner(_board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for _row in WAYS_TO_WIN:
        if _board[_row[0]] == _board[_row[1]] == _board[_row[2]] != EMPTY:
            _winner = _board[_row[0]]
            return _winner

    if EMPTY not in _board:
        return TIE

    return None

# Декор для поздравления победителя.
def congrat_winner(_the_winner, _CPU, _player):
    if _the_winner != TIE:
        print(_the_winner, "победили!\n")
    else:
        print("Вы сыграли в ничью!\n")

    if _the_winner == _CPU:
        print("Получился неплохой AI.\n"
              "Спасибо за участие в проекте! Надеюсь Вам понравилось)))")

    elif _the_winner == _player:
        print("Вы очень неплохо справились. Вам удалось победить ИИ!\n"
              "Спасибо за участие в проекте! Надеюсь Вам понравилось)))")

    elif _the_winner == TIE:
        print("Ничья - тоже очень неплохой результат. Попробуйте снова.\n"
              "Спасибо за участие в проекте! Надеюсь Вам понравилось)))")


greetRules()
_CPU, _player = queue()
turn = X
board = new_board()
board_scr(board)
while not winner(board):
    if turn == _player:
        move = player_move(board, _player)
        board[move] = _player
    else:
        move = CPU_move(board, _CPU, _player)
        board[move] = _CPU
    board_scr(board)
    turn = next_turn(turn)

the_winner = winner(board)
congrat_winner(the_winner, _CPU, _player)

input("\n\nНажмите <Enter>, чтобы выйти...")
