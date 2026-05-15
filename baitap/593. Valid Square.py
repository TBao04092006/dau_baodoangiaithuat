class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def get_dist_sq(pa, pb):
            return (pa[0] - pb[0])**2 + (pa[1] - pb[1])**2
        
        # Danh sách tất cả 6 cặp khoảng cách có thể có
        dists = [
            get_dist_sq(p1, p2), get_dist_sq(p1, p3), get_dist_sq(p1, p4),
            get_dist_sq(p2, p3), get_dist_sq(p2, p4),
            get_dist_sq(p3, p4)
        ]
        
        # Dùng set để lọc các giá trị khoảng cách duy nhất
        dist_counts = set(dists)
        
        # Một hình vuông hợp lệ phải có:
        # 1. Đúng 2 loại khoảng cách (cạnh và đường chéo)
        # 2. Khoảng cách không được bằng 0 (các điểm không trùng nhau)
        return len(dist_counts) == 2 and 0 not in dist_counts