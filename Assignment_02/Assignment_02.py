import unittest

'''
Description:
Author: Moncerrat Romero
Version:Python 3.6.5

'''

'''
    Implement a dictionary using chaining.
    You may assume every key has a hash() method, e.g.:
    >>> hash(1)
    1
    >>> hash('hello world')
    -2324238377118044897
'''

class dictionary:
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        
        count = 0
        for x in self.flattened():
            count += 1
            
        return count
                         
    def flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self): 
        return(iter(self.flattened())) 
    
    def __str__(self): 
        return(str(self.flattened()))

    def __setitem__(self, key, value):
        page_number = hash(key) % self.__limit
        if self.__items[page_number] == []:
            self.__items[page_number].append([key, value])
        else:
            if self.__items[page_number] == None:
                self.__items[page_number] = key      
            if self.__items[page_number][0] != key:
                for slot in self.__items[page_number]:
                    if slot[0] == key:
                        slot[1] = value
                        return
                self.__items[page_number].append([key, value]) 


    def __getitem__(self, key):
        
        page_number = hash(key) % self.__limit
        for slot in self.__items[page_number]:
            if slot[0] == key:
                return slot[1]   
        raise RuntimeError('No List')
                   
    def __contains__(self, key):
         
        page_number = hash(key) % self.__limit
        for slot in self.__items[page_number]:
            if slot[0] == key:
                return True
        
        return False   
        
    #C-level work        

class test_add_two(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[2] = "two"
        self.assertEqual(len(s), 2)
        self.assertEqual(s[1], "one")
        self.assertEqual(s[2], "two")
      # print(s)


class test_add_twice(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = "one"
        s[1] = "one"
        print(s)
        self.assertEqual(len(s), 1)
        self.assertEqual(s[1], "one")

class test_store_false(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = False
        self.assertTrue(1 in s)
        self.assertFalse(s[1])
        #print(s)
        
class test_store_none(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[1] = None
        self.assertTrue(1 in s)
        self.assertEqual(s[1], None)
        #print(s)
       
class test_none_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[None] = 1
        self.assertTrue(None in s)
        self.assertEqual(s[None], 1)
        
class test_False_key(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[False] = 1
        self.assertTrue(False in s)
        self.assertEqual(s[False], 1)
        
class test_collide(unittest.TestCase):
    def test(self):
        s = dictionary()
        s[0] = "zero"
        s[10] = "ten"
        print(s)
        self.assertEqual(len(s), 2)
        self.assertTrue(0 in s)
        self.assertTrue(10 in s)

if __name__ == '__main__':
    unittest.main()
