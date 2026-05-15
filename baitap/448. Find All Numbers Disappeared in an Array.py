def findDisappearedNumbers(nums):
    # Tạo một tập hợp chứa tất cả các số từ 1 đến n
    n = len(nums)
    all_numbers = set(range(1, n + 1))
    
    # Tạo tập hợp từ mảng nums hiện có
    exist_numbers = set(nums)
    
    # Kết quả là hiệu của hai tập hợp (những số có trong all_numbers nhưng không có trong exist_numbers)
    return list(all_numbers - exist_numbers)