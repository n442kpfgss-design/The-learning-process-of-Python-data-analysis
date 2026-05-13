import pandas as pd
#1.读取文件

#读取数据集，将结果赋值给变量data
data = pd.read_csv("示例文件\BookRates.csv")
#2.构建数据透视表
#使用pivot_table()函数创建数据透视表
#设置行索引lindex为"ISBN"，列索引lcolumns为"user_id"，值values为"rating"
#并赋值给变量userRatings

userRatings = data.pivot_table(index = "ISBN", columns = "user_id",values = "rating")
#3.计算用户间的相关系数
#使用corr()函数，计算userRatings的皮尔逊相关系数

# 传入参数method="pearson"',min_periods=5
#将结果赋值给变量corrMatrix
corrMatrix = userRatings.corr(method="pearson", min_periods=5)
#4.找出与用户638最相似的用户
#获取「用户638」与其他用户之间的皮尔逊相关系数，并赋值给userCorrusercorr = corrMatrix[638].drop(index=638)
usercorr = corrMatrix[638].drop(index=638)
#获取最大值对应的索引，并赋值给变量mostCorrUser
mostCorrUser = usercorr.idxmax()
#5.挑选可推荐书籍

#5.1获取相似用户评分过的书籍信息，赋值给targetBook
targetBook = userRatings [mostCorrUser]
#5.2获取相似用户评分在8分以上的书籍
targetBook = targetBook[targetBook.values>8]
#5.3获取目标用户评分过的书籍数据
userlRatings = userRatings[638].dropna()
#5.4删除目标用户看过的书籍
#获取相似用户评分在8分以上的书籍名称，并赋值给targetName
targetName = targetBook.index

#获取目标用户评分过的书籍名称，并赋值给user1Name
userlName = userlRatings.index
#筛选「用户1」未评分过的书籍名称，并赋值给bookList
bookList = targetName[~targetName.isin(userlName)]

#获取可推荐书籍的名称
bookList = bookList.values
# 输出bookList
print(bookList)