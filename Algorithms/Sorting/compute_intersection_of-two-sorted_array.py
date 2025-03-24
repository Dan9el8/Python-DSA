#Write a program which takes as hput two sorted arrays, and returns a new array containing
#elements that are present in both of the input arrays. The input arrays may have duplicate entries,
#but the returned array should be free of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12>
#and (5,5,6,8 ,8,9,70,10), your output should be (5, 6, 8).

def intersect(A, B):
    i, j,intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[j] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
                i, j = i + 1, j + 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1
                return intersection_A_B