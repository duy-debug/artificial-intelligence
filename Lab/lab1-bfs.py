'''
Breath first search (BFS)
Vi du 3, chuong 2
'''
# doc file
def readfile(filename):
    with open(filename,'r') as f:
        n = int(f.readline().strip()) # đọc một dòng
        adj = []
        for i in range(0,n,1):
            line = list(map(int,f.readline().split()))
            adj.append(line)
            print(line)
    return n,adj
# bfs
def bfs(n,adj,start,stop):
    open = [start]  # Danh sách mở
    close = []      # Danh sách đóng
    flag = False  # Cờ để kiểm tra nếu đã tìm thấy đích
    cha =[-1]*(n)  # Mảng cha để lưu đường đi
    while len(open) > 0:
        cur = open.pop(0)  # Lấy đỉnh đầu tiên trong danh sách mở
        print(f"cur={cur}")
        # chen dinh cur vao danh sach close
        close.append(cur)
        # neu la dinh ket thuc
        if cur == stop:
            flag = True
            # in ra duong di
            print(f"cha = {cha}")
            print(f"Duong di tu {start} -> {stop} la: ", end="")
            i = stop
            while i != -1:
                print(i, end='<-')
                i = cha[i]
            return
        else:
            # di tim cac dinh ke cua cur
            Tn=[] # reset Tn
            for m in range(n):
                if (adj[cur][m] == 1 and (m not in open and m not in close)):
                    Tn.append(m)
                    cha[m] = cur  # Lưu cha của đỉnh m
            print(f"Tn={Tn}")
            # chen Tn vao danh sach open
            open = open + Tn
            print(f"open={open}")
    # het while, in ra khong co duong di
    print(f"Khong co duong di tu {start} den {stop}")
# main
if __name__ == "__main__":
    n,adj = readfile('lab1.txt')
    print("Số đỉnh:", n)
    bfs(n, adj, 0, 6)  # Bắt đầu từ đỉnh 0 đến đỉnh 8
    # Bạn có thể thêm các đoạn code khác để xử lý dữ liệu từ file nếu cần