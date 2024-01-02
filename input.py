print("-----------------------------")
#Nhập input
print("Nhập input!")
"""
Cú pháp
    input(prompt)
Giá trị trả về: input() trả về xâu kí tự ở kiểu str,
Cần ép sang kiểu tương ứng
"""
s = input("Nhập chuỗi kí tự bất kì: ")
print("Chuỗi kí tự vừa nhập:",s)
print(type(s))
a = int(input("Nhập số nguyên: "))
print("Số nguyên vừa nhập:",a)
print(type(a))
print("-----------------------------")
#Nhập input nhiều số
print("Nhập input nhiều số!")
"""
Bước 1: Nhập cả dòng bằng input
Bước 2: Dùng hàm split để tách các số trong xâu input ra
Bước 3: Sử dụng map để ếp các xâu được tách ra trong input
        sang số int hoặc float tuỳ theo đề bài
"""
print("-----------------------------")
print("Bước 1: Nhập cả dòng bằng input")
print("s = input()")
s = input("Nhập 3 số x,y,z: ")
print("Bước 2: Dùng hàm split để tách các số trong xâu input ra")
print("a = s.split()")
a = s.split()
print("Bước 3: Sử dụng map để ếp các xâu được tách ra trong input sang số int hoặc float tuỳ theo đề bài")
print("x,y,z = map(int,a)")
x,y,z = map(int,a)
print("x = ",x,"\n","y = ",y,"\nz = ",z,sep ="")
print("-----------------------------")
print("Rút gọn!")
print("x,y,z = map(int,input().split())")
x,y,z = map(int,input("Nhập 3 số x,y,z: ").split())
print("x = ",x,"\n","y = ",y,"\nz = ",z,sep ="")