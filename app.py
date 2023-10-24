import pandas as pd

data_files = ["./data/daily_sales_data_0.csv", "./data/daily_sales_data_1.csv", "./data/daily_sales_data_2.csv"]

data_mapper = map(lambda filename: pd.read_csv(filename, index_col=None, header=0), data_files)
li = list(data_mapper)
data = pd.concat(li, axis=0)

for index, row in data.iterrows():
	pass
    # if row["product"] != "pink morsel":
    #     data.drop(index)
        
print(data)