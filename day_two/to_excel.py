import csv
import pandas as pd

bathing = pd.read_csv('balneabilidade.csv')

bathing.to_excel('balneabilidade.xlsx', sheet_name='balneabilidade')
