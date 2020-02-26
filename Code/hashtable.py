from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __len__(self):
        return self.length()

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(1) because we already keep size / len of buckets"""
        return len(self) / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: O(n) because we need to loop through all items in each bucket"""
        keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                keys.append(key)
        return keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: O(n) because we need to loop through all items in each bucket"""
        values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        return values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: O(n) because we need to loop over all the items in the bucket"""
        items = []
        for bucket in self.buckets:
            items.extend(bucket.items())
        return items

    def length(self):
        """Return the number of key-value entries by returning our running size.
        Best and worst case running time: O(1) because we are just returning a value that we are keeping"""
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: O(1) - We have a low load factor
        Worst case running time: O(l) - such that l is n/b where n is number of keys and b is number of buckets"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) - We have a low load factor
        Worst case running time: O(l) - such that l is n/b where n is number of keys and b is number of buckets"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: O(1) - We have a low load factor
        Worst case running time: O(l) - l=load factor - Ideally, we should maintain a low load factor so that set will never be more than O(1)"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        # increase size
        self.size += 1
        # checks if the load factor exceeds 75%
        if self.load_factor() > 0.75:
            # resize the underlying bucket size to be 2x of what it was before
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) - We have a low load factor
        Worst case running time: O(l) - l=load factor - Ideally, we should maintain a low load factor so that delete will never be more than O(1)"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            # reduce the size
            self.size -= 1
            # if the load factor is small we are able to downsize to save memory
            if self.load_factor() < 0.15:
                self._resize(0)
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(n + n) because we need to loop over all items to create a copy and then add them all back to a new LL
        Best and worst case space usage: O(n + n) with n being the amont of buckets, because we have to create a copy to create a newly sized LL"""
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size
        elif new_size is 0:
            new_size = len(self.buckets) // 2  # Half size

        current_items = self.items()

        self.buckets = [LinkedList() for i in range(new_size)]
        self.size = 0

        for key, value in current_items:
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
