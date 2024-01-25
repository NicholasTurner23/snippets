
"""
Given a string s, partition s such that every
substring
of the partition is a
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        sub = []

        def dfs(i):
            if i >= len(s):
                return result.append(sub.copy())
            
            for k in range(i, len(s)):
                if self.check_pali(s, i, k):
                    sub.append(s[i:k+1])
                    dfs(k+1)
                    sub.pop()
        dfs(0)
        return result

    def check_pali(self, s, l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True