class Hashtable:

    def __init__(self, initial_capacity=10):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

        # defining insert for hashtable
        # time complexity of o(1)

    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

        # Search hash table
        # time complexity of O(1)

    def search(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

        # remove method
        # time complexity of O(1)

    def hash_remove(self, key):
        opening = hash(key) % len(self.list)
        location = self.list[opening]

        if key in location:
            location.remove(key)
