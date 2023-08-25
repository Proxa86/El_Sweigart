import sys
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

#def check(number1):
#    if number1 == 1:
#        print("number_div == 1")
#        sys.exit()

#print('Enter integer number: ')
#try:
#    num = int(input())
#except ValueError:
#    print("Enter integer number: ")
#    num = int(input())

#while True:
#    number1 = collatz(num)
#    check(number1)
#    num = collatz(number1)
#    check(num)

# Вариант 2

print('Enter integer number: ')
try:
    num = int(input())
except ValueError:
    print("Enter integer number: ")
    num = int(input())

while num != 1:
    num = collatz(num)