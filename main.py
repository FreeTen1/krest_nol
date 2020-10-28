field = [["-" for j in range(3)] for i in range(3)] #предупреждаю код ужасен)) не знаю как улучшить(

def find_tire():
    check = 0
    for row in field:
        for elem in row:
            if elem == "-":
                check += 1
    return check


def win(x):
    for i in range(len(field) - 1):
        if field[i][0] == field[i][1] == field[i][2] == x:
            return True
        if field[0][i] == field[1][i] == field[2][i] == x:
            return True
    if field[0][0] == field[1][1] == field[2][2] == x:
        return True
    if field[0][2] == field[1][1] == field[2][0] == x:
        return True
    return False


def field_output():
    print("  1 2 3")
    n_row = 1
    for row in field:
        print(n_row, end=" ")
        for elem in row:
            print(elem, end=' ')
        print()
        n_row += 1
    return None


def change_field(n_m, value):  # хотел сделать через декоратор, но так как у меня одна ф-я подумал что все проверки лучше сделать в ней
    if any([n_m[0] < 1, n_m[1] < 1]):  # обработка значений < 1, если ввести 0 или меньше строку или столбец питон в обратную сторону считает, поэтому нужно)
        print("Некорректно! Попробуйте снова =)")
        return False
    if field[n_m[0] - 1][n_m[1] - 1] != "-":
        print("Место занято! Попробуйте снова")
        return False
    else:
        field[n_m[0] - 1][n_m[1] - 1] = value
        return True


n_moves = 1  # счётчик хода, нечётный = х, чётный 0
while True:
    try:  # помню из с++ о нём, тем самым обробатываю некорренктный ввод данных пользователя (слова, одно число и тд)
        field_output()
        if not find_tire():
            print("Победила дружба!!!)))")
            input()
            break
        if n_moves % 2 == 1:
            step = list(map(int, input("ходит 'х' введите строку и столбец (через пробел) x: ").split()))
            if change_field(step, "x"):
                if win("x"):
                    print("Поздравляю!!! Выиграл игрок 'x'")
                    field_output()
                    input()
                    break
                n_moves += 1
        else:
            step = list(map(int, input("ходит '0' введите строку и столбец (через пробел) 0: ").split()))
            if change_field(step, "0"):
                if win("0"):
                    print("Поздравляю!!! Выиграл игрок '0'")
                    field_output()
                    input()
                    break
                n_moves += 1
    except:
        print("Некорректно! Попробуйте снова =)")
