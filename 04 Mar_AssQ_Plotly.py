#!/usr/bin/env python
# coding: utf-8

# **Q1.** Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
# scatter plot for age and fare columns in the titanic dataset.
# 
# **Ans:**

# In[1]:


import seaborn as sns
import plotly.express as px

titanic_data = sns.load_dataset('titanic')
scatter_plot = px.scatter(titanic_data, x='age', y='fare')
scatter_plot.show()


# **Q2.** Using the tips dataset in the Plotly library, plot a box plot using Plotly express.
# 
# **Ans:**

# In[2]:


import plotly.express as px
from plotly import data

tips_data = data.tips()
box_plot = px.box(tips_data, x='day', y='total_bill')
box_plot.show()


# **Q3.** Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
# the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
# column with the color parameter.
# 
# **Ans:**

# In[3]:


import plotly.express as px
from plotly import data

tips_data = data.tips()
histogram_plot = px.histogram(tips_data, x='sex', y='total_bill', color='day', pattern_shape='smoker')
histogram_plot.show()


# **Q4.** Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
# the color parameter.
# 
# Note: Use "sepal_length", "sepal_width", "petal_length", "petal_width" columns only with the
# dimensions parameter.
# 
# **Ans:**

# In[4]:


import plotly.express as px
from plotly import data

iris_data = data.iris()
scatter_matrix_plot = px.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species")

scatter_matrix_plot.show()


# **Q5.** What is Distplot? Using Plotly express, plot a distplot.
# 
# **Ans:**
# 
# distplot is a function in the seaborn library that is used to plot a univariate distribution of observations. It combines a histogram with a kernel density estimate (KDE) to provide a smooth estimate of the distribution.

# In[5]:


import plotly.express as px
from plotly import data

iris_data = data.iris()
dist_plot = px.histogram(iris_data, x="sepal_length", nbins=20, marginal="rug", opacity=0.7, color_discrete_sequence=["#FF6699"])
dist_plot.show()


# In[ ]:




