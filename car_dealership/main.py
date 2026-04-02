from car import Car
from database import (initialize_database, import_cars, add_car, get_all_cars,
                      get_car_by_id, update_car, delete_car, search_cars)

#Create menu function 
def show_menu():
    print("\n" + "="*40)
    print("   🚗  CAR DEALERSHIP MANAGER")
    print("="*40)
    
    #  print menu and return the user's input
    
    print(f"1. Add Car")
    print(f"2. View All Cars")
    print(f"3. Update Car")
    print(f"4. Delete Car")
    print(f"5. Search Cars")
    print(f"6. Exit")
    
    choose_option = input("Choose options (1-6)): ")
    return choose_option


#Create add car function 

def add_car_flow():
    print(f"-----ADD CAR-----")
    try:
            model = input(f"Model: ")
            make = input(f"Make: ")
            year = int(input(f"Year: "))
            price = float(input("Enter price: "))
            mileage = float(input("Eneter Mileage: "))

            new_car = Car( id=None, make = make, model = model, year = year, price = price, mileage = mileage)

            add_car(new_car)

            print(f"\nCar was added with ID: {new_car.id}")
    except ValueError:
            print("\nError: Year, Price, and Mileage must be numbers!")

#Create view cars function   
           
def view_all_flow():
      print("\n -----All Cars-----")
      cars = get_all_cars()

      if not cars:
            print("Database is empty!Please add at least one car")
            return
      
      for car in cars:
            print (car)
            print ("-" * 40)
      print(f"Total: {len(cars)} cars")

# Create  update car  function 

def update_car_flow():
    print("\n -----Update Car-----")
    try:
            car_id = int(input("Enter car Id to update:"))
            car = get_car_by_id(car_id)
            if car is None: 
                  print(f"\n No car found with entered id {car_id}")
                  return
        
            print(f"\nCurrent details: {car}")  
            

            new_make = input(f"Make [{car.make}]: ")
            if new_make == "":
                car.make = car.make
            else:
                car.make = new_make

            new_model = input(f"Model [{car.model}]: ")
            if new_model == "":
                car.model = car.model
            else:
                car.model = new_model

            new_year = input(f"Year [{car.year}]: ")
            if new_year == "":
                car.year = car.year
            else:
                car.year = int(new_year)

            new_price = input(f"Price [{car.price}]: ")
            if new_price == "":
                car.price = car.price
            else:
                car.price = float(new_price)

            new_mileage = input(f"Mileage [{car.mileage}]: ")
            if new_mileage == "":
                car.mileage = car.mileage
            else:
                car.mileage = int(new_mileage)

            update_car(car)
            print("Car updated!")
            print(car)

    except ValueError:
        print("\nError: Incorrect input. Year, Price, and Mileage must be numbers!")

# Create delete function 

def delete_car_flow():
    print("\n-----Delete Car-----")
    car_id = int(input("Enter car ID to delete: "))
    car    = get_car_by_id(car_id)

    if car is None:
        print("No car found with that ID.")
        return

    print("Car to delete:")
    print(car)

    confirm = input("Type YES to confirm: ")

    if confirm == "YES":
        delete_car(car_id)
        print("Car deleted!")
    else:
        print("Delete cancelled.")       

#Search function 

def search_cars_flow():
    print ("\n-----Search Car-----")
    keyword = input("Search by make model or year:  ")
    results = search_cars(keyword)

    if len(results) == 0:
         print("No cars found")
         return
    
    print(f"Found {len(results)} car(s):")
    
    for car in results:
        print(car)
        print("-" * 40)

#Main loop function 

def main():
     initialize_database()
     import_cars()
     option_selection()

def option_selection():
    while True:
        choice = show_menu()

        match choice:
                case "1":
                    add_car_flow()
                case "2":
                    view_all_flow()
                case "3":
                    update_car_flow()
                case "4":
                    delete_car_flow()
                case "5":
                    search_cars_flow()
                case "6":
                    print("Exiting... Goodbye!")
                    break 
                case _:
                    print("\n[!] Invalid choice. Please pick 1-6.")

if __name__ == "__main__":
    main()


