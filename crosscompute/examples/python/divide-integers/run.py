from sys import argv

x, y = map(int, argv[1:])
try:
    print('quotient = {}'.format(x / y))
    print('remainder = {}'.format(x % y))
except ZeroDivisionError:
    exit('divisor.error = cannot divide by zero')
