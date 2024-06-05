import pandas

squirrel_data = pandas.read_csv('Day_25_Data_Handling/Squirrel_Data.csv')

Gray_Count = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])
Cinnamon_Count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
Black_Count = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

count = [Gray_Count, Cinnamon_Count, Black_Count]
data = {
    "Color":["Gray", "Cinnamon", "Black"],
    "Count": count
}

df = pandas.DataFrame(data)
df.to_csv("Day_25_Data_Handling/Data.csv")
