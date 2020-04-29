#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #data processing
import numpy as np #linear algebra
import matplotlib.pyplot as plt #for visualization


# In[2]:


#import the data from csv file
playdata=pd.read_csv("E:\data science videos\data sets\googleplaystore.csv")


# In[3]:


#for quick view on data from starting
print(playdata.head())


# In[4]:


np.shape(playdata) #for checking how many rows and columns in data


# In[5]:


#data cleaning steps
playdata['Rating'].isnull() #for checking how many null values in cloumn rating,if it present then it shows true


# In[6]:


playdata.isnull()  #for checking how many null values in our data set,if it present then it shows true


# In[7]:


#show nan values and varies with device as null
missing_values=["NAN","Varies with device"]
playdata=pd.read_csv("E:\data science videos\data sets\googleplaystore.csv",na_values=missing_values)
playdata.isnull()


# In[8]:


playdata.isnull().sum()


# In[9]:


playdata.isnull().sum().sum() #total counting of null values


# In[10]:


playdata.notnull().sum().sum() #total counting of not null values


# In[11]:


#pie chart representation between null values and not null values
data='Valid','Not Valid'
total=[134930,6003]
explode=(0,0.1)
plt.pie(total,explode=explode,labels=data,autopct='%1.2f%%',shadow=True)
plt.axis('equal')
plt.show()


# In[12]:


playdata.fillna(0,inplace=True) #on null value place 0


# In[13]:


playdata.head() #after cleaning view on data


# In[14]:


playdata.isnull() #now again after cleaning complete whether any null value is present


# In[15]:


playdata['Rating'].describe() 


# In[16]:


count=playdata['Last Updated'].value_counts()#count total values in last updated column


# In[17]:


df=pd.DataFrame(playdata)


# In[18]:


df['Rating'] = df['Rating'].astype(float) #Change rating column into float type


# In[19]:


#replace the one value with another values
playdata.Size = playdata.Size.str.replace("k"," ")
playdata.Size=playdata.Size.str.replace("M","000")
playdata.Reviews=playdata.Reviews.str.replace("M","000")


# In[20]:


playdata.Price=playdata.Price.str.replace("$"," ")
playdata['Content Rating']=playdata['Content Rating'].str.replace("17"," ")
playdata['Content Rating']=playdata['Content Rating'].str.replace("+"," ")
playdata['Content Rating']=playdata['Content Rating'].str.replace("10"," ")
playdata.Installs=playdata.Installs.str.replace("+"," ")
playdata.Installs=playdata.Installs.str.replace(","," ")
playdata.Reviews=pd.to_numeric(playdata.Reviews)


# In[21]:


playdata.head(n=200)


# In[22]:


free=playdata[playdata.Type=="Free"]
paid=playdata[playdata.Type=="Paid"]


# In[23]:


#graphical representation of camparing free and paid data
free.Reviews.plot(kind="line",color="r",linestyle=":",alpha=.7,
                  grid=True,linewidth=2,figsize=(12,6),label="Free")
paid.Reviews.plot(kind="line",color="b",linestyle=":",alpha=1, 
          grid=True,linewidth=2,figsize=(12,6),label="Paid")
plt.legend()
plt.xlabel("İndex")
plt.ylabel("Reviews")
plt.title("Free-Paid")


# In[24]:


df['Size']=pd.to_numeric(df['Size'],errors='coerce')#change the size dtype column into numeric


# In[25]:


#Histogram representation of data according to their size wise
df['Size'].plot(kind="hist",bins=50,figsize=(12,6))
plt.xlabel("Sizes")
plt.title("Size Wise Distribution")


# In[26]:


df['Rating']=pd.to_numeric(df['Rating'],errors='coerce')


# In[27]:


#find the top 10 ratings
max_rating=df.nlargest(10,'Rating',keep="last")
print(max_rating)


# In[28]:


#bar graph representation of data according to their content rating
playdata['Content Rating'].value_counts().plot(kind="bar",color=(0.2,0.4,0.6,0.6))
plt.yscale("log")
plt.xlabel("Content According to their Category")
plt.title("Content Rating Distribution")


# In[29]:


#top 10 rating of distribution with their size and reviews
max_rating.plot(kind = "bar",figsize = (12,6))
plt.yscale("log")
plt.xlabel("Data Range")
plt.title("Top 10 Rating of Distribution")


# In[30]:


playdata.Category=playdata.Category.astype("category")


# In[31]:


#barh representation of of category according to their total count
xc=playdata.Category.value_counts()
xc.plot(kind='barh',figsize= (12,8))
plt.title("Category Distribution according to their Number of Values in data")


# In[32]:


for v in playdata.Genres:
    print(v)


# In[33]:


if 'Music' in playdata.Genres:
    print("False")
else:
    print("True")


# In[34]:


pd.Series(playdata.Genres)


# In[ ]:





# In[ ]:




