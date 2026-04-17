import pandas as pd

df = pd.read_csv('users.csv')

resultado = (df[df['pais'] == 'Germany'][['nombre', 'pais', 'edad']]
             .sort_values(by='edad', ascending=False)
             .head(5))

print(resultado)