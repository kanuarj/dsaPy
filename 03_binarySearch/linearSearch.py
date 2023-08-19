from time import perf_counter

def linearSearch (arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
        
    return False

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    target = 9
    start = perf_counter()
    linearSearch (arr=nums, target=target)
    end = perf_counter ()
    print (f'Time taken : {end-start}')
        
