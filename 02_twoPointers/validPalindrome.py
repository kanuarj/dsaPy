class Solution:
    def isPalindrome (self, s : str) -> bool:
        inputString = ' '.join(character for character in s if character.isalnum())
        inputString = inputString.lower()
        start, end = 0, len(inputString)-1
        while start < end:
            if inputString[start] != inputString[end]:
                return False
            start += 1
            end -= 1
        return True
    
if __name__ == '__main__':
    sol = Solution()
    print (sol.isPalindrome ("A man, a plan, a canal: Panama"))