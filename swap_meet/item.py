import uuid 

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    
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