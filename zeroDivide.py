#def spam(diviBy):
#    try:
#        return 42 / diviBy
#    except ZeroDivisionError:
#        print('Error: Invalid argument.')

#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))

def spam(diviBy):
    return 42 / diviBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')