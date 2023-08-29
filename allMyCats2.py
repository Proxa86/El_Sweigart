catName = []
while True:
    print('Укажите имя кота или кошки ' + str(len(catName) + 1) + ' (<Enter> для завершения):')
    name = input()
    if name == '':
        break
    catName = catName + [name]
print('Имена котов и кошек: ')
for name in catName:
    print(' ' + name)