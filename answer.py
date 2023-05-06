"""
    Author priankac@udel.edu
    04/28/2023
    This takes in an input file with capacity, 
    item names, weights and values, finds the subset of items that 
    maximize their values and the weights should be <= capacity, 
    the items and their values are printed out.
"""
import math

class Item(object):
    def __init__(self, n_items, name, weight, value):
        """
        n- number of items
        name- the name of the item
        weight- the appointed weight of the item
        value- the sum of values of item/items
        
        """
        self._n_items= n_items
        self._name = name
        self._weight = weight
        self._value = value
        
    @property
    def n_items(self):
    #returns number of items
        return self._n_items

     

    @property
    def name(self):
        
    #returns the name of the item
        

        return self._name
    
    @property
    def value(self):
        
    #returns the sum of values of items
        

        return sum(self._values)

    @property
    def weight(self):
        
    #returns the weight of the item/items
        

        return self._weight

    


class Capacity(object):
    def __init__(self, capacity):
        
    #shows the maximum limit of weight
        

        self._capacity = capacity

    @property
    def items(self):
        
    #returns the items
        

        return self._items

    @items.setter
    def items(self, items):
        
    #items
        

        self._items = items

    def knapsack(self, weight, value, n):
        """
        does the maximizing function of knapsack
        """

        s = [[0 for W in range(self._capacity + 1)] for n in range(len(self._items))]
        for index, item in enumerate(self._items):
            for W in range(1, self._capacity + 1):
                if W < item.weight:
                    s[index][W] = s[index - 1][W]
                else:
                    s[index][W] = max(item.value + s[index - 1][W - item.weight], s[index - 1][W])
                    
        maximum = []
        n = len(self._items) - 1
        W = self._capacity
        while n > 0 and W > 0:
            if s[n][W] != s[n - 1][j]:
                maximum.append(self._items[n])
                j= j- self._items[n].weight
            n= n-1
            
        return maximum
