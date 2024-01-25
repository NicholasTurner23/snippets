"""
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.
Example input: = nums = [1,2,3]
output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List

def permuations(nums:List[int]) -> List[List[int]]:
    store = []
    if len(nums) == 1:
        return [nums[:]]
    
    for _ in range(len(nums)):
        n = nums.pop(0)
        permuts = permuations(nums)
    
        for perm in permuts:
            perm.append(n)
        store.extend(permuts)
        
        nums.append(n)
    return store

nums = [1,2,3]
print(permuations(nums))
            

