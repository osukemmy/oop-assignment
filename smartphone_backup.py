# smartphone.py
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}% battery."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        return f"Battery charged to {self.battery}%."

    def use(self, hours):
        self.battery = max(0, self.battery - (hours * 10))
        return f"After {hours} hour(s) of use, battery is at {self.battery}%."


class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_megapixels):
        super().__init__(brand, model, storage, battery)
        self.camera_megapixels = camera_megapixels

    # polymorphism: override phone_info
    def phone_info(self):
        return f"{self.brand} {self.model} Pro with {self.storage}GB storage, {self.camera_megapixels}MP camera, and {self.battery}% battery."

    def take_photo(self):
        if self.battery > 5:
            self.battery -= 5
            return f"Photo taken with {self.camera_megapixels}MP camera. Battery now at {self.battery}%."
        else:
            return "Not enough battery to take a photo."


if __name__ == "__main__":
    # Example usage
    phone1 = Smartphone("Samsung", "Galaxy S21", 128, 80)
    print(phone1.phone_info())
    print(phone1.use(3))
    print(phone1.charge(15))

    pro_phone = SmartphonePro("Apple", "iPhone 14", 256, 90, 48)
    print(pro_phone.phone_info())
    print(pro_phone.take_photo())
