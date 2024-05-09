try:
    str = r"D:\demo.txt"

    with open(str, 'r', encoding='utf-8') as file: 
        print(file.read())

except Exception as e:
    # 如果发生其他异常，可以通过 Exception 捕获并打印异常信息
    print("发生了异常:", e)        