"""
Cho 4 số X, Y, Z, T là số nguyên được nhập từ bàn phím. 
Bạn hãy in ra 3 dòng: 
Dòng 1 lần lượt 4 số Y,Z,X,T mỗi số cách nhau một dấu phẩy 
Dòng 2 in ra tổng 4 số 
Dòng 3 in ra giá trị của biểu thử X - Y + Z * T. 
(Chú ý giá trị của tích Z * T và giá trị của tổng 4 số có thể tràn kiểu dữ liệu int)
"""
x,y,z,t = map(int,input().split())
print(y,z,x,t,sep = ",")
print(x+y+z+t)
print(x-y+z*t)