with open("1.txt", encoding = "utf-8") as f1:
    content1 = f1.readlines()
with open("2.txt", encoding = "utf-8") as f2:
    content2 = f2.readlines()
with open("3.txt", encoding = "utf-8") as f3:
    content3 = f3.readlines()

files = [('1.txt', len(content1)), ('2.txt', len(content2)), ('3.txt', len(content3))]

files_sorted = sorted(files, key=lambda x: x[1])

with open("4.txt", "w") as f:
    for file_info in files_sorted:
        f.write(file_info[0] + '\n')
        f.write(str(file_info[1]) + '\n')
        if file_info[0] == '1.txt':
            f.writelines(content1)
        elif file_info[0] == '2.txt':
            f.writelines(content2)
        elif file_info[0] == '3.txt':
            f.writelines(content3)