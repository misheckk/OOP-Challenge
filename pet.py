class Pet:  # Fixed: PascalCase for class name
    def __init__(self, name, hunger=5, energy=5, happiness=5):  # Default values
        self.name = name
        self.hunger = hunger  
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} has taken a nap.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else: 
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"- Hunger: {self.hunger}/10")
        print(f"- Energy: {self.energy}/10") 
        print(f"- Happiness: {self.happiness}/10")

    def train(self, trick):  
        if self.energy >= 1:  
            self.tricks.append(trick)
            self.energy -= 1  # Training costs energy
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train.")

    def show_tricks(self):  
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} has not learned any tricks yet.")