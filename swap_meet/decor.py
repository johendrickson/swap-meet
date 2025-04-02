from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
    
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
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