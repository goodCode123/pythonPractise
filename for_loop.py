for x in range(1, 11):
    print(x)

    my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num == 3:
        continue
    else:
        print(num)

# 字典 dic

my_dict = {"a": 1, "b": 2}
for key in my_dict:
    print(key)

# 使用 for 迴圈遍歷字典的值
for value in my_dict.values():
    print(value)

# 使用 for 迴圈遍歷字典的鍵值對
for key, value in my_dict.items():
    print(key, value)
