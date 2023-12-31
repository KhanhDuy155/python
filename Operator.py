#Toán tử
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