from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, id, model, fuel_capacity, current_fuel):
        self.id = id
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.current_fuel = current_fuel
    
    def get_id(self):
        return self.id
    
    def get_model(self):
        return self.model
    
    def get_fuel_capacity(self):
        return self.fuel_capacity
    
    def get_current_fuel(self):
        return self.current_fuel
    
    def set_current_fuel(self, current_fuel):
        self.current_fuel = current_fuel
    
    @abstractmethod
    def display_info(self):
        pass
    
    def refuel(self, amount):
        if amount <= 0:
            raise ValueError("Fuel amount must be greater than zero.")
        if self.current_fuel + amount > self.fuel_capacity:
            raise ValueError("Cannot refuel. Fuel capacity exceeded.")
        self.current_fuel += amount
    
    def consume_fuel(self, amount):
        if amount <= 0:
            raise ValueError("Fuel usage must be greater than zero.")
        if amount > self.current_fuel:
            raise ValueError("Not enough fuel.")
        self.current_fuel -= amount


class Car(Vehicle):
    def __init__(self, id, model, fuel_capacity, current_fuel, seats):
        super().__init__(id, model, fuel_capacity, current_fuel)
        self.seats = seats
    
    def display_info(self):
        print("Car")
        print(f"ID: {self.get_id()}")
        print(f"Model: {self.get_model()}")
        print(f"Seats: {self.seats}")
        print(f"Fuel Capacity: {self.get_fuel_capacity()} L")
        print(f"Current Fuel: {self.get_current_fuel()} L")
        print("-----------------------------")


class Bike(Vehicle):
    def __init__(self, id, model, fuel_capacity, current_fuel, type):
        super().__init__(id, model, fuel_capacity, current_fuel)
        self.type = type
    
    def display_info(self):
        print("Bike")
        print(f"ID: {self.get_id()}")
        print(f"Model: {self.get_model()}")
        print(f"Type: {self.type}")
        print(f"Fuel Capacity: {self.get_fuel_capacity()} L")
        print(f"Current Fuel: {self.get_current_fuel()} L")
        print("-----------------------------")


class Truck(Vehicle):
    def __init__(self, id, model, fuel_capacity, current_fuel, load_capacity):
        super().__init__(id, model, fuel_capacity, current_fuel)
        self.load_capacity = load_capacity
    
    def display_info(self):
        print("Truck")
        print(f"ID: {self.get_id()}")
        print(f"Model: {self.get_model()}")
        print(f"Load Capacity: {self.load_capacity} tons")
        print(f"Fuel Capacity: {self.get_fuel_capacity()} L")
        print(f"Current Fuel: {self.get_current_fuel()} L")
        print("-----------------------------")


class FuelManagementSystem:
    def __init__(self):
        self.vehicles = []
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def find_vehicle(self, id):
        for vehicle in self.vehicles:
            if vehicle.get_id() == id:
                return vehicle
        raise ValueError(f"Vehicle with ID {id} not found.")
    
    def show_all(self):
        for vehicle in self.vehicles:
            vehicle.display_info()


def main():
    system = FuelManagementSystem()
    
    # Adding sample vehicles
    system.add_vehicle(Car("C1", "Toyota", 50, 20, 5))
    system.add_vehicle(Bike("B1", "Yamaha", 15, 8, "Sport"))
    system.add_vehicle(Truck("T1", "Volvo", 150, 90, 12))
    
    while True:
        print("\n===== Vehicle Fuel Management System =====")
        print("1. Show All Vehicles")
        print("2. Refuel a Vehicle")
        print("3. Use Fuel")
        print("4. Exit")
        
        try:
            choice = input("Enter your choice: ")
            
            if choice == "1":
                print("\n--- Vehicle List ---")
                system.show_all()
            
            elif choice == "2":
                id = input("\nEnter Vehicle ID (C1/B1/T1): ")
                try:
                    vehicle = system.find_vehicle(id)
                    amt = float(input("Enter fuel amount to add (in liters): "))
                    vehicle.refuel(amt)
                    print("Refuel successful.")
                    print(f"Updated Fuel: {vehicle.get_current_fuel()} L")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "3":
                id = input("\nEnter Vehicle ID (C1/B1/T1): ")
                try:
                    vehicle = system.find_vehicle(id)
                    amt = float(input("Enter fuel amount to use (in liters): "))
                    vehicle.consume_fuel(amt)
                    print("Fuel usage successful.")
                    print(f"Updated Fuel: {vehicle.get_current_fuel()} L")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif choice == "4":
                print("Exiting system...")
                break
            
            else:
                print("Invalid choice. Try again.")
        
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
