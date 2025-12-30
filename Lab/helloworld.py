# Dạng chuỗi 1:
ntu = "Trường Đại học Quốc gia Thành phố Hồ Chí Minh"
# Dạng chuỗi 2:
ntu2 = 'Trường Đại học Quốc gia Thành phố Hồ Chí Minh2'
# Dạng chuỗi 3 :
ntu3 = '''Trường Đại học Quốc gia Thành phố Hồ Chí Minh3
Trường Đại học Quốc gia Thành phố Hồ Chí Minh4'''
print(ntu)
print(ntu2)
print(ntu3)
# Kiểu số nguyên
n = 3721
print(n)
# Kiểu số thực
pi = 3.141592653589793
print("pi = %.2f" % pi)
# Kiểu số phức
z = 3 + 4j
print("z = %s" % z)
# Kiểu boolean
is_student = True
print("is_student = %s" % is_student)
# dùng hàm type() để kiểm tra kiểu dữ liệu
print("Kiểu dữ liệu của ntu:", type(ntu).__name__)
print("Kiểu dữ liệu của n:", type(n).__name__)
print("Kiểu dữ liệu của pi:", type(pi).__name__)
print("Kiểu dữ liệu của z:", type(z).__name__)
# LỆNH RẼ NHÁNH IF
# Dạng 1: Lệnh if thiếu
n = 5
if n % 2 != 0: print("n là số lẻ", n) # lệnh đơn

m = 4
if m > 0: # khối lệnh
    print("m =", m)
    print("m là số dương")
# Dạng 2: Lệnh if có lệnh else
if n % 2 == 0:
    print("n là số chẵn", n)
else: 
    print("n là số lẻ", n)
# Trong lệnh if, muốn kiểm tra điều kiện mới khi điều kiện trước không thỏa mãn thì dùng từ khóa elif
# Lệnh lăp while
n = 123
sum = 0
print("n = ", n)
while n > 0:
    sum += n % 10
    n //= 10
print("Tổng các chữ số của n là:", sum)
# Lệnh lặp break
i = 1
while i < 100:
    print(i, end = ' ')
    i+=1
    if i == 5: break
print("\nKết thúc vòng lặp sớm khi i = 5")
#Lệnh continue
i = 0
while i < 10:
    i+= 1
    if i % 2 == 0: continue
    print(i, end = ' ')
print("\nKết thúc vòng lặp khi i là số chẵn")
# Lệnh lặp for
for i in range(1, 11):
    print(i, end = ' ')
arr = ['An','Duy','Hùng','Hải','Hà']
print("\n")
for i in arr: # Duyệt từng phần tử trong mảng
    print(i, end = ' ')
# Duyệt từng phần tử thông qua vị trí trong danh sách
for i in range(len(arr)):
    print(arr[i], end = ' ')
# Duyệt chuỗi
print("\nDuyệt chuỗi:")
st = 'Xin chào các bạn'
for ch in st:
    print(ch)
# In 10 dòng hello world

for i in range(10):
    print("Hello World", end='\n')
    x = "Python" 
