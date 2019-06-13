from __future__ import print_function
import unittest

class LinkedList(object):
   class Node(object):
   
      def __init__(self, value, next_node):
         self.value = value
         self.next_node = next_node
         
   def __init__(self, initial=None):
      self.front = self.back = self.current = None
      if initial is not None:
         for i in initial:
            self.push_front(str(i))
      
   def empty(self):
      return self.front == self.back == None
      
   def __iter__(self):
      self.current = self.front
      return self
      
   def __next__(self):
      if self.current:
         tmp = self.current.value
         self.current = self.current.next_node
         return tmp
      else:
         raise StopIteration()
         
   def push_front(self, value):
      new = self.Node(value, self.front)
      if self.empty():
         self.front = self.back = new
      else:
         self.front = new
         
   def pop_front(self):
      if self.empty():
         raise RuntimeError 
      tmp = self.front.value
      self.front = self.front.next_node
      if not self.front:
         self.back = None
      return tmp
      
   def push_back(self, value):
      new = self.Node(value, None)
      if self.empty():
         self.back = self.front = new
      else:
         current = self.front
         while current.next_node is not None:
            current = current.next_node
         self.back.next_node = new
         self.back = new
      
   def pop_back(self):
      if self.empty():
         raise RuntimeError
      elif self.back == self.front:
         tmp = self.back.value 
         self.back = None
         self.front = None
         return tmp
      else: 
         tmp = self.back.value
         tmp2 = self.front
         while tmp2.next_node is not self.back:
            tmp2 = tmp2.next_node
         self.back = tmp2
         tmp2.next_node = None
         return tmp
         
   def __str__(self):
      tmp = ""
      while self.front is not self.back:
         tmp += str(self.pop_back()) + ","
      return tmp + str(self.pop_front())
      
   def __repr__(self):
      return "LinkedList((" + self.__str__() + "))" 
         
      
class TestEmpty(unittest.TestCase):
   def test(self):
      self.assertTrue(LinkedList().empty())
      
class TestPushFrontPopBack(unittest.TestCase):
   def test(self):
      linked_list = LinkedList()
      linked_list.push_front(1)
      linked_list.push_front(2)
      linked_list.push_front(3)
      self.assertFalse(linked_list.empty())
      self.assertEqual(linked_list.pop_back(), 1)
      self.assertEqual(linked_list.pop_back(), 2)
      self.assertEqual(linked_list.pop_back(), 3)
      self.assertTrue(linked_list.empty())
      
class TestPushFrontPopFront(unittest.TestCase):
   def test(self):
      linked_list = LinkedList()
      linked_list.push_front(1)
      linked_list.push_front(2)
      linked_list.push_front(3)
      self.assertEqual(linked_list.pop_front(), 3)
      self.assertEqual(linked_list.pop_front(), 2)
      self.assertEqual(linked_list.pop_front(), 1)
      self.assertTrue(linked_list.empty())

class TestPushBackPopFront(unittest.TestCase):
   def test(self):
      linked_list = LinkedList()
      linked_list.push_back(1)
      linked_list.push_back(2)
      linked_list.push_back(3)
      self.assertFalse(linked_list.empty())
      self.assertEqual(linked_list.pop_front(), 1)
      self.assertEqual(linked_list.pop_front(), 2)
      self.assertEqual(linked_list.pop_front(), 3)
      self.assertTrue(linked_list.empty())

class TestPushBackPopBack(unittest.TestCase):
   def test(self):
      linked_list = LinkedList()
      linked_list.push_back(1)
      linked_list.push_back("foo")
      linked_list.push_back([3, 2, 1])
      self.assertFalse(linked_list.empty())
      self.assertEqual(linked_list.pop_back(), [3, 2, 1])
      self.assertEqual(linked_list.pop_back(), "foo")
      self.assertEqual(linked_list.pop_back(), 1)
      self.assertTrue(linked_list.empty())
      
class TestInitialization(unittest.TestCase):
   def test(self):
      linked_list = LinkedList(("one", 2, 3.141592))
      self.assertEqual(linked_list.pop_back(), "one")
      self.assertEqual(linked_list.pop_back(), "2")
      self.assertEqual(linked_list.pop_back(), "3.141592")
      
class TestStr(unittest.TestCase):
   def test(self):
      linked_list = LinkedList((1, 2, 3))
      self.assertEqual(linked_list.__str__(), '1,2,3')
      
class TestRepr(unittest.TestCase):
   def test(self):
      linked_list = LinkedList((1, 2, 3))
      self.assertEqual(linked_list.__repr__(), 'LinkedList((1,2,3))')
      
class TestErrors(unittest.TestCase):
   def test_pop_front_empty(self):
      self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())
      
   def test_pop_back_empty(self):
      self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())
      
      
def fact(number):
   if number < 0:
      raise ValueError("Less than zero")
   if number == 0 or number == 1:
      return 1
      
   stack = LinkedList()
   while number > 1:
      stack.push_front(number)
      number -= 1
      
   result = 1
   while not stack.empty():
      result *= stack.pop_front()
      
   return result
   
class TestFactorial(unittest.TestCase):
   def test_less_than_zero(self):
      self.assertRaises(ValueError, lambda: fact(-1))
      
   def test_zero(self):
      self.assertEqual(fact(0), 1)
      
   def test_one(self):
      self.assertEqual(fact(1), 1)

   def test_two(self):
      self.assertEqual(fact(2), 2)

   def test_10(self):
      self.assertEqual(fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
      
if '__main__' == __name__:
   unittest.main()



