import uuid

import uuid 

class Item:
    def __init__(self, id=None):
        self.id = id if id is not None else uuid.uuid4().int

    def get_category(self):
        return self.__class__.__name__
# -----------------
# NATASHA CODE

    def __init__(self, id=None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
    