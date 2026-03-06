def preorderTraversal(self, root):
        res = []
        
        def helper(node):
            if not node:
                return
            # 1. Thêm giá trị gốc vào kết quả
            res.append(node.val)
            # 2. Duyệt sang trái
            helper(node.left)
            # 3. Duyệt sang phải
            helper(node.right)
        
        helper(root)
        return res