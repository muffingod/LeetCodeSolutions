from typing import Optional, List

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
  def __str__(self):
    output = 'ListNode:\n'
    output += f'\tValue: {self.val}\n'
    output += f'\tHasNext: {"True" if self.next != None else "False"}\n'
    return output

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    print(f'l1: {l1}')
    print(f'l2: {l2}')

    return

def lNL(list: List[int]):
  prevListNode = None
  for listItem in reversed(list):
    listNode = ListNode(listItem, prevListNode)
    prevListNode = listNode
  return prevListNode

if __name__ == '__main__':
  solution = Solution()
  """
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
  """
  print(solution.addTwoNumbers(lNL([2,4,3]), lNL([5,6,4])))
  
  """
    Input: l1 = [0], l2 = [0]
    Output: [0]
  """
  print(solution.addTwoNumbers(lNL([0]), lNL([0])))

  """
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
  """
  print(solution.addTwoNumbers(lNL([9,9,9,9,9,9,9]), lNL([9,9,9,9])))
