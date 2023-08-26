class Solution:
    def twoSum(self, nums: list(), target: int) -> list():
        hashmap = dict()

        for index, value in enumerate (nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[value] = index

        return []
    
if __name__ == '__main__':
    sol = Solution ()
    nums = [10, 13, 9, 15]
    target = 19
    outcome = sol.twoSum (nums, target)
    print (outcome)
        