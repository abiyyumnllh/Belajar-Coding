class MechanicalKeyboard:
    def __init__(self, brand, switch_type):
        self.brand = brand
        self.switch_type = switch_type
        self.is_connected = False
    
    def connect(self):
        self.is_connected = True
        print(f"the {self.brand} keyboard is successfully connected to the PC")
        
    def type_code(self, lines):
        if self.is_connected:
            print(f"Typing {lines} lines of code using {self.switch_type} switches. Clack clack clack")
        else :
            print(f"Error: Cannot type. The {self.brand} keyboard is not connected yet!")          
        
        
keyboard = MechanicalKeyboard("Ajazz", "Red")

keyboard.type_code(100)
keyboard.connect()
keyboard.type_code(100)