#Coffee Data Project

import pandas as pd
from icecream import ic

data = pd.ExcelFile("/Users/jonashapp/Documents/GitHub/MS_TF101_-001_Coffee-Project/04_CoffeeProject/Coffee Caffeine Content.xlsx")
coffee_data = pd.read_excel(data)

#As I user I want to know which chain has the most caffein (mg) per amount in ml

#ic((type(coffee_data)))
ic(coffee_data)

#As I user I want to know which product has the most caffein per amount

ic(coffee_data.columns) #Gives you Header Names of Rows as a List
ic(coffee_data.shape) #Gives ou the number of columns and rows, Like length / len()

#ic(coffee_data.tail(3)) #Gives you the last {number} columns as an output  

chain_list = (coffee_data['Chain'])
#ic(chain_list)

chain_list_unique = pd.unique(coffee_data['Chain']) #Filters the List of Chains to return only the names once, gives out array

ic(chain_list_unique)


drinks_list_unique = pd.unique(coffee_data['Product'])
ic(drinks_list_unique)

def calc_caffeine_per_ammount(caffeine_mg, drink_size):

    #should return ammount caffeine in mg per 100 ml

    caffeine_per_ammount = caffeine_mg / drink_size * 100
    caffeine_per_ammount = round(caffeine_per_ammount, 2)

    return caffeine_per_ammount

def execute_calculation_in_list(coffee_data): #imports old list

    column_count = len(coffee_data['Chain'])  #Gets number of items in DataFramew without header
    
    Per100ml = []
    new_coffee_data = coffee_data

    for x in range(0, column_count): #Starts at 1, not header

        caffeine_mg = coffee_data.iloc[x, 2]
        drink_size = coffee_data.iloc[x, 3]
        
        #ic(caffeine_mg)
        #ic(drink_size)

        caffein_per_ammount = calc_caffeine_per_ammount(caffeine_mg, drink_size) #100 proxy
        
        Per100ml.append(caffein_per_ammount)

    new_coffee_data = pd.DataFrame(coffee_data, columns = ['Chain', 'Caffeine (mg)', 'Drink size (ml)'])
    new_coffee_data["Caffeine per 100 ml"]= Per100ml

    return new_coffee_data


    #Should execute calculation for every drink in list and return a new list with column Caffeine_Ammount
    
new_coffee_data = execute_calculation_in_list(coffee_data)
ic(new_coffee_data)
