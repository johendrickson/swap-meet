from .item import Item

class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.inventory.remove(my_first_item)
        other_vendor.inventory.append(my_first_item)

        other_vendor.inventory.remove(their_first_item)
        self.inventory.append(their_first_item)
        return True
    

    def get_by_category(self, category=""):
        return [item for item in self.inventory if item.get_category() == category] 

    def get_best_by_category(self, category):
        pass
    
    def swap_best_by_category(self):
        pass