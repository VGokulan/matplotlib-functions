#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple Line plot :
import matplotlib.pyplot as plt
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.plot(x,y)
plt.show()


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()


# In[3]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()  
ax = plt.axes()  
x = np.linspace(0, 10, 1000)  
ax.plot(x, np.sin(x))


# In[5]:


plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 4, linestyle='-')  
plt.plot(x, x + 7, linestyle=':');


# In[8]:


#Scatter Plot :

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4,2]
plt.scatter(x, y)
plt.show()


# In[7]:


x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()


# In[9]:


rng=np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')
plt.colorbar();


# In[19]:


#Matplotlib Line

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
plt.plot(xpoints, ypoints)
plt.show()
plt.plot(ypoints, marker = 'o')
plt.show()
plt.plot(ypoints, marker = 'D')
plt.show()
plt.plot(ypoints, linestyle = 'dashed')
plt.show()
plt.plot(ypoints, 'o:y')
plt.show()
plt.plot(ypoints, ls = ':')
plt.show()
plt.plot(ypoints, c = 'hotpink')
plt.show()
plt.plot(ypoints, color = 'r')
plt.show()
plt.plot(ypoints, linewidth = '10.5')
plt.show()
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()


# In[20]:


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)
plt.show()


# In[ ]:




