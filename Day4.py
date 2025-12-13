# class car:
#     wheels = 4
#     def start_car(self):
#         print("Car started")

#     def exampe_one(self):
#         print(self.wheels)
#         self.start_car()

# car1=car()
# print(car1.wheels)
# car1.start_car()
# car1.exampe_one()

class car:
    wheel=4
    def sample(self,brand, model, price, milage):
        print(brand, model, price, milage)
    def sample2(self):
        print(self.wheel)

car1=car()
car1.sample("Honda","Amaze",900000,14.5)
car1.sample2()