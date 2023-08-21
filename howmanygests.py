name = ''
while not name:
    print('Введите своё имя: ')
    name = input()
print('Сколько гостей вы ждете?')
numOfGuests = int(input())
if numOfGuests:
    print('Убедитесь, что для гостей хватит места.')
print('Конец работы')