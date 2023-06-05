class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    print(s)
    return 0

if __name__ == '__main__':
  solution = Solution()

  """
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
  """
  print(solution.lengthOfLongestSubstring('abcabcbb'))

  """
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
  """
  print(solution.lengthOfLongestSubstring('bbbbb'))

  """
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
  """
  print(solution.lengthOfLongestSubstring('pwwkew'))