def fact(x):
    if x == 1:
        return 1
    else:
        x * fact(x-1) 