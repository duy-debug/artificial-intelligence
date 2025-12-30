from collections import deque
# Tìm kiếm theo chiều rộng (BFS) với đích
# Hàm bfs_with_goal tìm đường đi từ đỉnh start đến đỉnh goal trong đồ thị graph
# Sử dụng thuật toán BFS để tìm đường đi ngắn nhất
def bfs_with_goal(graph, start, goal):
        # Kiểm tra xem đỉnh bắt đầu và kết thúc có tồn tại không
    if start not in graph:
        print("Điểm bắt đầu", start, "không có trong đồ thị.")
        return
    if goal not in graph:
        print("Điểm kết thúc", goal, "không có trong đồ thị.")
        return
    open_set = deque([start])      # OPEN = {s}
    close_set = set()              # CLOSE = ∅
    parent = {start: None}         # Để truy vết đường đi
    while open_set:                # While(OPEN ≠ ∅)
        n = open_set.popleft()     # n = Retrieve(OPEN)
        close_set.add(n)           # CLOSE = CLOSE ∪ {n}
        if n == goal:              # Nếu là đỉnh đích
            # Truy vết đường đi từ goal về start
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]
            path.reverse()
            print("Đường đi:", " -> ".join(path))
            return
        # Xét các đỉnh kề của n
        for neighbor in graph[n]:  # Γ(n): các đỉnh đi trực tiếp từ n
            if neighbor not in open_set and neighbor not in close_set:
                open_set.append(neighbor)      # Open = Open ∪ Γ(n)
                parent[neighbor] = n           # Ghi nhận cha của đỉnh kề
    print("Không tìm thấy đường đi", start, "to", goal)
# Đồ thị ví dụ
graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['F','G'],
    'D': [],
    'E': ['H','I'],
    'F': ['J'],
    'G': []
}

# Chạy từ A đến F
print("Tìm đường từ A đến G:")
bfs_with_goal(graph, 'A', 'G')
