#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Whileloop


# In[2]:


i = 1
while i<6:
    print(i)
    i += 1


# In[3]:


i = 0
while i<=6:
    print(i)
    i += 1


# In[4]:


i = 0
while i<6:
    print(i)
    if i ==3:
        break
    i += 1


# In[5]:


i = 0
while i<6:
    i += 1
    if i == 3:
        continue
    print(i)


# In[6]:


i = 1
while i>6:
    print(i)
    i += 1
else:
    print("i is no longer than 6")


# In[7]:


#Forloop


# In[8]:


Fruits = ["Apple" , "Banana" , "Cherry"]
for x in Fruits:
    print(x)
    if x == "Banana":
        break


# In[9]:


Fruits = ["Apple" , "Banana" , "Cherry"]
for x in Fruits:
    print(x)


# In[10]:


Fruits = ["Apple" , "Banana" , "Cherry"]
for x in Fruits:
    if x == "Banana":
        break
    print(x)


# In[11]:


Fruits = ["Apple" , "Banana" , "Cherry"]
for x in Fruits:
    if x == "Banana":
        continue
    print(x)


# In[12]:


#Rangefunction


# In[13]:


for x in range(6):
    print(x)


# In[14]:


for x in range(2,6):
    print(x)


# In[15]:


for x in range(2,15,3):
    print(x)


# In[16]:


for x in range(6):
    print(x)
else:
    print("Finally Finished")


# In[17]:


for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally Finished")


# In[18]:


#Nestedloop


# In[19]:


a = ["Tasty" , "Love" , "Nice"]
b = ["Apple" , "Banana" , "Cherry"]
for x in a:
    for y in b:
        print(x,y)


# In[20]:


#Pass


# In[21]:


for x in [1,2,3]:
    pass


# In[22]:


#Libraries


# In[23]:


import numpy as np
a = np.arange(10)
s = slice(2,9,2) 
print (a[s])


# In[24]:


a = np.arange(10)
b = a[2:9:2] 
print (b)


# In[31]:


#We can slice them in both terms.[23 , 24]


# In[32]:


a = np.arange(10) 
b = a[5] 
print (b)


# In[33]:


import pandas 


# In[34]:


import pandas as pd
import numpy as np


# In[30]:


info = np.array("S","i","d","d","y","y","y") 
a = pd.Series(info)
print(a)


# In[35]:


import pandas as pd


# In[36]:


x = ['Python' , 'Pandas']
df = pd.DataFrame(x)
print(df)


# In[37]:


x = ['Python' , 'is' , 'a' , 'Programming' , 'Language']
df = pd.DataFrame(x)
print(df)


# In[38]:


import matplotlib.pyplot as plt


# In[39]:


x = np.arange(1,11)
y = 2*x+5
plt.title("Matplot") 
plt.xlabel("x axis") 
plt.ylabel("y axis") 
plt.plot(x,y) 
plt.show()


# In[ ]:




