def threeSumClosest(nums, target):
        # 1. Sắp xếp mảng để dùng con trỏ
        nums.sort()
        n = len(nums)
        
        # Giả định tổng gần nhất đầu tiên là tổng của 3 số đầu
        gan_nhat = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Hai con trỏ: l (trái) và r (phải)
            l = i + 1
            r = n - 1
            
            while l < r:
                tong_hien_tai = nums[i] + nums[l] + nums[r]
                
                # Nếu tìm thấy tổng bằng đúng target thì trả về luôn
                if tong_hien_tai == target:
                    return tong_hien_tai
                
                # Cập nhật tổng gần nhất nếu khoảng cách mới nhỏ hơn
                if abs(tong_hien_tai - target) < abs(gan_nhat - target):
                    gan_nhat = tong_hien_tai
                
                # Dịch chuyển con trỏ để tiến gần target hơn
                if tong_hien_tai < target:
                    l += 1
                else:
                    r -= 1
                    
        return gan_nhat