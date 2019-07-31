from decimal import *

def decimal():
    a = Decimal('.10')
    b = Decimal('.30')
    sum = (3 * a) + b #can be +,-,/,//
    print(f'Decimal fn result is {sum}')
    print(type(sum))
    integer()

def integer():
    c = 7
    d = 3
    sum1 = c + d  #can be +,-,/,//
    print(f'Integer fn result is {sum1}')
    print(type(sum1))
    boolean(False)
    floating()
    
def floating():
    e = .1
    f = .3
    sum2 = e + e - f  #can be any arithmetic operator
    print(f'Floating fn result is {sum2}')
    print(type(sum2))
    boolean(True)
    
def boolean(g):
    if g:
        print('Boolean call is from Floating fn')
        print(type(g))
    else:
        print('Boolean call is from Integer fn')
        print(type(g))

decimal()