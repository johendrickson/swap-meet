from swap_meet.item import Item

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
            new_inventory = []

            for piece in self.inventory:
                if piece != item:
                    new_inventory.append(piece)
            
            self.inventory = new_inventory

            return item
        return False
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        # if my_item not in self.inventory or their_item not in other_vendor.inventory:
        #     return False

        # self.inventory.remove(my_item)
        # other_vendor.inventory.append(my_item)

        # other_vendor.inventory.remove(their_item)
        # self.inventory.append(their_item)

        # return True
        self_found = self.get_by_id(my_item.id)
        other_found = other_vendor.get_by_id(their_item.id)

        if self_found is None or other_found is None:
            return False
        
        self.remove(my_item)
        other_vendor.remove(their_item)

        self.add(their_item)
        other_vendor.add(my_item)

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

    def get_best_by_category(self, category=""):
        category_items = self.get_by_category(category)
        
        best_item = None
        best_condition = -1
        
        for item in category_items:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
                
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        self.inventory.remove(my_best_item)
        other_vendor.inventory.remove(their_best_item)

        self.inventory.append(their_best_item)
        other_vendor.inventory.append(my_best_item)
        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True