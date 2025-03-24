import sys

def insert(array, score, insertIndex):
    length = len(array)
    tempArray = [0 for _ in range(length + 1)]
    for i in range(0, length):
        if i < insertIndex:
            tempArray[i] = array[i]
        else:
            tempArray[i + 1] = array[1]
            tempArray[insertIndex] = score
            return tempArray

            def main():
                scores = [90,70,50,80,60,85]
                scores = insert(scores,75,2) #insert 75 into the position index = 2
                length = len(scores)
                for i in range(0, length):
                    print(scores[i], ",", end="")

                    if __name__ == "__main__":
                        main()