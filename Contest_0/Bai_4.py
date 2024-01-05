"""
Cho 2 số x, y. Nhiệm vụ của bạn là tính x ^ y

Gợi ý : x^y sẽ không có phần lẻ thập phân vì x, y đều nguyên. 
Hàm pow trả về double 
nên bạn không được in ra luôn cout << pow(x, y). 
Với kết quả nhỏ thì không sao nhưng nếu kết quả lớn nó sẽ in ra dạng số thực
bạn thử cout << pow(10, 10) để xem thử kết quả. 
Cách làm đó là ép pow sang long long trước khi in 
hoặc lưu pow(x, y) vào 1 số nguyên long long rồi in ra.
"""
from math import *
x,y = map(int,input().split())
print(int(pow(x,y)))