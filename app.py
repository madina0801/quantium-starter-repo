import pandas as pd

data_files = ["./data/daily_sales_data_0.csv", "./data/daily_sales_data_1.csv", "./data/daily_sales_data_2.csv"]

data_mapper = map(lambda filename: pd.read_csv(filename, index_col=None, header=0), data_files)
li = list(data_mapper)
data = pd.concat(li, axis=0)
# data = pd.read_csv("./data/daily_sales_data_0.csv")

data.drop(data[data['product'] != "pink morsel"].index, inplace = True)

data['sales'] = data['quantity'].astype(str) + data['price']
data.drop(data.columns[[0, 1, 2]], axis=1, inplace=True)

data.to_csv('pink_morsel_data.csv', index=False)
print(data)