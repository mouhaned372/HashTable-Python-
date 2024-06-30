class HashTable:
    def __init__(self, size=10):
        self.table_size = size  
        self.table = [[] for _ in range(self.table_size)]
        self.count = 0

    def f(self, key):
        total = 0
        for char in key:
            total = (total * 31 + ord(char)) % self.table_size
        return total

    def add(self , x):
        x.split()[-1]
        index = self.f(x.split()[-1])
        if x.split()[-1] not in self.table[index]:
          self.table[index].append(x.split()[-1])
          self.count += 1 
          print("added successfully" +" " + x.split()[-1])
        else :
            print("already exist")

    def remove(self , x):
        x.split()[-1]
        index = self.f(x.split()[-1])
        try:
            self.table[index].remove(x.split()[-1])
            self.count -= 1
            print("removed successfully" +" " + x.split()[-1])
        except ValueError:
            print(f"Key { x.split()[-1]} not found")

    def get_size(self):  
        return self.count

   
    def contains(self, x):
        key = x.split()[-1]
        index = self.f(key)
        if key in self.table[index]:
            print(f"Key '{key}' found")
            return True
        else:
            print(f"Key '{key}' not found")
            return False

    def display(self):
        
       
            print("The hash table is: ")
            for i in range(self.table_size):
                print(f"{i}: {self.table[i]}")

hash_table = HashTable()

while True:
    x = input(" ").split()
    
    if x[0]=="add":
        hash_table.add(x[-1])
    elif x[0]=="remove":
        hash_table.remove(x[-1])
    elif x[0]=="contains":
        hash_table.contains(x[-1])
    elif x[0]=="size":
        print(f"Current size: {hash_table.get_size()}")
    elif x[0]=="display":
        hash_table.display()
    elif x[0] == "exit":
        break
    else:
        print("Invalid ch")

print("Exiting program.")() 
