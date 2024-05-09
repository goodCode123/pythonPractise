try:
    # 尝试执行可能会引发异常的代码
    num1 = int(input("请输入第一个整数: "))
    num2 = int(input("请输入第二个整数: "))
    result = num1 / num2
    print("结果为:", result)

except ValueError as ve:
    # 如果输入无法转换为整数，会引发 ValueError 异常
    print("请输入有效的整数。错误原因:", ve)

except ZeroDivisionError as zde:
    # 如果除数为0，会引发 ZeroDivisionError 异常
    print("除数不能为零。错误原因:", zde)

except Exception as e:
    # 如果发生其他异常，可以通过 Exception 捕获并打印异常信息
    print("发生了异常:", e)

else:
    # 如果没有发生异常，则执行这个代码块
    print("程序执行成功。")

finally:
    # 不管是否发生异常，都会执行这个代码块
    print("程序执行结束。")