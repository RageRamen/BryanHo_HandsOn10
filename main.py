class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [DoublyLinkedList() for _ in range(initial_capacity)]

    def hash_function(self, key):
        # Multiplication method
        A = 0.6180339887  # Approximate value of (√5 - 1) / 2
        return int(self.capacity * ((key * A) % 1))

    def resize(self, new_capacity):
        new_buckets = [DoublyLinkedList() for _ in range(new_capacity)]
        for bucket in self.buckets:
            for node in bucket:
                hash_value = self.hash_function(node.key)
                new_buckets[hash_value].append(node.key, node.value)
        self.buckets = new_buckets
        self.capacity = new_capacity

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        bucket = self.buckets[hash_value]
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        bucket.append(key, value)
        self.size += 1
        if self.size >= self.capacity * 0.75:
            self.resize(self.capacity * 2)

    def remove(self, key):
        hash_value = self.hash_function(key)
        bucket = self.buckets[hash_value]
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1
                if self.capacity > 8 and self.size <= self.capacity * 0.25:
                    self.resize(self.capacity // 2)
                return

    def search(self, key):
        hash_value = self.hash_function(key)
        bucket = self.buckets[hash_value]
        for node in bucket:
            if node.key == key:
                return node.value
        return None


# Example:
hash_table = HashTable()
hash_table.insert(5, 10)
hash_table.insert(15, 20)
hash_table.insert(25, 30)
print(hash_table.search(5))  # Output: 10
print(hash_table.search(15))  # Output: 20
hash_table.remove(5)
print(hash_table.search(5))  # Output: None
