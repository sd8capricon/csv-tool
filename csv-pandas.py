import pandas as pd

df = pd.read_csv('hw_25000.csv')

print(df["Height(Inches)"].mean())
