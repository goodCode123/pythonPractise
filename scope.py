## 變數範圍
a =10
def funtion_one():
    a = 1
    print(a)

    def funtion_two():
        b =2
        print("b:",b)
        print("a:",a)

    funtion_two()
funtion_one()