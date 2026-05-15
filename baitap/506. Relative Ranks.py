def findRelativeRanks(score):
    # Bước 1: Tạo bản sao và sắp xếp giảm dần
    # sorted_scores sẽ có dạng [10, 9, 8, 4, 3] với Ví dụ 2
    sorted_scores = sorted(score, reverse=True)
    
    # Bước 2: Tạo từ điển để tra cứu hạng dựa trên điểm số
    rank_map = {}
    for i in range(len(sorted_scores)):
        if i == 0:
            rank_map[sorted_scores[i]] = "Gold Medal"
        elif i == 1:
            rank_map[sorted_scores[i]] = "Silver Medal"
        elif i == 2:
            rank_map[sorted_scores[i]] = "Bronze Medal"
        else:
            rank_map[sorted_scores[i]] = str(i + 1)
            
    # Bước 3: Duyệt mảng gốc để lấy kết quả theo đúng thứ tự ban đầu
    return [rank_map[s] for s in score]