# LeetCode 27 - Remove Element
# Difficulty: Easy
# Topic: Arrays, Two Pointers

# Approach:
# 1. k pointer ko 0 se start kiya.
# 2. Array traverse kiya.
# 3. Agar nums[i] != val ho to nums[k] = nums[i].
# 4. k ko increment kiya.
# 5. End me k return kiya.

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def removeElement(self, nums, val):
      k = 0
      for i in range(len(nums)):
        if nums[i]!= val:
          nums[k]=nums[i]
          k+=1
      return k
        
        

