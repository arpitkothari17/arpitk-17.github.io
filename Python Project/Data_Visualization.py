# ! conda install -c conda-forge Plotnine --y 

from plotnine.data import diamonds

import pandas as pd

import seaborn as sns
tips = sns.load_dataset("tips")

diamonds.head(5)
tips.head(5)

from plotnine import *

# the carat and price on scatter plot 
ggplot(aes(x="carat", y="price"), diamonds) + geom_point() + ggtitle("My Diamonds") + ylab("PRICE") + xlab("CARAT") # most important command for 

diamonds.carat.corr(diamonds.price)
#%%
# Q1. Scatterplot to show the top v total_bill
ggplot(aes(x= "tip", y="total_bill"), tips) + geom_point() + ggtitle("Total Bills v Tips")

#%%
# Q2. Scatterplot to show the top v total_bill adding info about the sex of the waiter - aes(x,y,colour)
ggplot(aes(x="tip", y="total_bill", colour="sex"), tips) + geom_point() + ggtitle("Title 1") + xlab("Tips") + ylab("Total Bill")

#%% Diamong with type of cut 
ggplot(aes(x='cut'), diamonds) + geom_bar() + ylab('Number of Diamonds') 

diamonds.cut.value_counts()

#%% Plot a bar graph to show the number of bookings 
# Q1 - By Day
ggplot(aes(x="day"), tips) + geom_bar() + ylab("Number of Bookings") + xlab("Days")

# Q2 - by day and time 
ggplot(aes(x="day", fill="time"), tips) + geom_bar()
# colour is for a point and fill is for an area 
pd.crosstab(tips.day, tips.time)

# Q3 - By day, time and sex. check the option facet_wrap 
ggplot(aes(x="day", fill="time"), tips) + geom_bar() + facet_wrap("sex")

# Q4 - By day, time and sex & Smoer. check the option facet_grid 
ggplot(aes(x="day", fill="time"), tips) + geom_bar() + facet_grid("sex", "smoker")
#%% Price Histogram 
ggplot(aes(x="price"), diamonds) + geom_histogram(fill = "blue")
diamonds.price.median()

#%% 
# Scatter plot to show the tip & total_bill
ggplot(aes(x="tip", y='total_bill'), tips) + geom_point()

# Repeate by day 
ggplot(aes(x="tip", y='total_bill'), tips) + geom_point() + facet_wrap("day")

# Repeate by day  & time 
ggplot(aes(x="tip", y='total_bill', colour = "time"), tips) + geom_point() + facet_wrap("day")

# Repeate by day, time & sex
ggplot(aes(x="tip", y='total_bill', colour = "sex"), tips) + geom_point() + facet_grid("day", 'time')

# Repeate by day, time, sex & smoker 

ggplot(aes(x="tip", y='total_bill', colour = "sex", shape="smoker"), tips) + geom_point() + facet_grid("day", 'time')

#%% Average price by cut & clarity 
avg = diamonds.groupby(by=["clarity", 'cut'], as_index=0).price.mean()
ggplot(aes(x="clarity", fill="cut", y = "price"), avg) + geom_bar(stat="identity", position = "stack")

#%% Cheapest price in every cut 

#%% bloxplot - cut and price 
g1 = ggplot(aes(x="cut", y="price", fill = "clarity"), diamonds) + geom_boxplot() + facet_wrap("clarity") + coord_flip() + scale_fill_brewer(type="qual", palette="Dark2")

#%% to modfiy the colour 
    # scare_colour_gradient - for continous (salary, revenue, etc)
    # scare_colour_brewer - for discrete (gender, nationality, etc)
ggplot(aes(x="carat", y="price", colour="price"), diamonds)  + geom_point() + scale_colour_gradient(low="green",high="#3d7ef1")
ggplot(aes(x="carat", y="price", colour="cut"), diamonds)  + geom_point() + scale_colour_brewer(type="qual", palette="Dark2")
#%% To save
g1.save("G1.pdf") #jpg

#%% Different graphs options 
geom_point() # scatterplot - To identify patterns, trends, or correlations between two variables.
geom_bar() # bar graph - Comparing categories or groups using rectangular bars.
geom_histogram() # histogram - Displaying the distribution of a single continuous variable.




