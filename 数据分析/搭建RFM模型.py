# RFM模型的三个重要指标分别是：
# R：最近一次消费时间间隔
# F：消费频率
# M：消费金额
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv(r'示例文件\user_info.csv')

df['last_order_date'] = pd.to_datetime(df['last_order_date'])
endTime = datetime(2019,4,1)

df['time_gap'] = endTime -df['last_order_date']
df['time_gap'] = df['time_gap'].dt.days

# 分箱
df['R'] = pd.cut(df['time_gap'],[0,50,100,200,300,365]) # 按数值区间划分R指标
df['R'] = pd.qcut(df['time_gap'],5,labels=[5,4,3,2,1]) # 按分位数划分R指标
df['F'] = pd.qcut(df['order_count'],5,labels=[1,2,3,4,5]) 
df['M'] = pd.qcut(df['total_amount'],5,labels=[1,2,3,4,5])

def rfmTrans(x):
    if x >3:
        return 1
    else:        
        return 0
    
df['R'] = df['R'].apply(rfmTrans)
df['F'] = df['F'].apply(rfmTrans)
df['M'] = df['M'].apply(rfmTrans)

df['mark'] = df["R"].astype(str) + df["F"].astype(str) + df["M"].astype(str)

def rfmType(x):
    if x=="111":
        return "高价值用户"
    elif x=="101":
        return "重点发展用户"
    elif x=="011":
        return "重点唤回用户"
    elif x=="001":
        return "重点潜力用户"
    elif x=="110":
        return "一般潜力用户"
    elif x=="100":
        return "一般发展用户"
    elif x=="010":
        return "一般维系用户"
    else:
        return "低价值用户"

df['customer_type'] = df['mark'].apply(rfmType)
df_type = df['customer_type'].groupby(df["customer_type"]).count()
df_perc = df_type/ 51394

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.bar(df_type.index,df_type.values,color='skyblue')

plt.xlabel('客户类型')
plt.ylabel('客户数量')
plt.title('客户类型分布')
plt.twinx()
plt.plot(df_perc.index,df_perc.values,color='red',marker='o',label='客户占比')
plt.ylabel('客户占比')
plt.show()