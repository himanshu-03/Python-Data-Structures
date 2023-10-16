# Program Name: hash_table_with_chaining.py
# Implementing a hash table with chaining

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Usage
ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("name"))
print(ht.get("age"))
