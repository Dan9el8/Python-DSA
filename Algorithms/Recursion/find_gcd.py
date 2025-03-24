def find_gcd(x, y):
    if y == 0:
        return x
    else:
        find_gcd(y, x % y)