class Car :
    wheel = 4
    def __init__(self,make,model,year,color) -> None:
        #初始化
            self.make = make
            self.model = model
            self.year = year
            self.color = color

car1 = Car("Toyota","Altis",2021,"藍色")            
car1.wheel = 2
print(car1.wheel)