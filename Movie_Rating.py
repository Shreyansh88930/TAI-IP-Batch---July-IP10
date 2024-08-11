#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MOVIE RATING ANALYSIS- LEVEL2- TASK-1


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# LOADING THE DATASET
df= pd.read_csv("D:/movie.csv")


# In[4]:


# DISPLAYING THE FIRST 5 ROWS OF THE DATASET
df.head()


# In[5]:


# DATA CLEANING
df.isnull().sum()


# In[6]:


print("\nBasic Information:")
print(df.info())


# In[7]:


# DROP ROWS WITH MISSING VALUES
df= df.dropna()


# In[8]:


# Display the first few rows of the dataframe to understand its structure
print("First few rows of the dataset:")
print(df.head())

# Calculate the average rating (since each review has a single rating, this is just the mean of all labels)
average_rating = df['label'].mean()
print("\nAverage rating for all reviews:", average_rating)

# Identify highly rated reviews (label == 1)
highly_rated_reviews = df[df['label'] == 1]
print("\nNumber of highly rated reviews (label == 1):", len(highly_rated_reviews))

# Add a column for the length of each review
df['review_length'] = df['text'].apply(len)

# Plot histograms of review lengths
plt.figure(figsize=(10, 5))
sns.histplot(df['review_length'], bins=30, kde=True)
plt.title('Distribution of Review Lengths')
plt.xlabel('Review Length')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of review length vs. rating
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='review_length', y='label', alpha=0.3)
plt.title('Review Length vs. Rating')
plt.xlabel('Review Length')
plt.ylabel('Rating (Label)')
plt.show()

# Additional visualizations (if any specific user demographics or genres were included, which they are not in this dataset)
# Example: Visualize the distribution of ratings
plt.figure(figsize=(10, 5))
sns.countplot(x='label', data=df)
plt.title('Distribution of Ratings')
plt.xlabel('Rating (Label)')
plt.ylabel('Count')
plt.show()


# In[ ]:




