def readmtk(filename):
    with open(filename, 'r') as f:
        sodinh =int(f.readline().strip())
        print(sodinh)
        adj=[]
        for i in range(sodinh):
            line = list(map(int, f.readline().strip().split()))
            print(line)
            adj.append(line)
    return sodinh, adj     
def tomau(sodinh, adj):
    bac=[0]*sodinh
    for i in range(sodinh):
        for j in range(sodinh):
            if adj[i][j] == 1:
                bac[i] += 1
    print(f"Bac do thi:{bac}")
    OPEN=[]
    for i in range(sodinh):
        OPEN.append(i)
    print(f"OPEN:{OPEN}")
    #sap xep cac dinh giam dan theo bac
    OPEN.sort(key=lambda x: bac[x],reverse=True)
    print(f"OPEN sort:{OPEN}")
    mau=0
    color = [-1]*sodinh # -1 la chua to mau
    while len(OPEN)>0:
        n=OPEN.pop(0)  # lay dinh dau tien trong OPEN
        print(f"n={n}")
        color[n] = mau
        #TIm cac dinh khong ke voi n de to mau
        Tn=[]
        for i in range(sodinh):
            if adj[n][i] == 0 and color[i] == -1: # chua to mau
                #Dua cac dinh tim nang
                Tn.append(i)
        print(f"Tn={Tn}")
        #CHi giu lai cac dinh khong ke nhau trong Tn
        for i in Tn:
            for j in Tn:
                if i!=j and adj[i][j] == 1:
                    Tn.remove(j)
        print(f"Tn sau khi xoa dinh ke nhau: Tn={Tn}")
        #to mau
        for i in Tn:
            color[i] = mau
                #Xoa dinh da to mau khoi OPEN
            OPEN.remove(i)
        print(f"Color={color}")
        print(f"OPEN={OPEN}")
        mau+=1 #tang mau de to dinh tiep theo
    #het dinh stop
if __name__ == "__main__":
    sodinh,adj=readmtk("tomau.txt")
    tomau(sodinh, adj)
    