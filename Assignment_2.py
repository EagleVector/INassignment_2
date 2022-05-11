#!/usr/bin/env python
# coding: utf-8
Q1.What are the two values of the Boolean data type? How do you write them?
Ans. Boolean data types are:
1. True
2. False
If the expression is correct it returns True otherwise it returns False
# In[1]:


3 == 3


# In[2]:


7 > 9

Q2. What are the three different types of Boolean operators?
Ans. 1. And
2. Or
3. NotQ3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
Ans. 
and truth table:
True and True = True
True and False = False
False and True = False
False and False = False
or truth table:
True or True = True
True or False = True
False or True = True
False or False = False
not truth table:
not True = False
not False = TrueQ4. What are the values of the following expressions?
(5 > 4) and (3 == 5) : False
not (5 > 4) : False
(5 > 4) or (3 == 5) : True
not ((5 > 4) or (3 == 5)) : False
(True and True) and (True == False) : False
(not False) or (not True) : True5. What are the six comparison operators?
Ans.
1. ==
2. !=
3. >
4. <
5. >=
6. <=6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
Ans.
Equal to operator will return a boolean output when used. It is a comparison operator.It checks whether the both sides of an expression are equal or not. Symbol = '=='
Assignment operator assigns a value to a variable and stores it in the memory
# In[3]:


a = 5
b = 6
print(a == b)


# In[7]:


#Q7. Identify the three blocks in this code:
#Ans. There is an indentation error in this code
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')


# In[11]:


#Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
#Greetings! if anything else is stored in spam.

spam = int(input("Enter the value you wish to store inside spam: "))
if(spam == 1):
    print("Hello")
elif(spam == 2):
    print("Howdy")
else:
    print("Greetings!")

Q9.If your programme is stuck in an endless loop, what keys you’ll press?
Ans: Will first interrupt the kernel and then restart the kernel.10. How can you tell the difference between break and continue?
Ans. Break statement in python is used to make the program jump out of the loop once the condition inside the loop satisfy. Whereas continue statement makes the program run again everytime the condition inside the loop satisfies.
# In[31]:


def break_example(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)
            break
    print("Done")


# In[32]:


break_example(6)


# In[33]:


def cont_example(n):
    for i in range(n):
        if i % 2 == 0:
            print(i)
            continue
    print("Done")


# In[34]:


cont_example(6)

Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
Ans. All the three range are the same here. In range(0,10,1), 0 is the start point(inclusive) , 10 is the end point(exclusive) and 1 is the jump.
# In[1]:


#Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)
    


# In[1]:


j=1
while j<=10:
    print(j)
    j+=1

Q13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?
Ans. We can do it by either writing
import spam.bacon 
or
from spam import bacon