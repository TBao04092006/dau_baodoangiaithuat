def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        # Tìm chỉ số ở giữa (tránh tràn số trong một số ngôn ngữ khác)
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # Target nằm bên phải, thu hẹp phạm vi sang phải
            left = mid + 1
        else:
            # Target nằm bên trái, thu hẹp phạm vi sang trái
            right = mid - 1
            
    # Nếu thoát vòng lặp mà không tìm thấy
    return -1