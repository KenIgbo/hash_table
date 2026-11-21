class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, input_word):
        hash_value = 0
        for i in range(len(input_word)):
            hash_value += ord(input_word[i])
        return hash_value

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            self.collection[hash_value][key] = value   # dict[main_key][inner key] = inner_value
        else:
            self.collection[hash_value] = {key:value}

    def remove(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            inner_dict = self.collection[hash_value]
            if key in inner_dict:
                del(in_dict[key])

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            inner_dict = self.collection[hash_value]
            if key in inner_dict:
                return inner_dict[key]
            return None
        return None

# ------ end of program ------ #


table = HashTable()
table.add('golf', 'sport')
table.add('orange', 'fruit')
table.add('flog', 'discipline')
table.add('fcc', 'learning')
table.remove('cfc')

print(table.collection)
print(table.lookup('male'))