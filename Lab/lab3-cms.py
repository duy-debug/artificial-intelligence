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
def CMS(sodinh, adj, start, stop):
    g = [float('inf')] * sodinh  # Chi phí từ đỉnh bắt đầu đến đỉnh i
    print(g)
    g[start] = 0
    open = [start]
    close = []
    father = [-1] * sodinh  # Mảng cha để lưu đường đi
    while len(open) > 0:
        n = open.pop(0)
        print(f"n={n}")
        close.append(n)
        print(f'close={close}')
        father = [-1] * sodinh
        if n == stop:
            print(f"Đã tìm thấy đường đi từ {start} đến {stop}")
            # in ra đường đi
            i = stop
            while i != -1:
                print(chr(i+65), end='<-')
                i = father[i]
            return True
        Tn = []
        for i in range(sodinh):
            if adj[n][i] != 0:
                if i not in open and i not in close:
                    g[i] = g[n] + adj[n][i]  # Cập nhật chi phí đến đỉnh i
                    Tn.append(i)
                    father[i] = n  # Lưu cha của đỉnh i
                elif i in open:
                    print(f"Đã có đỉnh {i} trong open")
                    gnew = g[n] + adj[n][i]
                    print(f"g{i}new = {gnew}")
                    if gnew <g[i]:
                        g[i] = gnew
                        father[i] = n
                        
        print(f"Tn={Tn}")
        open = open + Tn
        print(f"open={open}")
        open = sorted(open, key=lambda x: g[x])
        print(f"open sorted={open}") 
    print("Khong tim thay duong di tu {start} den {stop}")  
if __name__ == "__main__":
    sodinh, adj = readmtk('lab3-cms.txt')
    CMS(sodinh, adj, 0, 8)  # Bắt đầu từ đỉnh 0 đến đỉnh 8