import uuid 

# class Item:
#     def __init__(self, id=None):
#         self.id = id if id is not None else uuid.uuid4().int

#     def get_category(self):
#         return self.__class__.__name__
# # -----------------
# # NATASHA CODE

class Item:
    def __init__(self, id=None):
        self.id = id if id is not None else uuid.uuid4().int

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}."
    