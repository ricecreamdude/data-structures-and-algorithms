# """
# add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

# get: takes in the key and returns the value from the table.

# contains: takes in the key and returns a boolean, indicating if the key exists in the table already.

# hash: takes in an arbitrary key and returns an index in the collection.

# """

from linkedList import LinkedList

class HashTable:
    
    def __init__(self):
        self.buckets = [LinkedList() for i in range(1024)]
        

    def hash(self, key):

        char_sum = sum([ord(char) for char in key])

        prime_number = 599
        
        index = char_sum * prime_number % len(self.buckets)

        return index

    def add(self, key, value):

        index = self.hash(key)

        #Handles collisions utilizing linkedlist.insert method
        self.buckets[index].insert({'key':key, 'value':value})


    def get(self, key):

        index = self.hash(key)
        bucket = self.buckets[index]

        #Find out if linked list has head value
        response = None

        #If the key has a value, return the value
        if bucket.head.value['key']:
            response = bucket.head.value['value']

            currentNode = bucket.head 

            print ('Current Node',currentNode.value)

            while currentNode.value['key'] is not key:
                currentNode = currentNode.next 

            response = currentNode.value['value']

        return response # or raise Exception if you like

    def contains(self, key):
        print('***********CONTAINS FIRED*****************')
        if self.get(key) == None:
            return False

        return True


































































# from linkedList import LinkedList

# class HashTable:
#     def __init__(self):
#         self.buckets = [LinkedList] * 1024  

#     #One example of a hashing algorithm
#     def hash(self, key):

#         #Generate a number based on the sum of the unicode values of each characters in KEY 
#         char_sum = sum( [ord(char) for char in key])

#         #Multiply value by a specific number
#         prime_number = 599

#         #Modulus by 1024 to provide list index for value
#         index = prime_number * char_sum % len(self.buckets) 

#         return index


#     def addValue(self, key, value):

#         hashIndex = self.hash(key)

#         # if self.buckets[hashIndex]: 
#         #     print('COLLISION')

#         print('****************KEY', key)        
#         print('****************VALUE', value)

#         print('*************ADD BUCKET', self.buckets[hashIndex])

#         self.buckets[hashIndex].insert('test')

#         return "Added value to bucket"


#     def get(self, key):
#         hash = self.hash(key)

#         #Empty values return null as default 
#         value = None

#         if self.buckets[hash].head:
#             value = self.buckets[hash].head.value

#         return value

#     def contains(self, key):

#         if self.get(key) == None:
#             return False

#         return True

# if __name__ == "__main__":
#     h = HashTable()

#     h.buckets[0].insert('lasagna')
    
#     print(h.buckets[0].head)
#     # h.add('potato', 'fries')



#     # print('BUCKETS', h.buckets)

