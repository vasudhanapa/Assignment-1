#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed  in a comma-separated sequence on a single line. 
# 

# In[6]:


list = [ x for x in range(2000,3200) if x % 7 == 0 and x % 5 != 0]
print(list, sep= ',')


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[7]:


fname = input("Write your first name: ")
lname = input("Write your last name: ")
print("Hello"+""+lname+""+fname)


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3 

# In[10]:


r = float(input("Enter the radius: "))
volume = (4* 3.1425 * r * r * r)/3
print("Volume of sphere is: ",volume)


# In[ ]:




