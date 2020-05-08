class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        _result = []
        temp = deque([root])
        next_temp = deque()
        
        while 1:
            while temp:
                node = temp.popleft()
                if node:
                    _result.append(node.val)
                    if node.left:
                        next_temp.append(node.left)
                    if node.right:
                        next_temp.append(node.right)
            
            temp = next_temp
            if _result:
                result.append(_result)
            _result = []
            next_temp = deque()
            
            if not temp and not next_temp:
                return result
