class HamsterTracker:
    def __init__(self, name, initial_weight):
        self.name = name
        self.__weight_grams = initial_weight
        
    def get_weight(self):
        return self.__weight_grams
    
    def update_weight(self, new_weight):
        