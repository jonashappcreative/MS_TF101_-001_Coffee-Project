#Coffee Data Project

import pandas as pd
from icecream import ic

xlsx = pd.ExcelFile("/Users/jonashapp/Documents/GitHub/MS_TF101_-001_Coffee-Project/04_CoffeeProject/Coffee Caffeine Content.xlsx")
df = pd.read_excel(xlsx)

#As I user I want to know which chain has the most caffein (mg) per amount in ml
#As I user I want to know which product has the most caffein per amount

ic((type(df)))
ic(df)
