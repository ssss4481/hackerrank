import os

problem = input("copy from leetcode title: ").split()
concate_result = '_'.join(problem)
os.system(f"cp ./fast_io.cpp \"./{concate_result}.cpp\"")
os.system(f"code \"./{concate_result}.cpp\"")