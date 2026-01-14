# Dictionary (HashMap) Implementation in Python

# Creating a dictionary
class HashMap:  
    def __init__(self):
        self.size = 10
        self.map = [[] for _ in range(self.size)] # creates [[], [], ..., []]

    # Hash function
    def _get_hash(self, key):
        return hash(key) % self.size 
        # hash(key) converts any key to a huge integer
        # hash("Diluksha") -> 12345678901234567890
        # We only have 10 buckets so we use modulo operator to fit it in our range
        # 12345678901234567890 % 10 -> 0

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        # Go to the specific bucket (Room)
        bucket = self.map[key_hash]
        
        # Check if key already exists (Update it)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return True
        
        # If not found, add to the chain (The "Bunk Bed")
        bucket.append(key_value)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)
        bucket = self.map[key_hash]
        
        # Search inside the bucket (Linear search only on the small chain)
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
    def print_map(self):
        for i, bucket in enumerate(self.map):
            print(f"Bucket {i}: {bucket}")

my_map = HashMap()

my_map.add("Diluksha", "Engineer")
my_map.add("Amal", "Doctor")
my_map.add("Nimal", "Teacher")
my_map.add("Kamal", "Lawyer")
my_map.add("Ravindu", "Surgeon")  # Update Amal's profession
my_map.add("Saman", "Pilot")
my_map.add("Kamal", "Judge")   # Update Kamal's profession
my_map.add("Nimala", "Architect")  # Update Nimala's profession
my_map.add("Ravi", "Artist")
my_map.add("Sunil", "Chef")
my_map.add("Thissa", "Dentist")

my_map.print_map()
 