import glob
import os

src_folder = "D:\\pystock\\src"
py_type = "*.py"

# src 폴더의 모든 파일경로 추출
files = glob.glob(os.path.join(src_folder,"*"))
print(files)

# src 폴더의 모든 .py 파일경로 추출
py_files = glob.glob(os.path.join(src_folder,"*.py"))
print(py_files)
