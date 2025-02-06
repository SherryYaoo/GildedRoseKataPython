# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)
    
    # Logic error 1: "Conjured" items degrade in Quality twice as fast as normal items
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item(name="Conjured", sell_in=3, quality=6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4, "Conjured items degrade in Quality twice as fast as normal items")
    
    # Logic error 2: Quality should not be negative
    def test_quality_should_not_be_negative(self):
        items = [Item("Mongoose", 1, 0.1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0, "Quality should never be negative")
    
    # Logic error 3: The Quality of an item is never more than 50
    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 5, 49.5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50, "The Quality of an item is never more than 50")
       
     # Syntax error1: Missing parameters 
    def test_gilded_rose_missing_parameter(self):
        items = [Item("Sulfuras", 5)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
    
    # Syntax error2: Calling update_quality() with an extra argument
    def test_update_quality_with_extra_argument(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality("extra_argument")  # This method does not accept parameters
        
    # Syntax error3: Calls a method that does not exist (remove_item)
    def test_gilded_rose_calls_non_existent_method(self):
        items = [Item("ItemA", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.remove_item("ItemA")  # This method does not exist in GildedRose


if __name__ == '__main__':
    unittest.main()