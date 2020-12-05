import os

folder_path = "D:\\pystock\\src_temp"
filename = "hello_os.py"

# os.path.join(폴더명, 파일이름) → 파일경로
joined = os.path.join(folder_path, filename)
print("연결된 경로 : ", joined)

# os.path.basename(파일경로) → 파일이름
os_test_path = "D:\\pystock\\src_temp\\os_test.py"
basename = os.path.basename(os_test_path)
print("파일 이름 :" ,basename)

# os.path.getctime(파일경로) → ctime값
ctime = os.path.getctime(folder_path)
print("ctime 값 : ",ctime)
