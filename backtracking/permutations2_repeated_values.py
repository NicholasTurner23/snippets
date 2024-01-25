"""
Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permuations in any order.
Example input: nums = [1,1,2]
output: [[1,1,2], [1,2,1], [2,1,1]]
"""
from typing import List, Dict

def permuations2(nums: List[int]) -> List[List[int]]:
    count: Dict[int,int] = {n:0 for n in nums}
    perm = []
    result = []
    for n in nums:
        count[n] += 1

    def dfs():
        if len(perm) == len(nums):
            return result.append(perm.copy())
        
        for n in count:
            if count[n] > 1:
                perm.append(n)
                count[n] -= 1
                dfs()

                count[n] += 1
                perm.pop(n)
    dfs()
    return result

nums = [1,1,2]
print(permuations2(nums))




        

        

