#Thư viện toán học
print("---------------------------")
print("Thư viện toán học!")
print("import math")
import math
print("---------------------------")
#Import tất cả hàm trong module
#=> Nên không cần module. nữa 
print("from math import *")
from math import *
print("---------------------------")
#In ra tất cả các hàm toán học
#print(help(math))
print("print(help(math))")
print("---------------------------")
#sqrt: square root :Hàm căn bậc 2
print("sqrt: square root : Căn bậc 2")
print("Cách 1: math.sqrt(2)")
print("math.sqrt(2) =",math.sqrt(2))
print("Cách 2: sqrt(2)")
print("sqrt(2) =",sqrt(2))
print("---------------------------")
#isqrt: integer square root: Hàm căn bậc 2 lấy số nguyên
print("isqrt: integer square root: Hàm căn bậc 2 lấy số nguyên")
print("Cách 1: math.isqrt(39)")
print("math.isqrt() =",math.isqrt(39))
print("Cách 2: isqrt(39)")
print("isqrt(39) =",isqrt(39))
print("---------------------------")
#pow : power : Hàm lũy thừa
print("pow : power : Hàm lũy thừa")
print("pow(2,10) =",pow(2,10))
print("---------------------------")
#ceil : ceiling : Trần nhà
#Hàm làm tròn lên số nhỏ nhất mà lớn hơn x kiểu integer
print("ceil : ceiling : Trần nhà")
print("Hàm làm tròn lên số nhỏ nhất mà lớn hoặc bằng x kiểu integer")
print("ceil(3.23) =",ceil(3.23))
print("---------------------------")
#floor : Sàn nhà
#Hàm làm tròn xuống, nhỏ hơn hoặc bằng x kiểu integer
print("floor: Trần nhà")
print("Hàm làm tròn xuống, nhỏ hơn hoặc bằng x kiểu integer")
print("floor(3.231) =",floor(3.231))
print("---------------------------")
#factorial: Hàm giai thừa
print("factorial: Hàm giai thừa")
print("factorial(5) =",factorial(5))
print("---------------------------")
#gcd: Greatest common divisỏ : Hàm ước chung lớn nhất
print("gcd: Greatest common divisior : Hàm ước chung lớn nhất")
print("gcd(2,4) =",gcd(2,4))
print("---------------------------")
#comb: Tổ hợp chập k của n
#C(n,k)
print("comb: Tổ hợp chập k của n")
print("comb(5,3) = ",comb(5,3))
print("---------------------------")
#fabs:  Hàm giá trị tuyệt đối
print("fabs: Hàm giá trị tuyệt đối")
print("fabs(-2) =",fabs(-2))
print("------------------------------------------------------")
#Built-in function
#Hàm có sẵn không phụ thuộc vào thư viện math
print("Built-in function")
print("Hàm có sẵn không phụ thuộc vào thư viện math")
print("---------------------------")
#abs: Hàm giá trị tuyệt đối
print("abs: Hàm giá trị tuyệt đối")
print("abs(-123) =",abs(-123))
print("---------------------------")
#round: Hàm làm tròn
#Lớn hơn bằng 0.5 thì làm tròn lên
#Nhỏ hơn 0.5 thì lằm tròn xuống
print("round: Hàm làm tròn")
print("Lớn hơn bằng 0.5 thì làm tròn lên")
print("Nhỏ honw 0.5 thì làm tròn xuống")
print("round(4.5431) =",round(4.5431))
print("---------------------------")
#max: Tìm số lớn nhất
#min: Tìm số nhỏ nhất
print("max: Tìm số lớn nhất")
print("min: Tìm số nhỏ nhất")
print("max(1,2,4,3) =",max(1,2,4,3))
print("min(1,2,4,3) =",min(1,2,4,3))
print("---------------------------")
#sum: Hàm tính tổng: Dùng trong list
print("sum: Hàm tính tổng: Dùng trong list")
print("sum([1,2,3,4]) =",sum([1,2,3,4]))