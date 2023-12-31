'''
    Kiểu dữ liệu số:-
        int: Số nguyên.
        float: Số thực dấu phẩy động
        Complex number; Số phức

'''
#int 
a = 100
print("Số nguyên: a =",a)
#float
#Giá trị thực lớn nhất là: 1.8x10^308
#Giá trị thực nhỏ nhất là: 5.0x10^-324
#Quá thì kết quả ra: INF
b = 100.1234566
print("Số thực: b =",b)
#In ra biến sau dấu phẩy
print("%.2f" %b)
print("{:.2f}".format(b))
#Complex
c = 100 -50j
print("Số phức: c =",c)
print("Phần thực:",c.real)
print("Phần ảo",c.imag)
#Hệ nhị phân Binary
d = 0b1101
print("Số nhị phân: d =",d)
#Hệ cơ số 10 Octal
e = 0o1505
print("Số thập phân: e =",e)
#hệ thập lục phân 16 Hex
f = 0x22A
print("Số thập lục phân: f =",f)
#Kiểu dữ liệu đúng sai BOOL
true = True
print(type(true))
false = False
print(type(false))
#Các giá trị được xác định là True:
#   Xâu khác rỗng, các số khác 0
print("Số 1 là:",bool(1))
print("Số 0 là:",bool(0))
print("Kí tự khác rỗng là:",bool("Duy đẹp trai"))
print("Kí tự rỗng là:",bool(""))
#Kiểu xâu kí tự STR<string>
s = "Nguyễn Khánh Duy"
print(s,type(s))
s1 = "1231233"
print(s1,type(s1))
#Ép kiểu dữ liệu
s = '121323123312'
a = int(s)
print(s,type(s))
print(a,type(a))
s = '12312.1231'
b = float(s)
print(s,type(s))
print(b,type(b)) 