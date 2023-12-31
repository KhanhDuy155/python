#Bài 1,2:
"""
    Câu lệnh print:

        print(object, sep = seperator, end = end)

        
Giải thích:
    Object: Các đối tượng trong Python
    Sep: Phân cách giữa các đối tượng khi in, 
            nếu không có tham số thì mặc định sẽ là dấu cách.
    End: Chỉ ra kí tự được in ở cuối dòng, 
            nếu không có tham số này thì mặc địch sẽ là dấu xuống dòng.
"""
# Không có tham số 
print("Nguyễn Khánh Duy")
# Có phân cách sep
print("Nguyễn","Khánh","Duy",sep = "+++")
# Có thêm kí tự cuối cùng
print("Nguyễn","Khánh","Duy",sep = "###",end = "!!!")
