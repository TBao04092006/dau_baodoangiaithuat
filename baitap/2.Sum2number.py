class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def taoHaiSo(n1, n2):
    nut_gia = ListNode(0)
    current = nut_gia # biến giả để quản lí
    carry = 0  # biến nhớ giá trị khi tăng 
    while n1 or n2 or carry :
        val1 = n1.val if n1 else 0
        val2 = n2.val if n2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        if n1: n1 = n1.next
        if n2: n2 = n2.next
    return nut_gia.next
n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))

result = taoHaiSo(n1, n2)
# ket qua do vao trong danh sach này
output=[]
while result:
    output.append(result.val)
    result = result.next
print(output)

       