"""
Created on 04/28/2023
author: priankac@udel.edu
This file contains unit tests for 0-1 knapsack problem
"""
import unittest

from answer import Item
from answer import Capacity

def test_item():
    """Test Item
    """

    d = Item(4, "NAME", 8, 56)
    
    assert d.n== 4
    assert d.name == "NAME"
    assert d.weight == 8
    assert d.value == 56


def test_Capacity():
    """Test knapsack algorithm
    """
    n= 4
    k = Capacity(14)
    items = [
        Item("Table", 4, 23),
        Item("laptop", 3, 36),
        Item("Pencil", 8, 55),
        Item("Airpods", 7, 62)
    ]
    

    function = k.knapsack(3, 32, 1)
    
    assert k.items == items
    assert [i.name for i in function] == [
        "laptop", "Pencil", "Airpods"
    ]

    function = k.knapsack(2, 33, 2)
    assert k.items == items
    assert [i.name for i in function] == [
        "laptop", "Pencil"
    ]

    

if __name__ == "__main__":
    unittest.main()
