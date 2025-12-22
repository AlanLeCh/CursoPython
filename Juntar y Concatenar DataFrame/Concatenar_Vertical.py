
import pandas as pd

df1 = pd.DataFrame({'id':['A','B','C','D'],
                    'age': [30,23,25,22]})

df2 = pd.DataFrame({'id':['E','F','G','F'],
                    'age': [40,21,19,24]})

print(df1)
print(df2)

Concatenación = pd.concat([df1, df2],ignore_index=True)

print(Concatenación)

