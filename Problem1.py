# Used hashing (dictionary) to store numbers while iterating through the list, checking if the c
# omplement (target - current number) exists in the hashMap for an 
# O(1) lookup, ensuring an efficient solution. If found, it returns the indices; otherwise, it adds the number to the hashMap.

# Time Complexity: O(n) (single pass through the list).
# Space Complexity: O(n) n elements in the hashMap).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap= {}
        for i,n in enumerate(nums):
            comp = target - n
            if comp in hashMap:
                return [i, hashMap[comp]]
            hashMap[n] = i