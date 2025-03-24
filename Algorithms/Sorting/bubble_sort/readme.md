## Bubble sorting algorithms
Bubble sort algorithm is done by comparing arrays[i] with arrays[i + 1], if arrays[i] > arrays[i + 1] are exchanged
If not it compares with the next number

The process is repeated until the sotring is completed.

In example where given the following numbers 60, 50, 95, 80 and 70

# Step one
compare 60 with 50, because its greater you swap the numbers
Compare 60 with 95, because is less than 95 you leave and move to the next number.
Compare 95 with 80, because its greater than 80 you swipe
Compare 95 with 70, because its greater than 70 you swipe the numbers 
So the numbers will be 50, 60, 80, 70, 95
95 bocomes the max number

# Step two
Compare 50 with 60, because it less than 60 you leave it and move to the next pair
Compare 60 with 80, beacause it less than 80 you leave it and move to the next number.
Compare 80 with 70, because its greater than 70 you swap it.
Compare 80 with 95, because its less than 95 you leave it. 
Numbers are 50, 60, 70, 80, 95
80 becomes max number

# Step 3
Compare 50 with 60, no swap because its less than 60
Compare 60 eith 70, no swap becase its less thn 70

If no swap happens between numbers terminate the sorting, now we can get the sorting numbers from small to large.

50, 60, 70, 80, 95