#declaring class with class name
class Vehicle:
    #defining the constructor by taking attributes
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
    #instance methods for the class vehicle
    print("****************************Vehicle******************************")
    def get_make(self): 
        print(f"Get the design {self.make}")    
    def get_model(self):
        print(f"Get the vehicle model {self.model}")
    def get_year(self):
        print(f"Get the vehicle manufactured year {self.year}")   
    def update_mileage(self,new_mileage):
        self.mileage=new_mileage
        print(f"Update the mileage {self.mileage}")   
    def calculate_maintenance_cost(self,cost):
        self.cost=cost
        print(f"Maintenance cost:{self.cost} ")
    print()
    def display_info(self):
       print("*****************displaying information**********************")
       print(f"Get design: {self.make} \nGet the model name: {self.model} \nGet the vehicle manufactured year: {self.year} \nGet the mileage of the vehicle: {self.mileage} \nGet the maintenance cost: {self.cost}")
       print("*****************displaying information**********************")
       print() 
       
    #static method for the class Vehicle
    @staticmethod
    def validate_registration(format):
        print("*****************static method**********************")
        return "valid format" if format=="AP0912" else "Invalid format"
        
    #class method for the class Vehicle
    total_count=4
    @classmethod
    def get_total_count(cls):  
        return cls.total_count


#creating subclass car for vehicle 
class Car(Vehicle):
    def __init__(self,fuel_type,transmission_type,total_count,registration_format):
        self.fuel_type=fuel_type
        self.transmission_type=transmission_type
        self.total_count=total_count
        self.registration_format=registration_format
    #static methods for the subclass Car
    def calculate_tax(tax):
        tax=80000
        return tax
    def calculate_insurance_premium(cost):
        insurance_premium=cost
        return insurance_premium
        

#creating subclass truck for vehicle 
class Truck(Vehicle):
    def __init__(self,load_capacity,fuel_efficiency,total_count,registration_format):
        self.load_capacity=load_capacity
        self.fuel_efficiency=fuel_efficiency
        self.total_count=total_count
        self.registration_format=registration_format

    #static methods for the subclass truck 
    def calculate_fuel_cost(cost):
        cost=1000
        return cost
    def calculate_depreciation(cost):
        cost=800000
        return cost

#creating subclass motorcycle for vehicle   
class Motorcycle(Vehicle):
    def __init__(self,engine_capacity,fuel_capacity,total_count,registration_format):
        self.engine_capacity=engine_capacity
        self.fuel_capacity=fuel_capacity
        self.total_count=total_count
        self.registration_format=registration_format

    #static method for the subclass motorcycle
    def check_engine_status(status):
        status="Good"
        return status
    #static method for the subclass motorcycle
    def calculate_acceleration(time,speed):
        acceleration=speed/time
        return acceleration
        
#creating subclass bicycle for vehicle  
class Bicycle(Vehicle):
    def __init__(self,frame_material,tire_size,total_count,registration_format):
        self.frame_material=frame_material
        self.tire_size=tire_size
        self.total_count=total_count
        self.registration_format=registration_format
    #static method for the subclass bycycle
    def check_tire_pressure(pounds):
        tire_pressure=pounds
        return tire_pressure
    def calculate_speed(distance,time):
        speed=distance/time
        return speed
    


# Creating an object for the class Vehicle
vehicle = Vehicle("Toyota","BMW", 2011, 10000)

# Calling instance methods of Vehicle
vehicle.get_make()
vehicle.get_model()
vehicle.get_year()
vehicle.update_mileage(55000)
vehicle.calculate_maintenance_cost(10000)
vehicle.display_info()

# Calling static method of Vehicle
print(Vehicle.validate_registration("AP0912"))

print("****************class method*******************")
print(Vehicle.get_total_count())

print("****************Car*******************")

# Creating an object for the subclass Car
car = Car("Petrol", "Automatic", 1, "AP1234")

# Calling static methods of Car
print(Car.calculate_tax(80000))
print(Car.calculate_insurance_premium(10000))

print("****************truck*******************")

# Creating an object for the subclass Truck
truck = Truck(5000, 15, 1, "AP5678")

# Calling static methods of Truck
print(Truck.calculate_fuel_cost(1000))
print(Truck.calculate_depreciation(800000))

print("**************motorcycle*********************")

# Creating an object for the subclass Motorcycle
motorcycle = Motorcycle(150, 10, 1, "AP9101")

# Calling static methods of Motorcycle
print(Motorcycle.check_engine_status("Good"))
print(Motorcycle.calculate_acceleration(2,80))

print("*****************bicycle******************")

# Creating an object for the subclass Bicycle
bicycle = Bicycle("Aluminum", "26-inch", 1, "AP779")

# Calling static methods of Bicycle
print(Bicycle.check_tire_pressure(30))
print(Bicycle.calculate_speed(10, 2))

print("*****************************************")
           





