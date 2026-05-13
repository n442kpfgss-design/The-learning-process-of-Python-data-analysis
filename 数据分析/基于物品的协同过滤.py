import pandas as pd

data = pd.read_csv(r'示例文件\Beauty_products.csv')


data1 = data.pivot_table(index='UserId', columns='ProductId', values='Rating')
data_corr = data1.corr(method='pearson')
list_id = []
for i in data1.index.values:
    user = data1.loc[i].dropna()
    name = user.index
    score = user.values

    smis = data_corr[name].drop(name) # 
    prod = smis * score 

    list_prod = prod.sum(axis=1)
    list_prod = list_prod.sort_values(ascending=False)

    list_id.append(list_prod.index.values[0:5])
dict_prod = {'用户ID':data1.index.values, '推荐列表':list_id}
data_frame = pd.DataFrame(dict_prod)
print(data_frame)