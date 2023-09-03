class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        holder = [c in {'a', 'e', 'i', 'o', 'u'} for c in s]

        maximumCount = count = sum (holder[:k])

        for i in range (len (s)-k):
            count += holder[i+k] - holder[i]

            if count > maximumCount:
                maximumCount = count

        return maximumCount
    
if __name__ == '__main__':
    sol = Solution ()
    s = 'abciiidef'
    k = 3
    print (sol.maxVowels (s, k))