def addTwoNumbers(l1, l2):
    stack1, stack2 = [], []
    
    # Bước 1: Đưa l1 vào stack
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
        
    # Bước 2: Đưa l2 vào stack
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
        
    curr_list = None
    carry = 0
    
    # Bước 3: Cộng dần từ cuối
    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        
        # Tạo node mới và nối vào phía trước (để đảo ngược kết quả)
        new_node = ListNode(total % 10) # type: ignore
        new_node.next = curr_list
        curr_list = new_node
        
    return curr_list