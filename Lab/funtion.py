def x():
    print("Hello world")
def tinhTong(*giatri):
    tong = 0
    for i in giatri:
        tong += i
    print("Tổng các giá trị là:", tong)
tinhTong(1,2,3)