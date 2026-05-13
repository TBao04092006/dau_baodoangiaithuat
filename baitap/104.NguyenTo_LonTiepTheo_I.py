def nextGreaterElement(nums1, nums2):
        # Dictionary để lưu: {số : phần tử lớn hơn kế tiếp của nó}
        mapping = {}
        stack = []
        
        # Duyệt qua mảng nums2 để tìm tất cả các "phần tử lớn hơn kế tiếp"
        for num in nums2:
            # Nếu stack không rỗng và số hiện tại lớn hơn số ở đỉnh stack
            while stack and num > stack[-1]:
                # Số hiện tại chính là "người lớn hơn kế tiếp" của số ở đỉnh stack
                smaller_num = stack.pop()
                mapping[smaller_num] = num
            
            # Đẩy số hiện tại vào stack để chờ tìm "người lớn hơn" cho nó
            stack.append(num)
            
        # Với các số còn lại trong stack, chúng không có số lớn hơn kế tiếp
        while stack:
            mapping[stack.pop()] = -1
            
        # Ánh xạ kết quả từ nums1 dựa trên dictionary đã xây dựng
        return [mapping[num] for num in nums1]