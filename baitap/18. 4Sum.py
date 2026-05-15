def fourSum(nums, target):
        # 1. Sắp xếp mảng để dùng con trỏ và tránh trùng lặp
        nums.sort()
        n = len(nums)
        res = []
        
        # 2. Vòng lặp i (Cố định số thứ 1)
        for i in range(n - 3):
            # Bỏ qua nếu số này giống số trước đó
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 3. Vòng lặp j (Cố định số thứ 2)
            for j in range(i + 1, n - 2):
                # Bỏ qua nếu số này giống số trước đó trong cùng vòng lặp j
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # 4. Kỹ thuật 2 con trỏ tìm 2 số còn lại (y hệt 3Sum)
                l = j + 1
                r = n - 1
                while l < r:
                    tong = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if tong == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # Bỏ qua các số trùng lặp để không bị kết quả lặp
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif tong < target:
                        l += 1 # Tổng nhỏ quá, tăng bên trái
                    else:
                        r -= 1 # Tổng lớn quá, giảm bên phải
                        
        return res