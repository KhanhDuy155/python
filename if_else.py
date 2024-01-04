# Cấu trúc rẽ nhánh (if else) trong python
print("Cấu trúc rẽ nhánh (if else) trong python")
print("---------------------------")
#if : nếu
print("if: Nếu")

"""
_if được sử dụng khi bạn cần kiểm tra điều kiện nào đó
trước khi thực hiện một hay nhiều câu lệnh.
_Các câu lệnh bên trong if được thụt lề so với if 
"""
print("if được sử dụng khi bạn cần kiểm tra điều kiện nào đó")
print("trước khi thực hiện một hay nhiều câu lệnh.")
print("Các câu lệnh bên trong if được thụt lề so với if.")
"""
_Cú pháp
    if condition:
        #code
"""
print("Cú pháp")
print("\tif condition:")
print("\t\t#code")
if 10<20:
    print("")
print("if 10<20:")
print("    print(Đúng)")
print("---------------------------")
#and or not
print("and or not")
print("if(10<20)and(10>2):")
print("print(Đúng)")
if(10<20)and(10>2):
    print("")
print("---------------------------")
#else 
print("else")
"""
Else được sử dụng trong trường hợp condition 
bên trong if là sai.
"""
print("Else được sử dụng trong trường hợp condition ")
print("bên trong if là sai.")
"""
Cú pháp
    if condition:
        #code if condition is True
    else 
        #code if condition is False
"""
print("Cú pháp")
print("\tif condition:")
print("\t\t#code if condition is True")
print("\telse:")
print("\t\t#code if condition is False")
print("---------------------------")
#elif: else if
print("elif: else if")
print("Cú pháp")
print("\tif condition:")
print("\t\t#code1")
print("\telif condition:")
print("\t\t#code2")
print("\t...")
print("\telif condition:")
print("\t\t#codeN")
print("\telse condition:")
print("\t\t#codeElse")
print("------------------------------------------------------")
#Shorthand if và toán tử 3 ngôi
print("Shorthand if và toán tử 3 ngôi")
print("---------------------------")
#Shorthand if:
#Bạn có thể sử dụng câu lệnh if trên 1 dòng
"""
Nếu trong if có nhiều câu lệnh, bạn có thể
đặt dấu chám phẩy giữa các câu lệnh
"""
print("Shorthand if:")
print("Bạn có thể sử dụng câu lệnh if trên 1 dòng")
a,b = 100,200
if a<b: print(a,"less than",b); print("abc")
print("a,b = 100,200")
print("if a<b: print(a,less than,b);print(abc)")
if a<b: print("=>",a,"less than",b,"\n=> abc")

print("---------------------------")

#Toán tử 3 ngôi
print("Toán tử 3 ngôi")
"""
Cú pháp
    variable = statement if condition else statement
                    ||                          ||
                 True branch                False branch
"""
print("Cú pháp")
print("\tvariable = statement if condition else statement")
print("\t\t\t||\t\t\t||")
print("\t\t   True branch\t\t   False branch")
a,b  = 100,200
res = "Duy" if a < b else "python"
print("a,b  = 100,200")
print("res = Duy if a < b else python")
print("print(res)")
print("=>",res)
print("---------------------------")
#if lồng nhau
print("if lồng nhau")
"""
Khi điều kiện trong if quá phức tạp, bạn có thể sử dụng
if lồng nhau (nested if) để kiểm tra từng điều kiện một.
"""
"""
Cú pháp:
    if condition1:#code
        if condition2:#code
            ...
    else #code        
"""


