class Solution:
    def search(self, nums: list(), target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
        
            elif nums[start] <= nums[middle]:
                if nums[start] <= target and target <= nums[middle]:
                    end -= 1
                else:
                    start += 1

            elif nums[middle] <= nums[end]:
                if nums[end] >= target and target >= nums[middle]:
                    start += 1
                else:
                    end -=1

        return -1
    
if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution ()
    outcome = sol.search (nums=nums, target=target)
    print (outcome)
        