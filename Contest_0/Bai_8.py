#Bài 8. Phép chia
"""
Đề bài:
1 dòng duy nhất chứa lần lượt 2 số nguyên b và a
Dòng 1 in ra thương của a / b khi sử dụng phép chia nguyên; 
Dòng 2 in ra thương của a / b khi sử dụng phép chia 
lấy phần thập phân với độ chính xác 2 số sau dấu phẩy.
"""
x = input()
b,a = map(float,x.split())
print(int(a/b))
print("%.2f" %(a/b))
