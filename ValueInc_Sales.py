#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:39:28 2022

@author: angieyou
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <-- format of read csv

data = pd.read_csv('transaction.csv')

#we will be using read.csv from pandas, transaction.csv is the file we'll be referring to, and ; is the separator

data = pd.read_csv('transaction.csv', sep = ';')

#summary of the data
data.info()

#working with calculations
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation 
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberOfItemsPurchased * CostPerItem

#adding new column to data frame

data['CostPerTransaction'] = CostPerTransaction

#Sales per transaction 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit per transaction
# profft = sales - cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#markup per transaction
#markup = (sales - cost)/cost

data['Markup'] = ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']

#rounding markup 

RoundMarkup = round(data['Markup'], 2) 

data['Markup'] = RoundMarkup

#combining data fields (year, month, day)

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#change column type
#change the day column to a string

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date 

#using iloc to view specific columns and rows
data.iloc[0] #views row with index of 0
data.iloc[0:3] #views first 3 rows
data.iloc[-5:] #views last 5 rows

data.iloc[:,2] #brings in all rows and column 2
data.iloc[4,2] #brings in 4th row, second column

#using split to split the client keywords field
#new_Var = column.str.split('separator' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new column for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#removing brackets from clientage and lengthofcontract using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#using lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#bringing in a new data set
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merging files 
#merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns
#df = df.drop('columnname;, axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year','Month'], axis = 1)

#export into CSV
#not including the index column
data.to_csv('ValueInc_Cleaned.csv', index = False)

















































