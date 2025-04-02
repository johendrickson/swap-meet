from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."