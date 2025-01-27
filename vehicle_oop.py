class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class gas_vehicle(Vehicle):
    def __init__(self, make, model, year, tank_size):
        super().__init__(make, model, year)
        self.tank_size = tank_size

    def display(self):
        super().display()
        print("Tank Size:", self.tank_size)


class electric_vehicle(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display(self):
        super().display()
        print("Battery Size:", self.battery_size)


class hybrid_vehicle(gas_vehicle, electric_vehicle, Vehicle):
    def __init__(self, make, model, year, tank_size, battery_size):
        super().__init__(make, model, year, tank_size)
        self.battery_size = battery_size

    def display(self):
        super().display()
        print("Battery Size:", self.battery_size)


# Test cases
vehicle1 = gas_vehicle("Toyota", "Corolla", 2020, 12)
vehicle1.display()
print()

vehicle2 = electric_vehicle("Tesla", "Model S", 2020, 100)
vehicle2.display()
print()

vehicle3 = hybrid_vehicle("Honda", "Civic", 2020, 12, 100)
vehicle3.display()
