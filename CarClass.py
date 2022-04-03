msg= """This example practice class in Python
============================================"""
print(msg)
class Car:
  def  __init__(self,make,model,year):
     self.make=make
     self.model=model
     self.year=year
     self.odo=0
  def change_name(self,new_name):
      self.name=new_name
  def change_model(self,new_model):
      self.model=new_model
  def print_out(self):
    msg=f"Car's make: {self.make}, Model: {self.model}, Year: {self.year}, Odo reading: {self.odo} \n This car has {self.odo} miles"
    print(msg)
  def set_odo(self,new_mile):
      self.odo=new_mile
  def update_odo(self,new_mile):
      self.odo=self.odo+new_mile

my_car = Car("Toyota","Camry Hybrid", 2012)
my_car.print_out()
her_car = Car("Honda Civid", "XLE", 2021)
her_car.print_out()

my_car.change_name("tesla")
my_car.print_out()
my_car.set_odo(12321)
my_car.print_out()
my_car.update_odo(230)
my_car.print_out()

message= """This example practice inheritance in Python
 ===================================================="""
class ElectricCar(Car):
    def __init__(self,make,model,year,battery):
         super().__init__(make,model,year)
         self.battery=battery
    def print_out(self):
     msg1=f"Car's make: {self.make}, Model: {self.model}, Year: {self.year}, Odo reading: {self.odo} \n This car has {self.odo} miles \n This car has {self.battery}% battery"
     print(msg1)
my_tesla=ElectricCar("Tesla","Model 3",2022,100)
my_tesla.set_odo(2320)
my_tesla.print_out()
my_tesla.change_name("Audi")
my_tesla.print_out()
my_tesla.change_name("Hello")
my_tesla.print_out()

