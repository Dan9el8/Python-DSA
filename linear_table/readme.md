## Linear table append
To add a number at the end of the list of array:
1. Fisrt create a temporary array(tempArray) larger than the original score of array length

2. Copy each value of the numbers to tempArray

3. Assign the number to append to the lat index position of tempArray

4. Finally assign the tempArray pointer reference to the original scores.

## Linear table insert
To insert a number anywhere in the one-dimensional  array number:
1. First create a temporary array tempArray larger than the original numbers
2. Copy each value of the previous value of the scores array from the begining to the insertation position to tempArray
3. Move the number array from the insertion position to eah value of the last element and move it back to tempArray
4. Then insert the number to the index of the tempArray.
5. Finally assing the tempArray pointer reference to the number 

## linear table delete
1
.
Delete the value of the
index=2
from scores array
Analysis:
1. Create a temporary array tempArray
that length smaller than scores
by 1.
2. Copy the data in front of i=2
to the front of tempArray
3. Copy the array after i=2
to the end of tempArray
4. Assign the tempArray
pointer reference to the scores
5. Printout scores
 