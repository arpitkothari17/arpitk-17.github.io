import pandas as pd 

air = pd.read_excel("Pandas 2_ML dataset (airbnb).xlsx")

air.columns
air.describe()

#%% 
# A. What type of Machine Learning model is?
    # It is a supervised model where we have the historical data of the properties and also the target variable is predicted as a column "PredictedIncome" 
    # This further falls under Regession model as PredictedIncome will be continuous variable which will want to predict in the future as well even after collecting data on income over time. 

#%%
# B. Airbnb wants to call the 20 apartments with the worst income predicted to encourage them to take actions. Could you give their names and ids?
low20 = air.sort_values(by="PredictedIncome", ascending = True).head(20).loc[:,["Id","Name"]] 
    # Step 1. Sorting by "PredictedIncome" in ascending order 
    # Step 2. filter top 20 rows and only extracting columns "Id" and "Name" 
print(low20)

#%%
# C. Could you give all the info (all the variables) for the best apartment in each neighbourhood? (best apartment means apartment with the highest predicted income)
best_tot = air.sort_values(by="PredictedIncome", ascending = False).loc[air.PropertyType == "Apartment", :].drop_duplicates(subset = "Neighbourhood")
    # Step 1. Sorting by "PredictedIncome" in desending order 
    # Step 2. Extracting PropterType as Apartments and dropping all duplicate values for "Neighbourhood" to show best apartments in each Neighbourhood
print(best_tot)
# air.Neighbourhood.value_counts()

#%%
# D. Which are the zipcodes for the 5 best scored Lofts in Queens?
Queens = air.loc[air.Neighbourhood == "Queens", :]
    # Step 1. Creating a variable "Queens" which stores the results only for Queens Neighbourhood
# Queens.PropertyType.value_counts()

Queens.sort_values(by="ReviewScoresRating", ascending = 0).loc[Queens.PropertyType == "Loft", "Zipcode"].head(5)
    # Step 2. Sorting values in desending order by "ReviewScoresRating" and then extracting "PropertyType" for "Loft" 

