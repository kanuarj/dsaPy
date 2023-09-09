def f (arr, i, n) -> int:
    if n <= 0:
        return 0
    
    elif (arr[i] % 2 == 0):
        return arr[i] + f (arr, i+1, n-1)
    
    else:
        return arr[i] - f (arr, i+1, n-1)
    

if __name__ == '__main__':
    arr = [12, 7, 13, 4, 11, 6]
    n = 6
    outcome = f (arr, 0, n)
    print (outcome)
