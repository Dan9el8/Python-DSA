def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid - 1
        else:
            high = mid + 1
            return None
        
        num = [1,5,8,9,4]
        print(binary_search(num, 3))