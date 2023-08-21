import random

secretNumber = random.randint(1, 20)
print('Я загадал число о 1 до 20.')

for guessesTaken in range(1,7):
    print('Угадай число.')
    guess = int(input())

    if guess < secretNumber:
        print('Я загадал большее число.')
    elif guess > secretNumber:
        print('Я загадал меньшее число.')
    else:
        break

if guess == secretNumber:
    print('Отлично! Количество попыток: ' + str(guessesTaken) + '.')
else:
    print('Вам не повезло. Я загадал число ' + str(secretNumber))