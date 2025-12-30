def dfs_with_goal(graph, start, goal):
# Tìm kiếm theo chiều rộng (DFS) với đích
# Hàm bfs_with_goal tìm đường đi từ đỉnh start đến đỉnh goal trong đồ thị graph
# Sử dụng thuật toán DFS để tìm đường đi ngắn nhất
    # Kiểm tra đỉnh tồn tại
    if start not in graph:
        print("Điểm bắt đầu", start, "không có trong đồ thị.")
        return
    if goal not in graph:
        print("Điểm kết thúc", goal, "không có trong đồ thị.")
        return
    stack = [start]           # STACK = {s}
    visited = set()           # Tập các đỉnh đã duyệt
    parent = {start: None}    # Để truy vết đường đi
    while stack:              # While(STACK ≠ ∅)
        n = stack.pop()       # DFS dùng pop cuối danh sách (LIFO)
        if n == goal:
            # Truy vết đường đi từ goal về start
            path = []
            while n is not None:
                path.append(n)
                n = parent[n]
            path.reverse()
            print("Đường đi:", " -> ".join(path))
            return
        if n not in visited:
            visited.add(n)
            # Duyệt ngược để giống thứ tự logic của DFS
            for neighbor in reversed(graph.get(n, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    if neighbor not in parent:
                        parent[neighbor] = n
    print("Không tìm thấy đường đi từ", start, "đến", goal) 
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
dfs_with_goal(graph, 'A', 'G')
