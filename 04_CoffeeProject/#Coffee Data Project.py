#Coffee Data Project

import pandas as pd
from icecream import ic

data = pd.ExcelFile("/Users/jonashapp/Documents/GitHub/MS_TF101_-001_Coffee-Project/04_CoffeeProject/Coffee Caffeine Content.xlsx")
coffee_data = pd.read_excel(data)

#Task 1: As I user I want to know which product has the most caffein per amount

#ic((type(coffee_data)))
#ic(coffee_data)
#ic(coffee_data.columns) #Gives you Header Names of Rows as a List
#ic(coffee_data.shape) #Gives ou the number of columns and rows, Like length / len()
#ic(coffee_data.tail(3)) #Gives you the last {number} columns as an output  

chain_list = (coffee_data['Chain'])

chain_list_unique = pd.unique(coffee_data['Chain']) #Filters the List of Chains to return only the names once, gives out array
#ic(chain_list_unique)

drinks_list_unique = pd.unique(coffee_data['Product'])
#ic(drinks_list_unique)

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

    new_coffee_data["Caffeine per 100 ml"]= Per100ml

    return new_coffee_data
    
new_coffee_data = execute_calculation_in_list(coffee_data)
#ic(new_coffee_data)

def print_result_task1(new_coffee_data):

    #Sort Data by highest amount per 100 ml and output Brand, Product and caffeine per 100 ml.
    new_coffee_data.loc[:, "Caffeine per 100 ml"]
    #ic(new_coffee_data.loc[:, "Caffeine per 100 ml"])

    index_highest_amount = new_coffee_data['Caffeine per 100 ml'].idxmax()

    product = coffee_data.iloc[index_highest_amount, 1]
    brand = coffee_data.iloc[index_highest_amount, 0]
    amount = coffee_data.iloc[index_highest_amount, 4]

    print("*************************")
    print("********* Task 1 ********")
    print("*************************")
    print("Question: As I user I want to know which product has the most caffein per amount. ")
    print(f"The {product} by {brand} has the highest amount of caffein per 100 ml. It contains {amount} mg per 100 ml.")
    print("*************************")

#print_result_task1(new_coffee_data)

#Task 2: As I user I want to know which chain has the most caffein (mg) per amount in ml

def calculate_caffein_average(new_coffee_data):

    # Split Dataframe using groupby() &
    # Grouping by particular dataframe column

    grouped = new_coffee_data.groupby(['Chain'])

    results = []

    for x in range(0, len(chain_list_unique)):
            
            df1 = grouped.get_group(chain_list_unique[x])
            #ic(type(df1))
            length_group_count = len(grouped.get_group(chain_list_unique[x]))
            #ic(type(length_group_count))

            caffein_sum = sum(df1['Caffeine per 100 ml'])
            caffein_average = round(caffein_sum / length_group_count, 2)

            results.append(caffein_average)
    
    #combine two lists to one with results
    combine_lists_to_df = {'Chain': chain_list_unique, 'Average_Caffeine': results} 
    final = pd.DataFrame(combine_lists_to_df)
    #ic(final)

    return final

def print_results_task2(new_coffee_data):

    results_task_two = calculate_caffein_average(new_coffee_data)
    results_task_two = results_task_two.sort_values(by=['Average_Caffeine'], ascending=False)

    #ic(results_task_two)

    print("*************************")
    print("********* Task 2 ********")
    print("*************************")
    print("Question: As I user I want to know which chain has the most caffein (mg) per serving. ")
    print(f"The chain {results_task_two.iloc[0, 0]} has the highest amount of caffein in their products. It is {results_task_two.iloc[0, 1]} mg per serving on average.")
    print("*************************")
    print("This is the full ranking:")
    print(results_task_two)
    print("*************************")

print_results_task2(new_coffee_data)


