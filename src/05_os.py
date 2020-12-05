import os

src_folder = "D:\\pystock\\src"
file_name = "05_os.py"

# os.path.join(폴더이름, 파일이름) → 파일경로
file_path = os.path.join(src_folder,file_name)
print("파일 경로 : ", file_path)

# os.path.basename(파일경로) → 파일 이름
basename = os.path.basename(file_path)
print("파일 이름 : ", basename)

# os.path.getctime(파일경로) → ctime 값, 값이 클수록 최신
src_ctime = os.path.getctime(src_folder)
print("src폴더의 ctime 값 : ", src_ctime )