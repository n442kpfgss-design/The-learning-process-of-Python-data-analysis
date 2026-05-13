import matplotlib.pyplot as plt
import pandas as pd 


data = pd.read_csv("示例文件\书店每月销量数据.csv")
df = pd.read_csv("示例文件\书店图书销量和广告费用.csv")

# 设置中文字体
plt.rcParams['font.sans-serif'] = 'SimHei'

# 创建画布
plt.figure(figsize=(4,3),facecolor="blue")

# 绘制折线图
plt.plot(data["month"],data["sum"],color="orange",marker="o",label="月销售额")
plt.xlabel("月份")# x轴标签
plt.ylabel("销售额")# y轴标签
plt.title("销售额")# 图表标题
plt.xticks(rotation=45)# x轴标签旋转45度
# 展示图例
plt.legend()
# 展示画布
plt.show()

# 绘制柱状图
plt.bar(data["month"],data["sum"],width=0.6,color="orange")

# 绘制散点图
plt.scatter(data["ads_fee"],data["sales"],color="green")
plt.xlabel("广告费用")# x轴标签
plt.ylabel("销售额")# y轴标签
plt.legend(loc="upper left")# 图例位置

# 双Y叠加图
plt.twinx()
plt.plot(data["month"],data["ads_fee"],color="red",marker="o",label="月广告费用")

# 簇形柱状图
ax = data.plot.bar("month",["first_floor","second_floor","third_floor"])
data["first_floor"].plot.bar()
ax.set_xlabel("月份")# x轴标签
ax.set_ylabel("销售额")# y轴标签



# 百分比堆积柱状图
data.plot.bar("month",["first_floor","second_floor","third_floor"],stacked=True)



# 并列子图
plt.subplot(2,2,1)
plt.plot(data["month"],data["sum"])
21
plt.xticks(rotation=90) # x轴标签旋转90度

# 选择序号为2子图
plt.subplot(2,2,2)

plt.scatter(df["ads_fee"],df["sales"])

# 选择序号为3的子图
plt.subplot(2,2,3)
# 在子图上使用pandas的plot方法绘制柱状图
data.plot.bar("month",["first_floor","second_floor","third_floor"],stacked=True,ax=plt.gca())

# 选择序号为4子图
plt.subplot(2,2,4)

plt.tight_layout() # 调整子图间距

# 绘制直方图
plt.hist(data["sum"],bins=5)
