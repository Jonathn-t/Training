class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # first Hash function
    def hash1(self, key):
        return key % self.size
    
    # Second Hash function
    def hash2(self, key):
        return 3 - (key % 3) # I selected the prime number 3 for the constant
    
    #Insert a key in the HashTable 
    def insert(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        i : int = 0
        
        # Keep searching for an empty space with the double hash
        while True:
            new_index = (index + i * step) % self.size
            if self.table[new_index] == []:
                self.table[new_index].append(key)
                break
            else:
                i += 1

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
