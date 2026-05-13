import pandas as pd

# 读取csv文件
df = pd.read_csv('示例文件\电商数据清洗.csv', encoding='utf-8', index_col= 'order_id')

# 获取数据框的基本信息
df.info()

# 查找数据框的缺失值
dfPayNull = df[df["pay_type"].isnull()]   # 也可以是单列

# 删除缺失值
df.drop(index=dfPayNull.index, inplace=True)  # inplace=True表示在原数据框上进行修改，默认为False
df.info()

# 填充缺失值
df["pay_type"].fillna("wxpay", inplace=True)  # 将pay_type列中的缺失值填充为"wxpay"

# 判断值是否存在于
df["pay_type"].isin(~ ["wxpay","alipay"])  # 判断pay_type列中的值是否存在于["wxpay","alipay"]

# 判断是否存在重复值
dfOrderDu = df[df['order_id'].duplicated()] 

