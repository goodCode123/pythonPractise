class Car :
    def __init__(self,make,model,year,color) -> None:
        #初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print(self.model + "正在行駛") 

    def stop(self):
        print(self.model + "停下來")        

car1 = Car("Toyota","Altis",2021,"藍色")

car2 = Car("Ford","Kuga",2021,"藍色")


print(car1.color)
car1.drive()
