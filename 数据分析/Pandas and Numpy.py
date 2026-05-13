import numpy as np
import pandas as pd
from datetime import datetime


# 构造向量
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算向量运算时，每个元素都参与运算

GDP = [80855, 77388, 68024, 47251, 40471]
city = ['GD','JS','SD','ZJ','HN']

# 使用Series"序列"构造函数
info = pd.Series(GDP,index = city)

# 构建同值不同索引的Series对象
s = pd.Series(6, index = ["a", "b", "c", "d"])

# 访问Series对象的元素
print('访问Series对象的元素：')
print(info[0])# 通过位置访问
print(info['GD'])# 通过索引访问
print(info[0:3])# 通过切片访问
print(info[['GD','JS']])# 通过列表访问
print(info[(info['GD'] > 50000) & (info['JS'] > 50000)])# 通过条件访问 &表示并且 |表示或者 ~表示非
print('------------------'*3)

# 访问Series对象的属性
print('访问Series对象的属性：')
print(info.dtype)# 类型 
print(info.values)# 值
print(info.index)# 索引行


# datafreame数据框

# 构建DataFrame数据框,字典类
data= {'rank':[1, 2, 3, 4],'GDP':[80855, 77388, 68024, 47251]}
city= ['GD','JS','SD','ZJ']
df = pd.DataFrame(data, index = city)

# 构建DataFrame数据框,列表类
data = [['May',689],['Tony',659],['Kevin',635]]
df = pd.DataFrame(data, index = city, columns=['name','score'])

# 访问DataFrame对象的元素
print('访问DataFrame对象的元素：')
print(df['name'])# 通过列名访问
print(df.loc['GD'])# 通过索引访问
print(df.iloc[0])# 通过位置访问
print(df.loc['GD','name'])# 通过行列访问
print(df.iloc[0,0])# 通过行列位置访问
print(df.loc[0:2,2:4])
print(df[df['score'] > 650])# 通过条件访问
print('------------------'*3)

# DAtaFrame的轴
df.sum(axis=0)# 轴为垂直方向，求和

# 访问DataFrame对象的属性
# 可以快速改变索引行和列名 
print('访问DataFrame对象的属性：')  
print(df.dtypes)# 类型
print(df.values)# 值
print(df.index)# 索引行
print(df.columns)# 列名

# 时间类型
start = datetime(2020, 5, 1, 23, 59, 59)
end = datetime(2020, 10, 1)
timeSpan = end - start

# 转换时间字符串为时间类型
df["create_time"] = pd.to_datetime(df["create_time"])
df["pay_time"] = pd.to_datetime(df["pay_time"])

data_2018_2 = data[(data["购药时间"].dt.month == 2)] # 获取购药时间的月份
week = df["create_time"].dt.strftime("星期%u")# 获取星期几 详情见 示例文件\日期格式.png
df['create_time'] = df['create_time'].astype(float)

# 统计函数 详情见示例文件\统计函数.png   #### 计算时可以多行同时进行
print(df.mean().round()) 

# 高级字符索引
df['name'].str.contains('May')# 判断字符串是否包含某个子串
df['name'].str.startswith('M')# 判断字符串是否以某个子串开头
df['name'].str.endswith('y')# 判断字符串是否以某个子串结尾

fishpot2 = df.set_index("XXXX")# 选择一列作为索引列
tasteBest = fishpot2["口味评分"].idxmax()# idxmax()函数返回最大值所在的索引标签 idxmin()函数返回最小值所在的索引标签
fishpot3 = df.reset_index()# 重置索引，将索引列变为普通列

# 数据排序
df.sort_values(by='score', ascending=False)# 按照某列排序，ascending=False表示降序，ascending=True表示升序
df.sort_index(ascending=False)# 按照索引排序，ascending=False表示降序

# 描述函数
df.describe()# 计算数值型数据的描述统计信息，包括计数、均值、标准差、最小值、25%分位数、50%分位数、75%分位数和最大值


# 强制转化数据类型
df["score"] = df["score"].astype('category')# 将score列的数据类型转换为category类型
# 1.列非空元素的数目——count# 2.类别的数目——unique# 3.数目最多的类别——top# 4.数目最多类别的数目——freq
df["score"].value_counts()# 计算score列中每个类别的数目
# 1. float (浮点型)
# 2. int (整型)
# 3. bool (布尔型)
# 4. datetime64[ns] (日期时间)
# 5. timedelta[ns] (时间差)
# 6. category (有限长度的文本值列表)
# 7. object (文本)


# 数据分组
grouped = df.groupby(df["name"])# 按照name列分组

# 重采样
resampleData = df.resample('M').sum()# 按照create_time列进行重采样，频率为每月，求和
resampleData.index = resampleData.index.strftime('%Y年%m月')# 将索引格式化为年月格式

# 重塑多重索引
groupByCategory = data.groupby(data["category"]).resample("M").sum()

# 使用unstack()函数将groupByCategory按照"category"重新排列，使得每个类别成为一个新的列，索引仍然是月份
groupByCategory = groupByCategory.unstack("category")

# 计算每个月的总销售额
sumTurnover = groupByCategory.sum(axis=1)
# sk-2794c390daee4f77a0d9a013faae0895
# apply()函数对DataFrame的每一列或每一行应用一个函数
def getPercentage(item):
    return item / sumTurnover

# 获取各营业额占当月营业额的比例，并赋值给变量percentage
percentage = groupByCategory.apply(getPercentage)

# 合并数据集
df2019 = pd.read_csv("2019.csv")
df2020 = pd.read_csv("2020.csv")
dfYear = pd.concat([df2020, df2019],axis=0,join="outer") # join="outer"表示外连接 join="inner"表示内连接,外连接会保留所有数据，内连接会保留交集数据
dfYear = pd.merge(df2019, df2020, on="month", how="outer",left_on="month",right_on="month")# 列合并数据集 left表示左连接 right表示右连接 outer表示外连接 inner表示内连接，默认为inner

# 数据透视表
pd.pivot_table(df, index="name", columns="score", values="create_time",aggfunc="sum")

# 计算相关系数
corrMatrix = df.corr(method='pearson', min_periods=10)# 计算数值型数据的相关系数矩阵, min_periods参数表示计算相关系数时至少需要的非NA值的数量，默认为1