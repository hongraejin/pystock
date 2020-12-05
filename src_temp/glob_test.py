import glob
import os

folder_path = "D:\\pystock\\src_temp"
py_type = "*.py"

# src_temp 폴더의 모든 파일경로 추출
files = glob.glob(os.path.join(folder_path,"*"))
print(files)

# src_temp 폴더의 모든 .py 파일경로 추출
py_files = glob.glob(os.path.join(folder_path,"*.py"))
print(py_files)
