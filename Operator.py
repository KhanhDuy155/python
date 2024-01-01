print("-----------------------------")
#Toán tử
print("Toán tử")
print("-----------------------------")
#Toán tử gán
print("Toán tử gán!")
a = 1000
b = a  # b = 1000
print(a)
print(b)
#Gán nhiều biến trên cùng 1 dòng
print("Gán nhiều biến trên cùng 1 dòng!")
a,b,c = 100,"Duy",True
print(a,b,c,sep = "\n")
#Hoán vị 2 toán tử
print("Hoán vị 2 toán tử!")
a,b = b,a
print(a,b,sep = "\n")
print("-----------------------------")
#Toán tử toán học
print("Toán tử toán học!")
a = 10
b = 2
print("a = ",a,"\n","b = ",b,sep = "")
print("Toán tử  + ")
print("a+b =",a+b)
print("Toán tử  - ")
print("a-b = ",a-b)
print("Toán tử nhân * ")
print("a*b = ",a*b)
print("Toán tử  chia thập phân / ")
print("a/b =",a/b)
print("Toán tử chia nguyên //")
print("a//b =",a//b)
print("Toán tử chia dư %")
print("a%b =",a%b)
print("Toán tử lũy thừa **")
print("a**b =",a**b)
print("-----------------------------")
#Toán tử so sánh
print("Toán tử so sánh!")
a = 100 
b = 200
print("a = ",a,"\n","b = ",b,sep ='')
print("So sánh bằng == ")
print("a == b ->",a==b)
print("So sánh lớn hơn > ")
print("a > b ->",a>b)
print("So sánh lớn hơn hoặc bằng >= ")
print("a >= b ->",a>=b)
print("So sánh nhỏ hơn < ")
print("a < b ->",a<b)
print("So sánh nhỏ hơn hoặc bằng <= ")
print("a <= b ->",a<=b)
print("So sánh khác != ")
print("a != b ->",a!=b)
print("-----------------------------")
#Toán tử logic
print("Toán tử logic!")
"""
AND - Toán tử và
| a | b | a and b |
| 1 | 1 |    1    |
| 1 | 0 |    0    |
| 0 | 1 |    0    |
| 0 | 0 |    0    |
(20==20) and (1<0) -> Talse
OR - Toán tử hoặc
| a | b | a or b |
| 1 | 1 |    1   |
| 1 | 0 |    1   |
| 0 | 1 |    1   |
| 0 | 0 |    0   |
(20==20) or (1<0) ->True
NOT - Toán tử phủ định
not(20==20) -> False
"""
print("Toán tử và and ")
print("(20==20) and (1<0) ->",(20==20) and (1<0))
print("Toán tử hoặc or ")
print("(20==20) or (1<0) ->",(20==20) or (1<0))
print("Toán tử phủ định not ")
print("not (20==20) ->",not(20==20))
print("-----------------------------")
print("Toán tử nhận dạng!")
#Toán tử nhận dạng
"""
Toán tử nhận dạng được sử dụng so sánh
2 đối tượng (2 địa chỉ,id) chứ không phải 
so sánh 2 giá trị
| Toán tử  |     Ý nghĩa                            | 
|   is     | Trả về True nếu 2 đối tượng giống nhau |
|   is not | Trả về True nếu 2 đối tượng khác nhau  |
"""
a = [1,2,3]
b = [1,2,3]
print("a =",a)
print("b =",b)
print("Toán tử nhận dạng is ")
print("a is b ->", a is b)
print("Toán tử nhận dạng is not ")
print("a is not b ->", a is not b)
print("-----------------------------")
print("Toán tử thành viên!")
#Toán tử thành viên
"""
Toán tử thành viên được dùng để kiểm tra
sự tồn tại của 1 đối tượng trong list, xâu, tuple...
| Toán tử |    Ý nghĩa                | Ví dụ             | Kết quả  |
|   in    | Trả về True nếu đối tượng | 'a' in 'abcd'     |   True   |
|         |    kiểm tra tồn tại       |                   |          |
| not in  | Trả về True nếu đối tượng | 'a' in not 'Duy'  |   True   |
|         |    kiểm tra không tồn tại |                   |          |
"""
s = 'Nguyễn Khánh Duy lớp 64ANM2 2251272688'
print("s =",s)
print("'a' in s ->", 'a' in s)
print("'a' not in s ->", 'a' not in s)
print("-----------------------------")