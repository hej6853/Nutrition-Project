import pandas as pd
import numpy as np
import datetime

file = 'Nutrition.csv'
Nutrition = pd.read_csv(file)
print(Nutrition)

#Create a New DF to put the aggregated data
sum_nutrition= Nutrition.groupby('Date').agg('sum')

#variable
print(sum_nutrition)

#convert index to column
sum_nutrition_convert=sum_nutrition.reset_index()
print(sum_nutrition_convert)

sum_nutrition_convert['Date'] = pd.to_datetime(sum_nutrition_convert['Date'], format='%m/%d/%Y')
sum_nutrition_convert=sum_nutrition_convert.sort_values(by='Date')
print(sum_nutrition_convert)

sum_nutrition_convert.to_csv('Aggregated data.csv', index = False)