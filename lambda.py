#Lambda表達式

def double(x):
    return x *2

print(double(5))


double2 = lambda x:x*2
print(double2(50))


mutiply = lambda x , y: x * y
print(mutiply(5,10))


result = lambda x : f"{x} 是偶數" if x % 2 == 0 else f"{x} 是奇數"
print(result(15))