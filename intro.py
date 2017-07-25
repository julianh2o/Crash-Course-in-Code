#!/usr/bin/env python

#variables and math
a = 5
print("a: ",a)

a = a + 1
print("a: ",a)

a += 5
print("a: ",a)

b = a / 2
c = a / 2.0
print("b: ",b)
print("c: ",c)

d = (a + 10)*c - 1
print("d: ",d)

import math
print(math.sqrt(25))

import os
print os.listdir(".")

print os.path.exists("./intro.py")

#defining functions
def add(a,b):
	return a+b

print(add(1,5))

#conditionals
height = 70
if (height > 60):
	print("you may ride this ride")
else:
	print("you're too short to ride")

#loops
for i in range(10):
	print("{0} times {0} is {1}".format(i,i*i))

s = "a rose"
while(len(s) < 40):
	s += " is a rose"
print(s)


# working with files
f = open("students.csv","r")
contents = f.read()
print(contents.split("\n")[0])

f = open("out.txt","w")
f.write("this is a line 1\n")
f.write("more lines\n")
f.write(str(a))
f.write("\n")
f.write(str(b))
f.write("\n")
f.close()


# manipulating strings
s = "the quick brown fox jumped over the lazy dogs"

print(s[0]) # prints "t"

print(s[4:9]) # prints "quick"

print(s[4:]) # prints "quick brown fox jumped over the lazy dogs"

print(s[-9:]) # prints "lazy dogs"

print(s[10:-10]) # prints "brown fox jumped over the


print(s.upper()) # capitalizes all the letters in a string
print(s.lower()) # lowercases all letters in a string

print(s.find("dogs")) # returns index of the first occurrence
print(s.rfind("the")) # returns index of the last occurrence

print(s.split(" ")) # returns the string broken up on " " as an array
print(s.replace("fox","ferret")) # replaces all occurrences of "fox"
print(",".join(["apples","pears","cherries"])) # joins an array using "," to separate elements

first_name = "John"
last_name = "Doe"
middle_name = "Mildred"
print("{0}, {1} {2}".format(last_name,first_name,middle_name[0])); # fills variables into a pre-formatted string

print(s.rjust(20)) # pads a string to the specified length (right justified)
print(s.center(20)) # pads a string to the specified length (right justified)


# lists
fruits = ["apple","pear","mango"] # define an array using brackets
print(fruits[0]) # prints apple

fruits[0] = fruits[0].upper()
print(fruits) # prints ['APPLE', 'pear', 'mango']

for fruit in fruits:
    print(fruit[0:2])


# dictionaries
scores = {"john":5,"jill":7,"billy":1,"stephanie":4}

print(scores["billy"]) # prints 1

scores["billy"] += 1
print(scores) # prints {'billy': 2, 'john': 5, 'stephanie': 4, 'jill': 7}

activePlayer = "john"
print(scores[activePlayer]) # prints 5
