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
def readh(filename):
    with open(filename, 'r') as f:
        h=list(map(int, f.readline().strip().split()))
        print(h)
    return h
def NhanhCan(sodinh,adj,h,start,stop):
    OPEN=[start]
    fmin= float('inf')
    CLOSE=[]
    CHA=[-1]*sodinh
    g=[float('inf')]*sodinh
    f=[float('inf')]*sodinh
    g[start]=0
    f[start]=h[start]
    print(f"g= {g}")
    print(f"f= {f}")
    flag = False
    while len(OPEN) > 0:
        n=OPEN.pop(0)
        print(f"n={n}")
        CLOSE.append(n)
        print(f"CLOSE={CLOSE}")
        if n== stop:
            flag = True
            if f[n] < fmin:
                print(f"fmin={fmin} > {f[n]}:cap nhat fmin = {f[n]}")
                fmin = f[n]
            else:
                print(f"fmin < f[n]")
        elif f[n]<fmin: #n khong la dinh stop va fn <fmin
            print(f"f{n}:{f[n]}<fmin:{fmin} Tim cac dinh ke")
            Tn=[]
            for i in range(sodinh):
                if adj[n][i] > 0: #co dinh ke
                    #TH1 i not in OPEN,CLOSE
                    if i not in OPEN and i not in CLOSE:
                        print(f"{i} not in OPEN,CLOSE")
                        g[i] = g[n] + adj[n][i]
                        f[i] = g[i] + h[i]
                        Tn.append(i)
                        CHA[i] = n 
                    elif i in OPEN and i not in CLOSE:
                        print(f"{i} in OPEN, not in CLOSE")
                        gnew=g[n] + adj[n][i]
                        fnew=gnew + h[i]
                        print(f"fnew = {fnew}")
                        if fnew < f[i] :
                            print(f"fnew <f[{i}]: {fnew}<{f[i]}, update f[{i}]")
                            g[i] = gnew
                            f[i] = fnew
                            CHA[i] = n 
                    #TH3 i not in OPEN, in CLOSE
                    elif i not in OPEN and i in CLOSE:
                        print(f"{i} not in OPEN, in CLOSE")
                        gnew = g[n] + adj[n][i]
                        fnew = gnew + h[i]
                        print(f"fnew = {fnew}")
                        if fnew < f[i]:
                            print(f"fnew < f[{i}]: {fnew}<{f[i]}, update f[{i}]")
                            g[i] = gnew
                            f[i] = fnew
                            CHA[i] = n
                            Tn.append(i)   
                    #TH4 i in OPEN,CLOSE
                    elif i in OPEN and i in CLOSE:
                        print(f"{i} in OPEN,CLOSE")
                        gnew = g[n] + adj[n][i]
                        fnew = gnew + h[i]
                        print(f"fnew = {fnew}")
                        if fnew < f[i]:
                            print(f"fnew < f[{i}]: {fnew}<{f[i]}, update f[{i}]")
                            g[i] = gnew
                            f[i] = fnew
                            CHA[i] = n      
            # sort Tn
            print(f"g={g}")
            print(f"f={f}")
            Tn = sorted(Tn, key=lambda x: f[x])
            print(f"Tn sort={Tn}")
            #Chen Tn vao OPEN
            OPEN =Tn+OPEN
            print(f"OPEN={OPEN}")
            print(f"CHA={CHA}")
        else:
            print(f"f{n}:{f[n]} >= fmin:{fmin}, XEN TIA")
    if not flag:
        print(f"Không tìm thấy đường đi từ {start} đến {stop}")
    else:
        print(f"\nTìm thấy đường đi từ {start} đến {stop}")
        print("Đường đi: ", end="")
        i = stop
        while i != -1:
            print(i, end=" <= " if CHA[i] != -1 else "\n")
            i = CHA[i]
if __name__ == "__main__":
    sodinh,adj=readmtk("nhanhcan1.txt")
    h=readh("nhanhcan.txt")
    NhanhCan(sodinh, adj, h, 0, 1)