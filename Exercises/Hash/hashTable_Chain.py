class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # first Hash function
    def hash_function(self, key):
        return key % self.size

    #Insert a key in the HashTable 
    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    # Print the HashTable
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")


# Exemple
hash_table = HashTable(10)

hash_table.insert(15)
hash_table.insert(25)
hash_table.insert(35)

hash_table.display()
