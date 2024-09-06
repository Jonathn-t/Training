class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # first Hash function
    def hash_function(self, key):
        return key % self.size

    #Insert a key in the HashTable 
    def insert(self, key):
        original_index = self.hash_function(key)
        i : int = 0

        # Keep searching for an empty space with the Quadratic Probing
        while True :
            new_index = (original_index + i**2) % self.size  # Wrapping
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