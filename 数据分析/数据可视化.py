import pandas as pd
import matplotlib.pyplot as plt #  https://matplotlib.org/stable/api/index.html

data = pd.read_csv("")

# Step1 设置字体，创建画布
plt.rcParams["font.sans-serif"] = "SimHei"

plt.figure(figsize=(4,3),facecolor='blue')
# figure()函数的常用参数有（均为非必选参数）：
# figsize:指定figure的宽和高，单位为英寸；
# facecolor:背景颜色
# edgecolor:边框颜色
# frameon:是否显示边框


# Step2 绘制折线图
plt.plot(data["month"],data["sum"],color="orange",marker="o",label="每月总销量")
# 将x轴标题设置为"月份"
plt.xlabel("月份")
# 将y轴标题设置为"销量"
plt.ylabel("销量")
# 将图表标题设置为"2019"
plt.title("2019年8月至2020年7月书店每月销量走势")
# 显示图例
plt.legend()
plt.show()
"""
1. 设置颜色： color参数
2. 设置折线图标记： marker参数
3. 添加并显示图例说明：label参数和plt.legend()函数
4. 添加坐标轴标题和添加图像标题：plt.xlabel()、plt.ylabel()函数和plt.title()函数
"""


# Step3 绘制柱状图
plt.bar(data["month"],data["sum"],width=0.5,color="skyblue",label="每月总销量")

plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月销量走势")
plt.legend()
plt.show()


# Step4 绘制散点图
plt.scatter(data["ads_fee"],data["sales"],color="green")
plt.xlabel("广告费用")
plt.ylabel("销量")
plt.show()


# Step5 绘制双y叠加图
plt.bar(data["month"],data["exposure"],color="skyblue",label="PV")
plt.xlabel("月份")
plt.ylabel("曝光量")

plt.legend(loc="upper left") # 修改图例位置

plt.twinx()

plt.plot(data["month"],data["CVR"],marker="o",label="CVR")
plt.ylabel("转化率")
plt.legend()
plt.show()


# Step6 簇形柱状图
data.plot.bar("month",["first_floor","second_floor","third_floor"])

plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月至2020年7月书店每月各楼层销量走势")
plt.show()

"""
data["first_floor"].plot.bar()
"""


# Step7 百分比堆积柱状图
data.plot.bar("month",["first_floor","second_floor","third_floor"],stacked=True) # stacked堆叠效果


# Step8 

plt.subplot(2,2,1)
plt.plot(data["month"],data["sum"])
# 旋转x轴的刻度至90度
plt.xticks(rotation=90)

plt.subplot(2,2,2)
plt.scatter(df["ads_fee"],df["sales"])

# 选择序号为3的子图
plt.subplot(2,2,3)
data.plot.bar("month",["first_floor","second_floor","third_floor"],ax=plt.gca())

# TODO 选择序号为4子图
plt.subplot(2,2,4)
percentData.plot.bar("month",["一楼","二楼","三楼"],stacked=True,ax=plt.gca())

# 调整子图布局
plt.tight_layout()
plt.show()