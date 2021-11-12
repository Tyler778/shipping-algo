
class HashTable:
    def __init__(self, initial_capacity=25):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def hash_function(self, key):
        k = hash(key) % len(self.table)
        return k

    def insert(self, key, item):
        bucket_list = self.table[self.hash_function(key)]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True


        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        bucket_list = self.table[self.hash_function(key)]

        for kv in bucket_list:

            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        bucket_list = self.table[self.hash_function(key)]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    def print(self):
        for item in self.table:
            if item is not None:
                print(str(item) + '\n')

