# Comments enhance the readability of the code and help the programmers to understand the code very carefully. 
# There are three types of comment in Python-
# 1. Single line Comments
# 2. Multiline line Comments
# 3. Docstring line Comments 

# Multi
# line
# comment

'''
This is a
docstring
comment
'''

def multiply(a,b):
    '''Multiplies the value of a and b'''
    return a*b

result=multiply(3,9)
print(result)

# Print the docstring of multiply function Ctrl+/
print(multiply.__doc__)    

# \n : for creating new line
print("Hello. \nthis will print in a new line.")

# \t : for using tab
print("This will create\tfour space.")

# \\ : will insert one \
print("This will insert one \\ (backslash).")

# \' : for using apostrophe or single quote
print("It\'s alright.")
print("Hey, \'This is a single quote\'")

# \" : For using quotation
print("Hey, \"This is double quote\"")

#\r : for Carriage Return
print("Python is included in CodeSpeedy\r123456")

# \b : for giving backspace
print("Hello \bWorld")
print("Hello\bWorld")

# r"" : for using raw string
print("C:\\Program Files\norton\appx")
print(r"C:\\Program Files\norton\appx")

