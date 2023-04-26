from main import file1_path
import time
start_time = time.perf_counter()
print("请输入初始值：")
a = int(input()) - 1
print("请输入终止值：")
b = int(input())
while a < b:
    a = a + 1
    with open(file1_path, 'a') as file_object_w:
        file_object_w.write(str(a) + '\n')
end_time = time.perf_counter()
run_time = end_time - start_time
print(round(run_time, 2))
