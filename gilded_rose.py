# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Special processing logic for Sulfuras: never has to be sold or decreases in Quality
            if item.name == "Sulfuras":
                item.sell_in -= 1
                continue
            
            # Handle different item types
            if item.name == "Aged Brie":
                self.increase_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_pass(item)
            elif "Conjured" in item.name:
                self.decrease_quality(item, 2)  # Conjured items degrade twice as fast
            else:
                self.decrease_quality(item)

            # Reduce sell_in and handle expired items
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    self.increase_quality(item)
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0  # Quality drops to 0 after concert
                else:
                    self.decrease_quality(item)

    # Increase quality, max 50
    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)
        
    # Decrease quality, never below 0
    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    # Special processing logic for Backstage: quality increases more as sell_in decreases
    def update_backstage_pass(self, item):
        if item.sell_in > 10:
            self.increase_quality(item)
        elif item.sell_in > 5:
            self.increase_quality(item, 2)
        elif item.sell_in > 0:
            self.increase_quality(item, 3)
            
    # Return all item names                   
    def get_items(self):
        return [item.name for item in self.items]
    
    # Remove an item    
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]
