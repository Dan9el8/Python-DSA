#Write a program which takes as input an array of digits encoding a nonnegative decimal integer
#D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
#you should update the array to (1,3,0). Your algorithm should work even if it is implemented in alangua ge that has finite-precision arithmetic.

def plus_pone(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)
            return A
