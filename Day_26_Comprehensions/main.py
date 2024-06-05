names = ["Alex", 'Beth', 'Caroline', 'Dave', 'Elanor', "Freddie"]
import random

score = {
    "Name" : names,
    "Marks": [random.randint(50, 100) for _ in range(len(names))]
}

import pandas

df = pandas.DataFrame(score)
print(df)

for (index, row_data) in df.iterrows():
    if row_data.Name == "Beth":
        print(row_data.Marks)