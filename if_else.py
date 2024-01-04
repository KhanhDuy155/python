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