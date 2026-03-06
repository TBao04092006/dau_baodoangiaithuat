def isBalanced(self, root):
        def check(node):
            if not node: return 0
            
            left = check(node.left)
            right = check(node.right)
            
            # Nếu nhánh con không cân bằng hoặc chênh lệch > 1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            # Trả về độ cao của nút hiện tại
            return max(left, right) + 1
            
        return check(root) != -1