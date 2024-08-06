"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
Algorithm
1. Recursive approach starting from head node
2. Make a dictionary - to keep track of cloned nodes
3. If we have a cloned copy in dict, we can use that reference
4. IF we don't have a cloned copy in dict, we add a new node and add it to the vis dict
5. We make two recursive calls, one with random and other with next pointer
"""
class Solution:
    def __init__(self):
         self.mp = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        if head in self.mp:
            return self.mp[head]
        node = Node(head.val, None, None)
        self.mp[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node