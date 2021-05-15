# Create new command
print("Xin chao")

# Python distinguishes spaces to create blocks of code
if 5 > 3:
    print("5 lon hon 3 la dung")

# This is a comment, It have hashtag '#' at the beginning of the command line

"""
Python khong co khai niem comment nhieu dung, nhung ban co the su dung \"\"\"
De tao comment nhieu dong
Boi vi python se bo qua cac lenh string nhieu dong neu khong khi bao bien
"""

# Create new variables
x = 10
y = 2
name = "Vang"
_data = "data"
print(_data)
a = b = c = "Vang"
print(a)
print(b)
print(c)

# Casting
x = str(3)
y = int(3)
z = float(3)

# Get the type of a variable
print(type(x))

# Case-Sensitive
# Variable names are case-sensitive.
x = 2
X = "Two"
if type(x) != type(X):
    print("variable x not equals variable X")

# Multi Words Variable Names
abc = 123
ABC = 123
aBC = 123
a_b_c = 123
_abc = 123

# Many Values to Multiple Variables
e, d, f = "a", "b", "c"
print(e)
print(d)
print(f)

# One Value to Multiple Variables
a = b = c = 10

# Unpack a Collection
data = [1, 2, 3]
x, y , z = data
print(x)
print(y)
print(z)


# Output Variables
# To combine both text and a variable, Python uses the + character:
x = 'Huynh Minh'
print('My name is ' + x + ' Vang')

# You can also use the + character to add a variable to another variable:
x = 'Python is '
y = 'awesome'
z = x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 7
z = x + y
print(z)

# Global Variables
x = 10

def myFunc(): 
    print('X = ' + str(x))
myFunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
"""

