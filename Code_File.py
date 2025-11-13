#!/usr/bin/env python
# coding: utf-8

# # Activity: Full OSEMN

# ## Introduction
# 
# In this assignment, you will work on a data analysis project. This project will
# let you practice the skills you have learned in this course and write real code
# in Python.
# 
# You will perform the following steps of the OSEMN framework:  
# - [Scrub](#scrub)
# - [Explore](#explore)
# - [Interpret](#interpret)

# In[1]:


# We'll import the libraries you'll likely use for this activity
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data
df = pd.read_csv('transactions-pet_store.csv')
df_orig = df.copy()


# ## Scrub
# 
# You will scrub the data. It's important that you follow the directions as
# stated. Doing more or less than what is asked might lead to not getting full
# points for the question.
# 
# ------
# 
# If while you're working on the scrubbing phase you need to reset the DataFrame,
# you can restart the kernel (in the toolbar: "Kernel" > "Restart").

# #### Question 1
# 
# Remove all rows that have are missing either the `Product_Name` or the
# `Product_Category`. Assign the cleaned DataFrame to the variable `df`
# (overwriting the original DataFrame.).

# In[11]:


# Your code here
df=df.dropna(subset=['Product_Name','Product_Category'])
df.describe()
# your code here


# In[5]:


# Question 1 Grading Checks

assert df.shape[0] <= 2874, 'Did you remove all the rows with missing values for the columns Product_Name & Product_Category?'
assert df.shape[0] >= 2700, 'Did you remove too many the rows with missing values?'
assert len(df.columns) == 10, 'Make sure you do not drop any columns.'


# #### Question 2
# 
# Find any clearly "incorrect" values in the `Price` column and "clean" the
# DataFrame to address those values.
# 
# Ensure you make the changes to the DataFrame assigned to the variable `df`.

# In[20]:


df_test = df[~(df['Product_Name'] == 'MissingNo Plush')] 
df= df_test



# your code here


# In[21]:


# Question 2 Grading Checks

assert (df.Price < df.Price.quantile(0.0001)).sum() == 0, 'Check for very small values'
assert (df.Price > df.Price.quantile(0.999)).sum() == 0, 'Check for very large values'


# #### Question 3
# 
# After you've done the cleaning above, remove any column that has more than `500`
# missing values.
# 
# Ensure you make the changes to the DataFrame assigned to the variable `df`.

# In[24]:


# Your code here
df=df.drop(columns='Size')
# your code here


# In[25]:


# Question 3 Grading Checks

assert len(df.columns) < 10, 'You should have dropped 1 or more columns (with more than 500 missing values)'


# #### Question 4
# 
# Address the other missing values. You can replace the values or remvove them,
# but whatever method you decide to clean the DataFrame, you should no longer have
# any missing values.
# 
# Ensure you make the changes to the DataFrame assigned to the variable `df`.

# In[32]:


# Your code here
df=df.dropna(subset=['Customer_ID'])
df.info()

# your code here


# In[33]:


# Question 4 Grading Checks

assert df.Customer_ID.isna().sum() == 0, 'Did you address all the missing values?'


# ## Explore
# 
# You will explore the data. It's important that you follow the directions as
# stated. Doing more or less than what is asked might lead to not getting full
# points for the question.
# 
# You may use either exploratory statistics or exploratory visualizations to help
# answer these questions.
# 
# ------
# 
# Note that the DataFrame loaded for this section (in the below cell) is different
# from the data you used in the [Scrub](#scrub) section.
# 
# If while you're working on the scrubbing phase you need to reset the DataFrame,
# you can restart the kernel (in the toolbar: "Kernel" > "Restart").

# In[34]:


df = pd.read_csv('transactions-pet_store-clean.csv')


# #### Question 5
# 
# Create a `Subtotal` column by multiplying the `Price` and `Quantity` values. 
# This represents how much was spent for a given transaction (row).

# In[36]:


# Your code here
df['Subtotal']= df.Price * df.Quantity
df
# your code here


# In[37]:


# Question 5 Grading Checks

assert 'Subtotal' in df.columns, ''


# #### Question 6
# 
# Determine most common category (`Product_Category`) purchases (number of total
# items) for both `Product_Line` categories. Assign the (string) name of these
# categories to their respective variables `common_category_cat` & 
# `common_category_dog`.

# In[88]:


