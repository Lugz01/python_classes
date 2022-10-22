
class Car:
    def __init__(self, name, price, model):
        self.name = name
        self.price = price
        self.model = model

    def drive(self):
        return f"I am driving my {self.name}"

    def air_conditioner(self):
        return f"air conditioner turned on for {self.name}"

glk_mercedes = Car("Glk Mercedes benz", "$2000", "GLk")
# glk_mercedes.drive()
eClass = Car("Merceded E class", "$3000", "E class")
print(glk_mercedes.drive())
print((eClass.drive()))
print(glk_mercedes.air_conditioner())