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
            updater = self.get_updater(item)
            updater.update(item)

    # Determine goods types
    def get_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Sulfuras":
            return SulfurasUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif "Conjured" in item.name:
            return ConjuredUpdater()
        else:
            return StandardUpdater()
        
    # Return all item names
    def get_items(self):
        return [item.name for item in self.items]

    # Remove an item
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]


class UpdaterOperation:
    def update(self, item):
        pass
    
    # Decrease quality, never below 0
    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)
        
    # Increase quality, max 50
    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)
        
    # Decrease the number of days we have to sell the item
    def decrease_sell_in(self, item):
        item.sell_in -= 1


class StandardUpdater(UpdaterOperation):
    def update(self, item):
        self.decrease_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item)


# Aged Brie: actually increases in Quality the older it gets
class AgedBrieUpdater(UpdaterOperation):
    def update(self, item):
        self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item)


# Sulfuras: never has to be sold or decreases in Quality
class SulfurasUpdater(UpdaterOperation):
    def update(self, item):
        item.sell_in -= 1  # Sulfuras still reduces sell_in


# Backstage passes: increases in Quality as its SellIn value approaches
class BackstagePassUpdater(UpdaterOperation):
    def update(self, item):
        if item.sell_in > 10:
            self.increase_quality(item)
        elif item.sell_in > 5:
            self.increase_quality(item, 2)
        elif item.sell_in > 0:
            self.increase_quality(item, 3)
        else:
            item.quality = 0

        self.decrease_sell_in(item)


# Conjured: degrade twice as fast
class ConjuredUpdater(UpdaterOperation):
    def update(self, item):
        self.decrease_quality(item, 2)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)