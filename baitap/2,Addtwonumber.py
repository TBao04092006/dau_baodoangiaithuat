class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        # Tính toán
        total = v1 + v2 + carry
        carry = total // 10
        val = total % 10
        
        # Tạo nút mới
        curr.next = ListNode(val)
        
        # Di chuyển con trỏ
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

# Test thử
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)

output = []
while result:
    output.append(result.val)
    result = result.next
print(output)

       