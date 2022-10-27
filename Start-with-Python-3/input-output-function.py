# Ask user name and print user name
'''
user_name=input("What is your name? ")
print("Hello "+user_name)
'''

#Ask user age and add 5 with that age
'''
user_age=input("What is your age? ")
age=int(user_age)
print(age)
print("Your age is", age+5)
'''

# print(type(input))

'''
Sep Keyword

print("hello world\n",10)
print("hello wold","hello python","Goon evening",sep="**")
print('Hello world',sep="***")
'''

#End keyword
'''
print("I love Python",end="***")
print("THis is my friend",end="\n")
print("THis is my laptop",end="\n")
'''

# print('i love python','hello world',sep="---",end="***")

# file_name=open('./learn.txt',"a")
# print("I love javascript language",file=file_name)


from time import sleep
# output is not flushed here
print("This will work ",end="",flush="True")
sleep(1)
print("After five second")

frozen= frozenset({'banana', 'cherry', 'apple'})
print(frozen)
# print(type(frozen))

