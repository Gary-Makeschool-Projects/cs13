from hashtable import HashTable


class HashSet(object):
    def __init__(self, elements=None):
        self.ht = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)

    def __len__(self):
        return self.size

    @property
    def size(self):
        return self.ht.size

    def get(self, element):
        """Get item from the Set"""
        return self.ht.get(element)

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        return self.ht.contains(element)

    def add(self, element):
        """add element to this set, if not present already"""
        if not self.contains(element):
            self.ht.set(element, element)

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.ht.delete(element)

    def items(self):
        return self.ht.keys()

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        return HashSet(self.items() + other_set.items())

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        return HashSet([element for element in self.items() if other_set.contains(element)])

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        return HashSet([element for element in self.items() if not other_set.contains(element)])

    def is_subset(self, other_set):
        """return a boolean indicating whether other_set is a subset of this set""" 
        for item in other_set.items():
            if not self.contains(item):
                # An item in our set is not in the given set
                return False
        return True