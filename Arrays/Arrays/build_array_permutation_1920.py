## Problem: Build Array from Permutation
- Time Complexity: O(n)
- Space Complexity: O(n)


#frist we are create the empty list
#then we are travles 
#and store tha value of index in variable values 
#and this values  variable append ans 
#in last return ans 


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
      ans = []
      for i in range(len(nums)):
        values = nums[nums[i]]
        ans.append(values)
      return ans

