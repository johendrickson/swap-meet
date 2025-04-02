from swap_meet.item import Item

class Electornics(Item):
    def __init__(self, id=None, type="Unknown"):
        super().__init__(id)
        self.type = type
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. This is a {self.type} device."