fruits = ["蘋果", "柳橙", "香蕉"]
# 蘋果
print(fruits[0])

for items in fruits:
    print(items)

fruits.append("芭樂")

for items in fruits:
    print(items)


fruits.remove("蘋果")
print(fruits)
for items in fruits:
    print(items)

print(fruits.index("香蕉"))
