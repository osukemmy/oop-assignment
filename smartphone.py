# Base class
class Device:
    def __init__(self, brand, battery=100):
        self.brand = brand
        self.battery = battery

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} charged to {self.battery}%")

    def device_info(self):
        print(f"Device: {self.brand}, Battery: {self.battery}%")

# Subclass 1: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, battery=100):
        super().__init__(brand, battery)
        self.model = model

    def phone_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Battery: {self.battery}%")

    def take_photo(self):
        if self.battery > 5:
            self.battery -= 5
            print(f"{self.model} took a photo! Battery is now {self.battery}%")
        else:
            print("Battery too low to take photo!")

# Subclass 2: Smartwatch
class Smartwatch(Device):
    def __init__(self, brand, battery=100):
        super().__init__(brand, battery)

    def track_steps(self, steps):
        if self.battery > 2:
            self.battery -= 2
            print(f"{self.brand} tracked {steps} steps! Battery: {self.battery}%")
        else:
            print("Battery too low to track steps!")

# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S21", 80)
    watch = Smartwatch("Apple Watch", 50)

    phone.phone_info()
    phone.take_photo()
    phone.charge(10)

    print("---")

    watch.device_info()
    watch.track_steps(1200)
    watch.charge(30)
