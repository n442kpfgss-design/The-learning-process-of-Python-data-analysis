from apyori import apriori
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'示例文件\用户浏览数据.csv')

articles = []
for i in data['文章类型']:
    i = i.split(',')
    articles.append(i)

rules = apriori(articles, min_support=0.1, min_confidence=0.6)

extract_result = []
for rule in rules:
    support = round(rule.support,3) # 支持度
    for i in rule.ordered_statistics:
        head_set = list(i.items_base) # 规则的前件，即条件部分
        tail_set = list(i.items_add) # 规则的后件，即结论部分
        
        if head_set ==[]:
            continue
        related_category = str(head_set) + '->' + str(tail_set) # 关联类别
        confidence = round(i.confidence,3) # 置信度
        lift = round(i.lift,3) # 提升度
        
        extract_result.append([related_category,support,confidence,lift])

rule_data = pd.DataFrame(extract_result, columns=['关联规则','支持度','置信度','提升度'])        
promoted_rules = rule_data[rule_data['提升度'] > 1] # 提升度大于1的规则
restricted_rules = rule_data[rule_data['提升度'] < 1] # 提升度小于1的规则

promoted_rules.plot.bar('关联规则',['支持度','置信度'],rot=0)
plt.title('促进关系的强关联规则')

plt.show()