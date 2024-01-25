"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

from typing import List,Set
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars: Set[str] = set()

        def check_repeat(chars, s):
            prev = set()
            for c in s:
                if c in chars or c in prev:
                    return True
                prev.add(c)
            return False

        def dfs(i):
            if i == len(arr):
                return len(chars)
            result = 0
            if not check_repeat(chars, arr[i]):
                for c in arr[i]:
                    chars.add(c)
                result = dfs(i+1)
                for c in arr[i]:
                    chars.remove(c)
            return max(result, dfs(i+1))
        return dfs(0)
    
arr = ["un","iq","ue"]
c = Solution()
print(c.maxLength(arr))