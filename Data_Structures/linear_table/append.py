import sys

def main():
    scores = [90,70,50,80,60,85]
    length = len(scores)

    tempArray = [0 for _ in range(length+1)]

    for i in range(0, length):
        tempArray[i] = scores[i]

        tempArray[length] = 75
        scores = tempArray

        length = len(scores)
        for i in range(0, length):
            print(scores[i], ",", end="")

            if __name__ == "__main__":
                main()