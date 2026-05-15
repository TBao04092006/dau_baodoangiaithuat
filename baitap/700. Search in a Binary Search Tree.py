def searchBST(root, val):
    # Chạy vòng lặp cho đến khi tìm thấy hoặc hết cây
    while root is not None and root.val != val:
        # Nếu val nhỏ hơn gốc, sang trái
        if val < root.val:
            root = root.left
        # Nếu val lớn hơn gốc, sang phải
        else:
            root = root.right
    
    # Trả về nút tìm được (hoặc None nếu không thấy)
    return root