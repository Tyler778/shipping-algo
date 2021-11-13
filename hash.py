
# Hash table with an initial capacity of 45.  45 was the number I felt I was getting few multiple items in one bucket, sacrificing some space complexity for a decrease in time complexity.
#
# Space complexity for the hashTable is O(n)
class HashTable:
    # Constructor
    def __init__(self, initial_capacity=45):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Hash function to distribute keys/hashed keys across the available indices.
    # Time complexity of O(1)
    def hash_function(self, key):
        k = hash(key) % len(self.table)
        return k

    # Method to hash key as well as place passed item in as a value at that hashed key index.
    # Assuming a solid hashTable implementation, time complexity should be O(1)
    def insert(self, key, item):
        b_l = self.table[self.hash_function(key)]

        for i in b_l:
            if i[0] == key:
                i[1] = item
                return True
        kv = [key, item]
        b_l.append(kv)
        return True
    # Method for getting value given a key.  We hash the key then point to that index within the hashtable
    #
    # Given a solid hashtable with distributed items, access/search will be O(1).  If improper distribution, O(n)
    def search(self, key):
        b_l = self.table[self.hash_function(key)]
        for i in b_l:
            if i[0] == key:
                return i[1]
        return None

    # Method for removing specific key from the hashtable by hashing it then finding the item/value at that index.
    #
    # Assuming a solid implementation, time complexity should be O(1), if improper implementation with poorly distributed values, you can expect O(n) time complexity.
    def remove(self, key):
        b_l = self.table[self.hash_function(key)]
        for i in b_l:
            if i[0] == key:
                b_l.remove([i[0], i[1]])
