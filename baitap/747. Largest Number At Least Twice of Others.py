def dominantIndex(nums):
        # Khởi tạo giá trị lớn nhất và lớn thứ hai
        max_val = -1
        second_max = -1
        max_index = -1
        
        # Duyệt qua mảng một lần duy nhất
        for i, n in enumerate(nums):
            if n > max_val:
                # Cập nhật số lớn thứ hai trước khi đổi ngôi số lớn nhất
                second_max = max_val
                max_val = n
                max_index = i
            elif n > second_max:
                # Cập nhật số lớn thứ hai nếu n nằm giữa max_val và second_max
                second_max = n
        
        # Kiểm tra điều kiện: số lớn nhất >= 2 * số lớn thứ hai
        if max_val >= 2 * second_max:
            return max_index
        
        return -1
        