import sys

def delete(array, deleteIndex):
    length =len(array)

# create a new temp array, length = length - 1
tempArray = [0 for _ in range(length -1)]
for i in range(0, length):
    if i < deleteIndex:# Copy the data in front of index to the front of
        tempArray[i] = array[i]
        if i > deleteIndex:
# Copy the array after index to the end of
 tempArray[i] = array[i]
return tempArray

def main():
    scores = [90,70,50,80,60,85]
index= int(input("Please enter the index to be deleted: \n"))
scores = delete(scores,index)
length = len(scores)
for i in range(0, length):
    print(scores[i],",",end="")

if __name__ == "__main__":
    main()