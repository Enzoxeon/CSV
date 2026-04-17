import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

df2 = df[['math score']].sort_values(by='math score', ascending=False)

print(df2.head(15))