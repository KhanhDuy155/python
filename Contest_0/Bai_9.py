#bài 9. Xoá số
"""
Cho số nguyên dương N có ít nhất 5 chữ số, 
nhiệm vụ của bạn là xóa đi 3 chữ số cuối cùng của N và
in ra những chữ số còn lại. 
Ví dụ N = 12345 sau khi xóa đi 3 chữ số cuối cùng thì N = 12. 
Gợi ý, đối với phép chia nguyên nếu bạn muốn xóa đi 1 chữ số cuối cùng chỉ cần lấy N chia nguyên cho 10, 
ví dụ N = 12345 / 10 = 1234, 
tương tự N = 12345 / 100 = 123, N = 12345 / 1000 = 12....
"""
x = int(input())
x = x/10
x = x/10
x = x/10
print(int(x))