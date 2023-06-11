#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

#printing the top 10 rows
display(data.head(10))

plt.show()


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

# Scatter plot w day against tip
plt.scatter(data['age'], data['balance'])

# Adding Title to the plot
plt.title("Program Data Bank")

# Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('balance')

plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

# Scatter plot w day against tip
plt.plot(data['age'])
plt.plot(data['balance'])


# Adding Title to the plot
plt.title("Program Data Bank")

# Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('balance')

plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

# Scatter plot w day against tip
plt.bar(data['age'], data['balance'])

# Adding Title to the plot
plt.title("Program Data Bank")

# Setting the X and Y labels
plt.xlabel('age')
plt.ylabel('balance')

plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

# Scatter plot w day against tip
plt.hist(data['age'])

# Adding Title to the plot
plt.title("Histogram")

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("data bank.csv")

# Scatter plot w day against tip
sales = ['age', 'balance']
datasales = [23, 10]

plt.pie(datasales, labels=sales)

plt.title("Program Data Bank")

plt.show() 


# In[ ]:


import matplotlib.pyplot as plt

#creating data

