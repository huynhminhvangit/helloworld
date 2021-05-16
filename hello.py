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

# Python Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Python Strings
print("Hello")
print('Hello')
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

# Python - Slicing Strings
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])
# Slice To the End
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
b = "Hello, World!"
print(b[-5:-2])

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Methods
"""
capitalize()	  Converts the first character to upper case
casefold()	    Converts string into lower case
center()	      Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	      Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()	  Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	      Formats specified values in a string
format_map()	  Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	      Returns True if all characters in the string are alphanumeric
isalpha()	      Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	      Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	      Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	  Returns True if all characters in the string are printable
isspace()	      Returns True if all characters in the string are whitespaces
istitle()	      Returns True if the string follows the rules of a title
isupper()	      Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()    	  Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	      Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	      Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	  Returns a tuple where the string is parted into three parts
rsplit()	      Splits the string at the specified separator, and returns a list
rstrip()	      Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	  Splits the string at line breaks and returns a list
startswith()	  Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
"""

# String Concatenation
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)


# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format
"""
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)
"""

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Python - Escape Characters
"""
Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

"""
'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ ooo	Octal value	
\ xhh	Hex value
"""
