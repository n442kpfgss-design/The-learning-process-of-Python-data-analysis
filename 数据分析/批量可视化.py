import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 1. 读取订单表并合并
data1 = pd.read_csv('示例文件/2019年下半年订单表.csv')
data2 = pd.read_csv('示例文件/2020年上半年订单表.csv')
order_data = pd.concat([data1, data2])

# 2. 转换下单时间为时间类型并设为索引
order_data['下单时间'] = pd.to_datetime(order_data['下单时间'])
order_data = order_data.set_index('下单时间')

# 3. 按商品ID分组，按月采样，统计数量和，重置索引
monthly_orders = order_data.groupby('商品ID')['数量'].resample('M').sum().reset_index()
monthly_orders['下单时间'] = monthly_orders['下单时间'].dt.strftime('%Y-%m')

# 4. 读取浏览数据表
exposure = pd.read_csv('示例文件/Exposure.csv')

# 5. 合并数据
merged = pd.merge(
    exposure,
    monthly_orders,
    left_on=['ID', 'Month'],
    right_on=['商品ID', '下单时间'],
    how='left'
)

# 6. 计算购买转化率
merged['购买转化率'] = (merged['数量'] / merged['Exposure']).round(2)
# 若数量为NaN，转化率也为NaN

# 7. 按商品ID分组计数，获取index
id_counts = merged.groupby('ID').size()
id_list = id_counts.index.tolist()

# 8. 可视化
matplotlib.rcParams['font.sans-serif'] = ['Arial Unicode MS']
fig, axes = plt.subplots(len(id_list), 1, figsize=(10, 4 * len(id_list)), sharex=True)

if len(id_list) == 1:
    axes = [axes]  # 保证axes可迭代

for i, id_ in enumerate(id_list):
    ax = axes[i]
    data = merged[merged['ID'] == id_]
    ax.plot(
        data['Month'],
        data['购买转化率'],
        marker='o',
        label='转化率'
    )
    ax.set_xticklabels(data['Month'], rotation=90)
    ax.set_ylim(0, 0.3)
    ax.legend(loc='best')
    ax.set_title(f'商品ID: {id_}')
    ax.set_ylabel('购买转化率')
    ax.set_xlabel('Month')

plt.tight_layout()
plt.show()