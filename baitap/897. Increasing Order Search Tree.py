def increasingBST(root):
        # Tạo một nút giả (dummy) để làm điểm tựa ban đầu
        dummy = TreeNode(0)
        current = dummy
        
        def inorder(node):
            if not node:
                return
            
            # Duyệt bên trái
            inorder(node.left)
            
            # Xử lý nút hiện tại:
            # 1. Loại bỏ liên kết bên trái để thỏa mãn yêu cầu bài toán
            node.left = None
            # 2. Gắn nút này vào bên phải của nút trước đó
            current.right = node
            # 3. Di chuyển con trỏ sang nút vừa mới gắn
            current = node
            
            # Duyệt bên phải
            inorder(node.right)
            
        inorder(root)
        return dummy.right
        