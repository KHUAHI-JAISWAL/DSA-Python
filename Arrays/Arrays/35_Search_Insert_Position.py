## Approach (Brute Force)

1. Traverse the array from left to right.
2. Compare each element with the target.
3. If nums[i] >= target, return i.
4. If the loop finishes, return len(nums).

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      for i in range(len(nums)):
        if nums[i]>=target:
          return i
      return len(nums)
