# OOP Assignment
# OOP Assignment - Smartphone and Devices

## Assignment Task
Design Your Own Class! 🏗️

- Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
- Add attributes and methods to bring the class to life!
- Use constructors to initialize each object with unique values.
- Add an inheritance layer to explore polymorphism or encapsulation.  

---

## My Solution

### Base Class: `Device`
- Represents a generic device with attributes like `brand` and `battery`.
- Methods:
  - `charge(amount)` → charges the device.
  - `device_info()` → shows the brand and battery status.

### Subclass 1: `Smartphone`
- Inherits from `Device`.
- Adds attributes like `model`.
- Methods:
  - `phone_info()` → displays brand, model, and battery.
  - `take_photo()` → simulates taking a photo (reduces battery).

### Subclass 2: `Smartwatch`
- Inherits from `Device`.
- Methods:
  - `track_steps(steps)` → simulates step tracking (reduces battery).

---

## Example Usage
```python
phone = Smartphone("Samsung", "Galaxy S21", 80)
watch = Smartwatch("Apple Watch", 50)

phone.phone_info()
phone.take_photo()
phone.charge(10)

watch.device_info()
watch.track_steps(1200)
watch.charge(30)

