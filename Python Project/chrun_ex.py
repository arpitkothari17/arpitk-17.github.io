#Pandas Exercise 1 : Session 10
#Data set  pandas churn 

#first I placed in the upper right hand side the folder in which the data set is found in my computer. 
#next step is to import pandas and the file name 

import pandas as pd

#now I create a variable named churn to import the file. it is an xlsx file so we have to put that in the command and in the string inside the command. 
chn = pd.read_excel("Pandas 1_Churn dataset.xlsx")
#Info about these variables is given:
#gender: 0 (male) vs 1 (female)
#start: day of the year when the client started in the company
#time: the tenure of the client in number of days
#churned: 0 (non-churner) vs 1 (churner)

#%%
#A. How many clients are churners and non-churners?
print(chn.loc[chn.churned == 1, "churned"].count()) #churn 
print(chn.loc[chn.churned == 0, "churned"].count()) #non-churn

#%%
#B. Which is the percentage of churns by gender
ma_chn = chn.loc[chn.churned == 1, :].loc[chn.gender == 0, "gender"].count() # counting total churn in male 
fe_chn = chn.loc[chn.churned == 1, :].loc[chn.gender == 1, "gender"].count() # counting total churn in femal
tot_chn = chn.loc[chn.churned ==1, "gender"].count() # counting total churn 

per_tot = (fe_chn/tot_chn)*100 # calculating percentage of female churn in total churn
print(per_tot.round(2),"%")

perm_tot = (ma_chn/tot_chn)*100 # calculating percentage of male churn in total churn
print(perm_tot.round(2), "%")

#%%
#C. How much is the average time if we compare churners vs non-churners clients? Do we have differencies?
ch = chn.loc[chn.churned == 1, "time"] # extracting time for churn 
ch.mean().round(2) # taking the mean with 2 decimal point

ch.time.mean()

nch = chn.loc[chn.churned == 0, "time"] # extracting time for non churn  
nch.mean().round(2) # taking the mean with 2 decimal point

# Looking at the result, the mean of churn time is 121.62 and the mean of non churn is 174.79 
# We do have differences in the time meaning the non churn clients stays longer for about 53 days on average before leaving 
#%%
#D. Enumerate 3 factors/variables you would consider discriminating to find churners. Explain the reasons to select these 3 factors.

# Based on above exercise, the 3 discriminating factors to be cosidered while finding churners are: 
        # Gender - We observed 76% of churn in male compared to 23% in female. Hence, it is important to understand why male customers are leaving more frequently than female customers 
        # Time - Analysing the gap of 53 days. How can the company overcome the threshold of 121 days. Maybe the company needs to optimise its efforts from day 100 to ensure better customer satisaction, specially in male customrs 
        # Start - The mean of start for churners is 122 compared to non churners which is 190. That mean, those who start working earlier in the year, tend to leave sooner than those who start working later, with the difference of 68 days.

# Analysing these 3 variable for churners vs non churners gives us better clarity to futher analyse the readon for churn as they might have direct impact on the churn rate.
        
chn.loc[chn.churned == 1, "start"].mean()
chn.loc[chn.churned == 0, "start"].mean()

