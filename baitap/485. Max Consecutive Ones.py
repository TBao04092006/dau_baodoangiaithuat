def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
        else:
            # Cập nhật max_count trước khi reset current_count
            if current_count > max_count:
                max_count = current_count
            current_count = 0
            
    # Kiểm tra lần cuối sau khi kết thúc vòng lặp 
    # (trường hợp chuỗi số 1 nằm ở cuối mảng)
    return max(max_count, current_count)