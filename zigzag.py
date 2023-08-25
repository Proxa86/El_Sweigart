import time
import sys

indent = 0  # колличество пробелов для отступа
indentIncreasing = True  # увеличение или уменьшение отступа

try:
    while True:  # главный цикл программы
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # пауза длительностью 0.1 секунды

        if indentIncreasing:
            indent = indent + 1  # увеличение количества пробелов
            if indent == 20:
                indentIncreasing = False  # изменение направления
        else:
            indent = indent - 1  # уменьшение количества пробелов
            if indent == 0:
                indentIncreasing = True  # изменение направления
except KeyboardInterrupt:
    sys.exit()
