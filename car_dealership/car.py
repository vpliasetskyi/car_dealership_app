#Create class car with arguments 
class Car: 
        def __init__(self,id,make,model,year,price,mileage):
                self.id = id
                self.make = make
                self.model = model
                self.year = year
                self.price = price 
                self.mileage = mileage
                # Validation for nagative or zero price and year 
                if self.year <= 0  or self.price <= 0:
                        raise ValueError("Invalid year or price value") 
        #Create string method
        def __str__(self):
                return (f" [ID: {self.id}] {self.year} {self.make} {self.model} | ${self.price:,.2f} | {self.mileage:,.2f}km")
        #Create helper method for db that convert input to tuple 
        def to_tuple(self):
                return(self.make, self.model, self.year , self.price, self.mileage)
        
# test
#car1 = Car(1, "Toyota", "Camry", 2022, 25000, 15000)
#print(car1)

#tuple test
#print(car1.to_tuple())

# error test 
#car2 = Car(2, "Honda", "Civic", -1, 22000, 8000)


