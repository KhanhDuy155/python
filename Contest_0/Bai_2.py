"""
Đề bài yêu cầu bạn nhập : 
Dòng 1 là số nguyên X 
Dòng 2 là số nguyên Y
Dòng 3 là kí tự C
Dòng 4 là số thực float F
Dòng 5 là số thực double D. 
Nhiệm vụ của bạn là in ra 5 dòng. 
Dòng 1 in X, 
Dòng 2 in Y, 
Dòng 3 in C, 
Dòng 4 in F với 2 số đằng sau dấu phẩy, 
Dòng 5 in D với 9 số sau dấu phẩy.
"""
x = int(input())
y = int(input())
c = str(input())
f = float(input())
d = float(input())
print(x,"\n",y,"\n",c,"\n","%.2f" %f,"\n%.9f"%d,sep = "")