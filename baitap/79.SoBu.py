def findComplement(num):
    # Tìm độ dài bit của số num
    # Ví dụ: num = 5 (101), độ dài là 3
    bit_length = num.bit_length()
    
    # Tạo một mask toàn số 1 có độ dài tương ứng
    # (1 << 3) là 1000 (số 8), trừ đi 1 thành 0111 (số 7)
    mask = (1 << bit_length) - 1
    
    # Dùng phép XOR để đảo bit
    return num ^ mask