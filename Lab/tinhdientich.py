""" Nhap 3 diem tren he truc toa do Oxy
1. Xac dinh 3 diem co tao thanh mot tam giac hay khong
2. Neu tao thanh tam giac:
   2.a Xuat ra chu vi tam giac
   2.b Xuat ra dien tich tam giac
"""
import math
xa = float(int(input("Nhap hoanh do diem A: ")))
ya = float(int(input("Nhap tung do diem A: ")))
xb = float(int(input("Nhap hoanh do diem B: ")))
yb = float(int(input("Nhap tung do diem B: ")))
xc = float(int(input("Nhap hoanh do diem C: ")))
yc = float(int(input("Nhap tung do diem C: ")))
# Kiem tra 3 diem co tao thanh mot tam giac hay khong
ab = math.sqrt((xb-xa)**2 + (yb - ya)**2)
bc = math.sqrt((xc-xb)**2 + (yc - yb)**2)
ca = math.sqrt((xa-xc)**2 + (ya - yc)**2)
if ab+bc > ca and ab + ca > bc and bc + ca > ab:
    print("3 diem A, B, C tao thanh mot tam giac")
    # Tinh chu vi tam giac
    print("Chu vi tam giac ABC la: {0}".format(ab+bc+ca))
    # Tinh dien tich tam giac
    p = (ab + bc + ca) / 2  # Nua chu vi
    s = math.sqrt(p*(p-ab)*(p-bc)*(p-ca)) # Cong thuc Heron
    print("Dien tich tam giac ABC la: {0}".format(s))
else: 
    print("3 diem A, B, C khong tao thanh mot tam giac")