# Your code here
df_dog = df[df['Product_Line'] == 'dog']
df_dog.groupby('Product_Category').count()
df_cat = df[df['Product_Line'] == 'cat']
df_cat.groupby('Product_Category').count()
common_category_cat = 'treat'
common_category_dog = 'bedding'

# your code here


# In[56]:


# Question 6 Grading Checks

assert isinstance(common_category_dog, str), 'Ensure you assign the name of the category (string) to the variable common_category_dog'
assert isinstance(common_category_cat, str), 'Ensure you assign the name of the category (string) to the variable common_category_cat'


# #### Question 7
# 
# Determine which categories (`Product_Category`), by `Product_Line` have the
# ***median*** highest `Price`.
# Assign the (string) name of these categories to their respective variables
# `priciest_category_cat` & `priciest_category_dog`.

# In[60]:


# Your code here
df_cat.groupby('Product_Category')['Price'].median()
priciest_category_dog= 'toy'
priciest_category_cat = 'bedding'
# your code here


# In[61]:


# Question 7 Grading Checks

assert isinstance(priciest_category_dog, str), 'Ensure you assign the name of the category (string) to the variable priciest_category_dog'
assert isinstance(priciest_category_cat, str), 'Ensure you assign the name of the category (string) to the variable priciest_category_cat'


# ## Modeling
# 
# This is the point of the framework where we'd work on modeling with our data.
# However, in this activity, we're going to move straight to interpretting.

# ## Interpret
# 
# You will interpret the data based on what you found so far. It's important that
# you follow the directions as stated. Doing more or less than what is asked might
# lead to not getting full points for the question.
# 
# 
# ------
# 
# Note that the DataFrame loaded for this section (in the below cell) is the same
# as the data you used in the [Explore](#explore) section.
# 
# If while you're working on the scrubbing phase you need to reset the DataFrame,
# you can restart the kernel (in the toolbar: "Kernel" > "Restart").

# #### Question 8
# 
# You want to emphasize to your stakeholders that the total number of product
# categories sold differ between the two `Product_Line` categories (`'cat'` & 
# `'dog'`).
# 
# Create a **_horizontal_ bar plot** that has `Product_Category` on the y-axis and
# the total number of that category sold (using the `Quantity`) by each 
# `Product_Line` category. Also **change the axis labels** to something meaningful
# and add a title.
# 
# You will likely want to use Seaborn. Make sure you set the result to the
# variable `ax` like the following:
# ```python
# ax = # code to create a bar plot
# ```

# In[86]:


# Your code here
ax=sns.barplot(x=df['Quantity'], y=df['Product_Category'], estimator=sum, hue= df['Product_Line'])

# Set custom axis labels and title
plt.xlabel('Quantity by Product Line')
plt.ylabel('Product Category')
plt.title('Product Categorical Sales')

# your code here


# In[87]:


# Question 8 Grading Checks

assert isinstance(ax, plt.Axes), 'Did you assign the plot result to the variable ax?'


# #### Question 9
# 
# Based on the plot from [Question 8](#question-8), what would you conclude for
# your stakeholders about what products they should sell? What would be the
# considerations and/or caveats you'd communicate to your stakeholders?
# 
# Write at least a couple sentences of your thoughts in a string assigned to the
# variable `answer_to_9`.
# 
# The cell below should look something like this:
# ```python
# answer_to_9 = '''
# I think that based on the visualization that ****.
# Therefore I would communicate with the stakeholders that ****
# '''
# ```

# In[89]:


# Your code here
answer_to_9 = '''
I think based on the visualisation the company has strong market for treats and bedding and should really emphasis on those categories to improve sales. 
There is a strong potential in the treats market for dogs as well as in bedding market for cats.
'''
print(len(answer_to_9))
# your code here


# In[90]:


# Question 9 Grading Checks

assert isinstance(answer_to_9, str), 'Make sure you create a string for your answer.'


# #### Question 10
# 
# The plot you created for [Question 8](#question-8) is good but could be modified
# to emphasize which products are important for the business.
# 
# Create an explanatory visualization that emphasizes the insight you about the
# product category. This would be a visualization you'd share with the business
# stakeholders.
# 
# Make sure you set the result to the variable `ax` like the following:
# ```python
# ax = # code to create explanatory visualization
# ```

# In[94]:


# Your code here
ax= df['Price'].plot.box()
# your code here


# In[95]:


# Question 10 Grading Checks

assert isinstance(ax, plt.Axes), 'Did you assign the plot result to the variable ax?'

