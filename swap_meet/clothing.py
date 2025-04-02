from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    
    def condition_description(self):
        descriptions = {
        0 : "oof",
        1 : "been around the block!",
        2 : "decent",
        3 : "moderate wear",
        4 : "gently used",
        5 : "like new"
        }
        if self.condition < 0 or self.condition > 5:
            return "unknown condition"
        return descriptions[self.condition]