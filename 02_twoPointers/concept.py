from time import perf_counter

def summatationOccurence (arr : list(), target : int) -> bool:
    for i in range (len(arr)):
        for j in range (len(arr)):
            if (arr[i] + arr[j]) == target:
                return True
            
            if (arr[i] + arr[j]) > target:
                return False
            
    return False

def twoPointers (arr : list(), target : int) -> bool:
    start, end = 0, len(arr)-1
    while start < end:
        if (arr[start] + arr[end]) == target:
            return True
        elif (arr[start] + arr[end]) > target:
            end -= 1
        else:
            start += 1

    return False


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    target = 90
    start = perf_counter()
    outcome = summatationOccurence (arr, target)
    end = perf_counter()
    print (f'The time taken by the summation occurence is {end-start}')

    start = perf_counter()
    outcome = twoPointers (arr, target)
    end = perf_counter()
    print (f'The time taken by the two pointers is {end-start}')