from time import perf_counter

def binarySearch (arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle -1

    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 5
    start = perf_counter()
    binarySearch (arr=nums, target=target)
    end = perf_counter ()
    print (f'Time taken : {end-start}')