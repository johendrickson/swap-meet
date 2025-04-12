from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."
    
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