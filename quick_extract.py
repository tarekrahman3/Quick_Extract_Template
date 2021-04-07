import amazon
import pandas as pd

df = pd.read_csv('import_file.csv', header=0)
importURLS = df.links.to_list()

data = amazon.parse_amazon(importURLS)

df = pd.DataFrame (data)
print(df)
df.to_csv(r'export_data.csv', index = False, header=True)
