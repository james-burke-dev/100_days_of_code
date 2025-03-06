import pandas as pd

data = pd.read_csv("weather_data.csv")

temps = data["temp"].to_list()

avg_temp = data["temp"].mean()
max_temp = data["temp"].max()
min_temp = data["temp"].min()


print(data[data.temp == max_temp] )

monday = data[data.day == "Monday"]
monday_temp_in_F = monday.temp[0] * 9/5 + 32