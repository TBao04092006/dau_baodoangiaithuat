def maximumProduct(self, nums):
        # Bước 1: Sắp xếp mảng theo thứ tự tăng dần
        nums.sort()
        
        # Bước 2: So sánh hai trường hợp có thể xảy ra
        # TH1: 3 số cuối cùng (3 số lớn nhất)
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # TH2: 2 số đầu tiên (2 số âm nhỏ nhất) và số cuối cùng (số dương lớn nhất)
        case2 = nums[0] * nums[1] * nums[-1]
        
        # Trả về giá trị lớn hơn
        return max(case1, case2)