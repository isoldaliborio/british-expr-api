class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def __repr__(self):
        return f"My name is {self.name} and I am a {self.breed}"



d1 = Dog("Chica", "Australian Shepherd")

print(d1.__dict__)