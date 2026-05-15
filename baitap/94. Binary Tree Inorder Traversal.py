def inorderTraversal(self, root):
        res = []
        
        def helper(node):
            if not node:
                return
            helper(node.left)    # Đi hết sang trái
            res.append(node.val) # Lấy giá trị gốc
            helper(node.right)   # Đi sang phải
            
        helper(root)
        return res
        