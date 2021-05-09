My Blog post url:
https://abayomidare.medium.com

base simply mean things are moving in sequence of what ever the number is

Keywords are predefined, reserved words used in programming that have special meanings to the compiler


my view of keywords:

break:The break keyword is used to break out a for loop, or a while loop.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. ...
In Python everything is an object. When an object is said to be iterable, it means that you can step through 

An iterator is an object that contains a countable number of values.


for i in range(9):
  if i > 3:
    break
  print(i)

else:
The else keyword is used in conditional statements (if statements), and decides what to do if the condition is False.
The else keyword can also be use in try...except blocks,


not:
The not keyword is a logical operator.
The return value will be True if the statement(s) are not True, otherwise it will return False.
x = False

print(not x)

try:
The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.

A function is a block of code which only runs when it is called.



len() 	Returns the length of an object
len() is a built-in function in python. You can use the len() to get the length of the given string, array, list, tuple, dictionary, etc. You can use len function to optimize the performance of the program. The number of elements stored in the object is never calculated, so len helps provide the number of elements.
mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)

map() 	Applies a function to every item of an iterable

an iterable object is some kind of collection of items, for instance: a list of number, a string of characters, a range,etc

Python’s map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable. map() is one of the tools that support a functional programming style in Python.
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))



#convert the map into a list, for readability:
print(list(x))

https://realpython.com/python-map-function/

next() 	Retrieves the next item from an iterator
Python next() function is used to fetch next item from the collection. It takes two arguments an iterator and a default value and returns an element. This method calls on iterator and throws an error if no item is present. To avoid the error, we can set a default value

mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

range() 	Generates a range of integer values
a particular order in which related things follow each other.
The range() function is used to generate a sequence of numbers over time. At its simplest, it accepts an integer and returns a range object (a type of iterable).
x = range(6)
for n in x:
  print(n)

reversed() 	Returns a reverse iterator

The reversed() function allows us to process the items in a sequence in reverse order. It accepts a sequence and returns an iterator. A sequence list string, list, tuple etc. To produce the result at once we have wrapped reversed() in a list() call.

alph = ["a", "b", "c", "d"]

ralph = reversed(alph)

for x in ralph:
  print(x)

Simple Interest= P x R x T ÷ 100,




  https://www.w3schools.com/python/python_regex.asp
  LOWER UPPER


