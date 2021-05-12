from pandas.core.frame import DataFrame
from apriori import Arules
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from PyARMViz.Rule import generate_rule_from_dict
import PyARMViz
import squarify

MAIN_FILE_NAME = 'Project1 - groceries.csv'
TEST_FILE_NAME = 'Project1 - groceries copy.csv'
# MIN_SUPPORT = 0.055
MIN_SUPPORT = 0.005
MIN_CONFIDENCE = 0.2
# MIN_CONFIDENCE = 0.4
# MIN_LIFT = 

df:DataFrame = pd.read_csv(MAIN_FILE_NAME, header = None, squeeze = True, keep_default_na=False)
a = Arules()
a.get_frequent_item_sets(transactions=df.values, min_support=MIN_SUPPORT)
print(f'number of frequent itemstes: {len(a.frequent_itemsets)}')
arules = a.get_arules(min_confidence=MIN_CONFIDENCE)
print(f'number of association rules: {len(arules)}\n')
for rule in arules:
    print('{%s -> %s, %s}' % rule)
    # qq = (rule[0], rule[1], rule[4])
# print(arules)
# arules = [[1,2,3,4,5],(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5),(1,2,3,4,5)]
# plt.scatter(['ali', 'arman','ghasemi','mohseni','reza','aghareza'],[a[2] for a in arules] ,alpha=0.5)

# scatter
# plt.scatter([r['support'] for r in arules],[r['confidence'] for r in arules] ,alpha=0.5)
# plt.xlabel('support')
# plt.ylabel('confidence')
# plt.title('Support vs Confidence')
# plt.show()


# parallel diagrams
# rules = []
# for rd in arules: 
#     rules.append(generate_rule_from_dict(rd))
# print(len(rules))
# PyARMViz.generate_parallel_category_plot(rules)
# PyARMViz.generate_rule_graph_plotly(rules)
# PyARMViz.generate_rule_strength_plot(rules)


# item = {"Count": [], "Item": []}
# # print(sorted(a.num_of_occurrences.items(), reverse=True, key=lambda item: item[1])[:50])
# for el in sorted(a.num_of_occurrences.items(), reverse=True, key=lambda item: item[1])[:50]:
#     if len(el[0]) ==1:
#         item["Item"].append(el[0][0])
#         item["Count"].append(el[1])
# fig, ax = plt.subplots()
# cmap = matplotlib.cm.coolwarm
# mini = min(item["Count"])
# maxi = max(item["Count"])

# norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
# colors = [cmap(norm(value)) for value in item["Count"]]
# # print(colors)
# squarify.plot(sizes=item["Count"], label=item["Item"], alpha=0.8, color=colors)
# plt.axis('off')
# plt.title("Top 50 Frequent Basket Items", fontsize=15)
# plt.show()
# ttl = ax.title
# ttl.set_position([.5, 1.05])




































######################### Test that our code is true #########################
# num = 0
# t_num = len(df.values)
# for rule in arules:
#     num1=0
#     num2=0
#     num3=0

#     for t in df.values:
#         # print(set(rule[0]), set(rule[1]), set(t))
#         t1=False
#         t2=False
#         if len(set(rule[0]).intersection(set(t))) == len(rule[0]):
#             t1 = True
#             num1+=1
#         if len(set(rule[1]).intersection(set(t))) == len(rule[1]):
#             num2+=1
#             t2 = True
#         if t1 and t2:
#             num3+=1
#     # print(num1, num2, num3)
#     sup1 = num1/t_num
#     sup2 = num2/t_num
#     # print(num1,num2)
#     sup = num3/t_num
#     conf = num3/num1
#     lift = conf*t_num/num2
#     if sup >= MIN_SUPPORT and conf >= MIN_CONFIDENCE:
#         num+=1
#     print(lift, rule[2])
    
# print(num)
