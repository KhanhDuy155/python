#Bài 7. Chữ số cuối cùng và 2 chữ số cuối cùng
"""
Cho nguyên dương N, 
bạn hãy sử dụng phép chia dư để lấy ra chữ số cuối cùng 
và 2 chữ số cuối cùng của N. 
Gợi ý : 
Để lấy chữ số cuối cùng của N bạn chỉ cần lấy N chia dư cho 10. 
Ví dụ N = 1234 % 10 = 4. 
Để lấy 2 chữ số cuối cùng của N bạn chỉ cần lấy N chia dư cho 100. 
Ví dụ N = 1234 % 100 = 34. ....
"""
"""
Đề bài:
Khai báo biến nguyên n
Nhập n từ bàn phím
In ra n % 10
In ra n % 100
}
"""
x = int(input())
print(x%10)
print(x%100)
