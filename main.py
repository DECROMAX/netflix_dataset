import pandas as pd

pd.set_option('display.width', 1200)
pd.set_option('display.max_columns', 29)

df = pd.read_csv('/home/ryan/PycharmProjects/netflix_dataset/netflix-rotten-tomatoes-metacritic-imdb.csv')

df['Genre'].fillna('None', inplace=True)
print(df['Genre'])
