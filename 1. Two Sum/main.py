from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """ Complexity: O(n^2)
    for i in range(0, len(nums)-1):
      for j in range(i + 1, len(nums)):
        if(nums[i]+nums[j] == target):
          return [i, j]
    """
    """ Complexity: O(n)
    dict = {element: index for (index, element) in enumerate(nums)}
    for i in range(len(nums)):
      complement = target - nums[i]
      if(complement in dict.keys() and dict[complement] != i):
        return [i, dict[complement]]
    """
    dict = {}
    for i, j in enumerate(nums):
      complement = target - j
      if(complement in dict):
        return [dict[complement], i]
      dict[j] = i

if __name__ == "__main__":
  solution = Solution()
  """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
  """
  print(solution.twoSum([2,7,11,15], 9))

  """
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
  """
  print(solution.twoSum([3, 2, 4], 6))
  
  """
    Input: nums = [3,3], target = 6
    Output: [0,1]
  """
  print(solution.twoSum([3, 3], 6))