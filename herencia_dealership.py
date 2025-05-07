
class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand     # Atributo
        self.model = model     # Atributo
        self.price = price     # Atributo
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido.")
        else:
            print(f"El vehículo {self.brand} no está disponible.")

    #abstraccion
    def check_available(self):
        return self.is_available

    #abstraccion
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia 
class Car(Vehicle):

    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha."
        else:
            return f"El coche {self.brand} no está disponible."

    #Polimorfismo
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido."
        else:
            return f"El coche {self.brand} no está disponible."
        
#Herencia
class Bike(Vehicle):

    #Polimorfismo
    def start_engine(self):
        print(f"La bicicleta {self.brand} está en marcha")

    #Polimorfismo
    def stop_engine(self):
        print(f"La bicicleta {self.brand} se ha detenido")

class Truck(Vehicle):
    def start_engine(self):
        print(f"El motor del camión {self.brand} está en marcha")

    def stop_engine(self):
        print(f"El motor del camión {self.brand} se ha detenido")

class Customer:
    def __init__(self, name):
        self.name = name       # Atributo
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, el {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        print(f"El {vehicle.brand} esta {availablity} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"{vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} ha sido registrado como cliente")
    
    def show_available_vehicles(self):
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"Marca: {vehicle.brand}, Precio: {vehicle.get_price()}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Chalo")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#mostrar los vehiculos disponibles
dealership.show_available_vehicles()

#cliente consultara un vehiculo
customer1.inquire_vehicle(car1)

#cliente comprara vehiculo
customer1.buy_vehicle(car1)

#mostrar vehiculos disponibles
dealership.show_available_vehicles()