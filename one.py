import os
import shutil
target ='practice'
os.chdir("C:\\newone\\practice")
print(os.getcwd())
filenames = os.listdir(".")

for file_ in filenames:
    dirname = file_.split(".")[-1]
    os.makedirs(dirname, exist_ok= True)
    src = file_
    dst = os.path.join(dirname, file_)
    shutil.move(src,dst)

