class Animal:
    def make_sound(self):
        print("動物發出聲音")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # 使用 super() 調用父類的 make_sound 方法
        print("汪汪！")

dog = Dog()
dog.make_sound()