def postorderTraversal(self, root):
        if not root: return []
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            res.append(node.val)
            # Đẩy con bên trái vào trước để xử lý sau (LIFO)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return res[::-1] # Đảo ngược để có: Trái - Phải - Gốc