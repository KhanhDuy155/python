"""
Hàm ceil : làm tròn lên số nguyên gần nhất
floor : làm tròn xuống số nguyên gần nhất
round : làm tròn số nguyên phụ thuộc vào phần thập phân.
Cho số thực X nhiệm vụ của bạn là 
sử dụng 3 hàm trên để tìm số nguyên nhỏ hơn gần X nhất, 
số nguyên lớn hơn gần X nhất, số nguyên gần X nhất.
"""
from math import *
x = float(input())
print(floor(x))
print(ceil(x))
print(round(x))