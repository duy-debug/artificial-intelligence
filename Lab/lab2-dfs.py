def readmtk(filename):
    with open(filename) as f:
        sodinh = int(f.readline())
        print(sodinh)
        adj=[]
        for i in range(sodinh):
            line = list(map(int,f.readline().strip().split())) # strip loai bo ky tu xuong dong o dau va cuoi
            # split 
            adj.append(line)
            print(line)
    return sodinh, adj
def DFS(sodinh, adj, start, stop):
    open = [start]
    close = []
    cha = [-1] * sodinh  # Mảng cha để lưu đường đi
    print(cha)
    while len(open) > 0:
        n = open.pop(0) # lay phan tu cuoi cung trong danh sach open 
        print(f"n={n}")
        close.append(n)
        print(f'close={close}')
        if n == stop:
            print(f"Da tim thay duong di tu {start} den {stop}")
            # in ra duong di
            i = stop
            while i != -1:
                print(i,end = '<-')
                i = cha[i]
            return True
        # Nguoc lai di tim cac dinh ke cua n
        Tn = [] # reset Tn
        for i in range(sodinh):
            if adj[n][i]==1 and (i not in open and i not in close):
                Tn.append(i)
                cha[i] = n  # Lưu cha của đỉnh i 
        print(f"Tn={Tn}")
        open = Tn + open # chen Tn vao dau danh sach open
        print(f"open={open}")
        print(f"cha={cha}")
    print(f"Khong co duong di tu {start} den {stop}")
if __name__ == "__main__":
    sodinh, adj = readmtk('lab1.txt')
DFS(sodinh, adj, 0, 7) # Bắt đầu từ đỉnh 0 đến đỉnh 6   