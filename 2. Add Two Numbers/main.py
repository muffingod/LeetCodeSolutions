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
    sum = 0
    if(l1):
      sum += l1.val
    if l2:
      sum += l2.val

    if sum >= 10:
      sum %= 10
      if l1 and l1.next:
        l1.next.val += 1
      elif l2 and l2.next:
        l2.next.val += 1
      else:
        if not l1:
          l1 = ListNode(0, ListNode(1))
        else:
          l1.next = ListNode(1)

    if((l1 and l1.next) or (l2 and l2.next)):
        return ListNode(sum, self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None))
    else:
      return ListNode(sum, None)

def lNL(list: List[int]):
  prevListNode = None
  for listItem in reversed(list):
    listNode = ListNode(listItem, prevListNode)
    prevListNode = listNode
  return prevListNode

def listNodeToList(ln: ListNode):
  resultArr = []
  if(ln.next):
    resultArr.extend(listNodeToList(ln.next))
  resultArr.append(ln.val)
  return resultArr

if __name__ == '__main__':
  solution = Solution()
  """
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
  """
  l1 = [2,4,3]
  l2 = [5,6,4]
  resNode = solution.addTwoNumbers(lNL(l1), lNL(l2))
  print(listNodeToList(resNode))
  #print(listNodeToList(solution.addTwoNumbers(lNL([2,4,3]), lNL([5,6,4]))))
  
  """
    Input: l1 = [0], l2 = [0]
    Output: [0]
  """
  print(listNodeToList(solution.addTwoNumbers(lNL([0]), lNL([0]))))

  """
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
  """
  print(listNodeToList(solution.addTwoNumbers(lNL([9,9,9,9,9,9,9]), lNL([9,9,9,9]))))
