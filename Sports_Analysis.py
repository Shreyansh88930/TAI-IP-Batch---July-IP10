#!/usr/bin/env python
# coding: utf-8

# In[1]:


# SPORTS DATA ANALYSIS- LEVEL-1 TASK-2


# In[2]:


import pandas as pd              # Pandas is used for data manipulation and analysis, particularly for working with data frames.
import matplotlib.pyplot as plt    # Matplotlib is used for creating static, animated, and interactive visualizations in Python.
import seaborn as sns              # Seaborn is a data visualization library based on matplotlib


# In[3]:


# Load the dataset
df = pd.read_csv('D:/fifa_stats.csv')


# In[4]:


# Displaying the first 5 rows of the dataset
print(df.head())


# In[5]:


# Data Cleaning and Preprocessing
# Convert 'Joined' column to datetime format
df['Joined'] = pd.to_datetime(df['Joined'], errors='coerce')
# Using pd.to_datetime() to convert these string values into datetime objects.
# 'Coerce'->
# If any date conversion fails (due to incorrect format or invalid date),
# The 'coerce' option ensures that those entries are converted to 'NaT' (Not a Time).
# 'NaT' is a special datetime value used to represent missing or undefined dates, which ensures consistent handling


# In[6]:


# Drop rows with missing values in 'Joined', 'Overall', and 'Name'
df_cleaned = df.dropna(subset=['Joined', 'Overall', 'Name'])
# Use the dropna() method to remove rows with missing values.
# The subset parameter specifies the columns to check for missing values.


# In[7]:


# Select top 5 players based on frequency
top_players = df_cleaned['Name'].value_counts().index[:5]
# Use the value_counts() method on the 'Name' column to get a Series of player names
# The Series will contain player names as the index and their corresponding counts (frequency of appearances) as values.
# This method counts the number of occurrences of each unique value in the 'Name' column.
# By using index[:5], we select the first 5 player names from the Series.


# In[8]:


# Filter data for the top players
df_top_players = df_cleaned[df_cleaned['Name'].isin(top_players)]
# The isin() method is used to filter rows based on whether the 'Name' column value
# is in the list of top players (top_players).
# df_cleaned['Name'].isin(top_players) creates a boolean mask.
# This mask is True for rows where the 'Name' value is in the top_players list and False otherwise.


# In[9]:


# 1. Line plot to show player performance over time
# Create a new figure for the plot with a specified size (12 inches wide by 6 inches tall).
plt.figure(figsize=(12, 6))
# hue='Name': Different lines in the plot will represent different players, distinguished by their names.
sns.lineplot(x='Joined', y='Overall', hue='Name', data=df_top_players)
plt.title('Player Performance Over Time')
plt.xlabel('Date')
plt.ylabel('Overall Rating')
plt.legend(title='Player')
plt.show()


# In[10]:


# Print the filtered data to check for any issues
print(df_top_players)


# In[11]:


# 1. Line plot to show player performance over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Joined', y='Overall', hue='Name', data=df_top_players)
plt.title('Player Performance Over Time')
plt.xlabel('Date')
plt.ylabel('Overall Rating')
plt.legend(title='Player')
plt.show()


# In[12]:


# Extract the year from 'Joined' as the season
df['Season'] = df['Joined'].dt.year  
# Use the .dt accessor to access the datetime attributes of the 'Joined' column.
# The .year attribute extracts the year part from each datetime value in the 'Joined' column.

# Drop rows with missing values in 'Season', 'Overall', and 'Club'
df_cleaned = df.dropna(subset=['Season', 'Overall', 'Club'])


# In[13]:


# Select top 10 clubs based on frequency
top_clubs = df_cleaned['Club'].value_counts().index[:10]


# In[14]:


# Filter data for the top clubs
df_top_clubs = df_cleaned[df_cleaned['Club'].isin(top_clubs)]
# The isin() method is used to filter rows based on whether the 'Club' column value
# is in the list of top clubs (top_clubs).

# df_cleaned['Club'].isin(top_clubs) creates a boolean mask.
# This mask is True for rows where the 'Club' value is in the top_clubs list and False otherwise.


# In[15]:


# Group by Season and Club to get the mean Overall rating
df_grouped = df_top_clubs.groupby(['Season', 'Club'])['Overall'].mean().reset_index()
# reset_index() turns this MultiIndex into regular columns in a new DataFrame.


# In[16]:


# Plotting
plt.figure(figsize=(14, 8))
sns.barplot(x='Season', y='Overall', hue='Club', data=df_grouped)
plt.title('Average Team Rankings Across Seasons')
plt.xlabel('Season')
plt.ylabel('Average Overall Rating')
plt.legend(title='Club')
plt.show()


# In[17]:


# Data Cleaning and Preprocessing
# Drop rows with missing values in 'Overall'
df_cleaned = df.dropna(subset=['Overall'])

# Plotting the Histogram
plt.figure(figsize=(10, 6))  # Set the size of the plot
sns.histplot(data=df_cleaned, x='Overall', bins=10, kde=True)  # Create a histogram of 'Overall' ratings with 10 bins and a KDE (Kernel Density Estimate) curve
plt.title('Distribution of Overall Ratings')  # Set the title of the plot
plt.xlabel('Overall Rating')  # Set the label for the x-axis
plt.ylabel('Frequency')  # Set the label for the y-axis
plt.show()  # Display the plot


# In[19]:


# Drop rows with missing values in 'Age', 'Overall', 'Name', or 'Potential'
df_cleaned = df.dropna(subset=['Age', 'Overall', 'Name', 'Potential'])

# Plotting the Scatter Plot with sampled data
plt.figure(figsize=(8, 5))  # Adjusted smaller size
sns.scatterplot(data=df_cleaned.sample(n=1000), x='Age', y='Overall', hue='Name', size='Potential', sizes=(10, 100), alpha=0.7)  # Adjusted sizes
plt.title('Relationship between Age and Overall Rating')
plt.xlabel('Age')
plt.ylabel('Overall Rating')

# Adjust legend position below the plot
plt.legend(title='Player', bbox_to_anchor=(0.5, -0.3), loc='upper center', ncol=7)  # Centered below with 5 columns

plt.tight_layout()  # Adjust layout for better presentation
plt.show()


# In[ ]:




