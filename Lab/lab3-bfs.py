# best first search (BFS) using a queue
def readmtk(filename):
    with open(filename) as f:
        sodinh = int(f.readline())
        print(sodinh)
        adj = []
        for i in range(sodinh):
            line = list(map(int, f.readline().strip().split()))
            # strip loai bo ky tu xuong dong o dau va cuoi
            adj.append(line)
            print(line)
    return sodinh, adj
def readh(filename):
    with open(filename) as f:
        h = list(map(int, f.readline().strip().split()))
        print(h)
    return h
def HCS(sodinh, adj, h,start, stop):
    open = [start]
    close = []
    father = [-1] * sodinh  # Mảng cha để lưu đường đi
    print(father)
    while len(open) > 0:
        n = open.pop(0)
        print(f"n={n}")
        close.append(n)
        print(f'close={close}')
        if n == stop:
            print(f"Đã tìm thấy đường đi từ {start} đến {stop}")
            # in ra đường đi
            i = stop
            while i != -1:
                print(i, end='<-')
                i = father[i]
            return True
        # Ngược lại đi tìm các đỉnh kề của n
        Tn = [] # reset Tn
        for i in range(sodinh):
            if adj[n][i] == 1 and (i not in open and i not in close):
                Tn.append(i)
                father[i] = n
        print(f"Tn={Tn}")
        open = Tn + open # chen Tn vao dau danh sach open
        open = sorted(open, key=lambda x: h[x])
        print(f"open={open}")
        print(f"father={father}")
    print(f"Không có đường đi từ {start} đến {stop}")
if __name__ == "__main__":
    sodinh, adj = readmtk('lab3-timkiemleodoi.txt')
    h = readh("lab3-cost.txt")
    HCS(sodinh, adj, h, 0, 8)  # Bắt đầu từ đỉnh 0 đến đỉnh 9