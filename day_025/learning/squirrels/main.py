import pandas as pd 

data = pd.read_csv("Squirrel_Data.csv")

squirrel_colour_count = data["Primary Fur Color"].value_counts()

