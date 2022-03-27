#!/usr/bin/env python
# coding: utf-8

# # Question no 1

# In[3]:


count=0
for i in range(32,128,1):
    count+=1
    if(count==16 or count==32 or count==48 or count==64 or count==80):
        print('\r')
    print(chr(i),end=" ")


# # Question no 2

# In[4]:


sum=0
x=int(input('Enter a number: '))
while x<0:
    x=int(input('Plz enter a positive number: '))
for i in range(0,x+1,1):
    sum+=i
print('Your sum is: ',sum)


# # Question no 3

# In[6]:


speed=int(input('Enter speed of vehicle in miles: '))
hours=int(input('Enter hours of vehicle: '))
distance = speed*hours
print('------------------------')
print('Hours Distance Travelled')
print('------------------------')

for i in range(1,hours+1,1):
    print(i,'           ',i*speed)
print('------------------------')


# # Question no 4

# In[9]:


print('Celsius      Fahrenheit     Kelvin')
for i in range(0,21,1):
    print(i,'           ',(i*9/5)+32,'         ',i+273.15)


# # Question no 5

# In[61]:


print('Speed in MPH         Speed in KPH')
print('---------------------------------')
for i in range(60,135,5):
    print(format(i*0.6214,".2f"),'                 ',i)
print('---------------------------------')


# # Question no 6

# In[17]:


day=int(input("How many days employee work: "))
a=1
while day<1 or day>31:
    day=int(input("plz enter days between 1 to 31: "))
print('Day              Salary')
for i in range(1,day+1,1):
    print(i,'               ',a/100)
    a*=2
    


# # Question no 7

# In[ ]:





# # Question no 8

# In[19]:


num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
length=0
width=0


if num1>num2:
    length=num1
    width=num2
else:
    length=num2
    width=num1

for i in range(0,width,1):
    for j in range(0,length,1):
        print('x',end="")
    print('\r')


# # Question no 9

# In[22]:


x=1
a=chr(32)
for i in range(0,3,1):
    print(a*8,end="")
    for j in range(0,x):
        print("+",end="")   
    x+=2
    print("\r")

for k in range(0,14):
    print('+',end="")
print('\r')

d=5
for l in range(0,3,1):
    print(a*8,end="")
    for m in range(0,d):
        print("+",end="")   
    d-=2
    print("\r")


# # Question no 10

# In[ ]:





# # Question no 11

# In[46]:


for i in range(1,6,1):
    for j in range(0,i,1):
        print(j+1,end="")
    for k in range(0,i-1,1):
        print(j,end="")
        j=j-1
    print('\r')
l=4
for i in range(1,5,1):
    for j in range(0,l,1):
        print(j+1,end="")
    for k in range(0,l-1,1):
        print(j,end="")
        j=j-1
    print('\r')
    l=l-1


# # Question no 12

# In[60]:


amount=int(input('Enter initial amount: '))
years=int(input('Enter number of years: '))
interest=float(input('Enter interest rate (percent per year): '))
total=0
total=amount
interest=interest/100
for i in range(0,years,1):
    total=total+(total*interest)
print('At the end of 10 years, you will have: $',format(total,".2f"))


# # Question no 13

# In[ ]:





# # Question no 14

# In[63]:


guests=int(input('Enter number of guests: '))
chairs=int(input('Enter number of chairs: '))
loop1=guests-chairs
outcomes=1
for i in range(guests,loop1,-1):
    outcomes*=i
print('The possible arrangements are: ',outcomes)

