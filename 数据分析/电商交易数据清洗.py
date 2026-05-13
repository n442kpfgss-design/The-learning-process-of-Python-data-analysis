
import pandas as pd
import numpy as np

# 读取数据，id作为index
data = pd.read_csv("./示例文件/180101-190630交易数据.csv", index_col='id')

# 1. order_id：去除<=0和重复值
if 'order_id' in data.columns:
	data = data[data['order_id'] > 0]
	data = data[~data['order_id'].duplicated()]

# 2. user_id：去除<=0
if 'user_id' in data.columns:
	data = data[data['user_id'] > 0]


# 3. payment、price、cutdown_price、post_fee：去除<0，全部转为元（直接/100）
for col in ['payment', 'price', 'cutdown_price', 'post_fee']:
	if col in data.columns:
		data = data[data[col] >= 0]
		data[col] = data[col] / 100

# 4. items_count：去除<0
if 'items_count' in data.columns:
	data = data[data['items_count'] >= 0]

# 5. create_time、pay_time：转为时间格式，去除create_time>pay_time
for col in ['create_time', 'pay_time']:
	if col in data.columns:
		data[col] = pd.to_datetime(data[col], errors='coerce')
if 'create_time' in data.columns and 'pay_time' in data.columns:
	data = data[data['create_time'] <= data['pay_time']]

# 6. 去除重复行
data = data.drop_duplicates()

# 7. 只输出info
data.info()