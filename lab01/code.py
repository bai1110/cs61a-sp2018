#Q1
print(True and 13)
print(False or 0)
print(not 10)
print(not None)
#print(True and 1 / 0 and False)
print(True or 1 / 0 or False)
print(True and 0)
print(False or 1)
print(1 and 3 and 6 and 10 and 15)
print(0 or False or 2 or 1 / 0)
print(not 0)
print((1+1) and 1)
#print(1/0 or True)
print((True or False) and False)





#Q3
def repeated(f, n, x):
    """Returns the result of composing f n times on x.
    def square(x):
         return x * x

    repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    repeated(square, 1, 4)  # square(4)
    16
    repeated(square, 6, 2)  # big number
    18446744073709551616
    def opposite(b):
         return not b

    repeated(opposite, 4, True)
    True
    repeated(opposite, 5, True)
    False
    repeated(opposite, 631, 1)
    False
    repeated(opposite, 3, 0)
    True
    """
    if n == 1:
        return f(x)
    else:
        r = f(x)
        for i in range(n-1):
            r = f(r)
        return r


def square(x):
    return x * x


def opposite(b):
    return not b


print(repeated(opposite, 3, 0))





#Q4
def sum_digits_left(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    x = 0
    s = 0
    l = len(str(n))
    while x < l:
        if n == 0:
            break
        digit = n // pow(10, len(str(n)) - 1)  # 5
        n = n % (digit * pow(10, len(str(n)) - 1))  # 12
        s += digit
        x += 1
    return print(s)# can use return instead of print


def sum_digits_right(n):
    d = 0
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s += d
    return s

sum_digits_left(4224) # calculate the digit starting from left
print(sum_digits_right(4224)) # calculate the digit starting form right




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0 :
        if n < 9:
            return False
        d1 = n % 10 # 7
        n = n // 10 # 88
        d2 = n % 10 # 8
        if d1*d2 == 64:
            return True
print(double_eights(80808080))
