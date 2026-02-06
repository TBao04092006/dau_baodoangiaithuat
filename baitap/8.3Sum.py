def threeSum(nums):
        # 1. Sắp xếp mảng để dễ dàng dùng 2 con trỏ
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n):
            # Bỏ qua số giống hệt số vừa xét để không bị trùng bộ 3
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Đặt 2 con trỏ: trái (l) và phải (r)
            l = i + 1
            r = n - 1
            
            while l < r:
                tong = nums[i] + nums[l] + nums[r]
                
                if tong == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Tiếp tục bỏ qua các số trùng nhau ở con trỏ trái
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif tong < 0:
                    l += 1 # Tổng nhỏ quá, dịch trái sang phải để tăng tổng
                else:
                    r -= 1 # Tổng lớn quá, dịch phải sang trái để giảm tổng
                    
        return res