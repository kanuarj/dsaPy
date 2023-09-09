def twoPointers (inputArr, left, right):
    while left < right:
        inputArr[left], inputArr[right] = inputArr[right], inputArr[left]
        left += 1
        right -= 1

def reverseArr (inputArr, left, right):
    if left > right:
        return
    inputArr[left], inputArr[right] = inputArr[right], inputArr[left]
    reverseArr (inputArr, left + 1, right - 1)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    reverseArr (arr, 0, len(arr)-1)
    print (arr)