#!/usr/bin/env python
# coding: utf-8

# Q1. Explain with an example each when to use a for loop and a while loop.

# for loop: It is used to iterate over sequence.we use for loop when we simply want to run the code to meet a general requirement.
# while loop: It iterates the loop till the condition is true.

# In[1]:


# For loop
for i in range(11):
    print(i)
print("**************************")
i = 0
while i <11:
    print(i)
    i += 1


# Q2. Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop.
# 

# In[2]:


#Sum using for loop
sum = 1
for i in range(2,11):
    sum+=i
sum


# In[3]:


#product using for loop
product = 1
for i in range(2,11):
    product = product * i
product


# In[4]:


#sum using while loop
start_point = 0
sum1 = 1

while sum1<=10:
    start_point +=sum1
    sum1 +=1
print(start_point)


# In[5]:


#Product using while loop
start = 1
product = 1

while product <=10:
    start = start *product
    product+=1
print(start)


# Q3. Create a python program to compute the electricity bill for a household.
# 
# The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
# unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
# be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.
# You are required to take the units of electricity consumed in a month from the user as input.
# Your program must pass this test case: when the unit of electricity consumed by the user in a month is
# 310, the total electricity bill should be 2250.

# In[6]:


n = int(input("Enter the units: "))

if n<=100:
    bill = n*4.5
    print("Your electricity bill is: ",bill)
elif n<=200:
    bill = 100*4.5 + ((n-100)*6)
    print("Your electricity bill is: ",bill)
elif n<=300:
    bill = 100*(4.5+6) + ((n-200)*10)
    print("Your electricity bill is: ",bill)
elif n>300:
    bill = 100*(4.5+6+10) + ((n-300)*20)
    print("Your electricity bill is: ",bill)


# 
# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print that list.

# In[7]:


m = list(range(1,101))
n= []
for i in m:
    cube= i*i*i
    print("Cube of "+str(i)+" is ",cube)
    if cube%4==0 or cube%5==0:
        n.append(i)
n


# Q5. Write a program to filter count vowels in the below-given string.
# string = "I want to become a data scientist"

# In[8]:


string = "I want to become a data scientist"
m = ["A","E","O","I","U","a","e","i","o","u"]
count = 0
for i in string:
    if i in m:
        count+=1
print(count)


# In[ ]:




