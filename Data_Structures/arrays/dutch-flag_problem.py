red, white, blue = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    #first pass: group elements smallr than pivot
    for i in range (len(A)):

        #look for a smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
            for i in reversed(range (len(A))):
                if A[j] < pivot:
                    break

                #look for a larger element. stop when we reach an element less than
                #pivot, since first pass has moved them to the start of A

                for j in reversed(range(i)):
                    if A[j] > pivot:
                        A[i], A[j] = A[j], A[i]
