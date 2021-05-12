from pandas.core.frame import DataFrame
from apriori import Arules
import pandas as pd

MAIN_FILE_NAME = 'Project1 - groceries.csv'
TEST_FILE_NAME = 'Project1 - groceries copy.csv'
MIN_SUPPORT = 0.005
MIN_CONFIDENCE = 0.2
# MIN_LIFT = 

df:DataFrame = pd.read_csv(MAIN_FILE_NAME, header = None, squeeze = True, keep_default_na=False)
a = Arules()
a.get_frequent_item_sets(transactions=df.values, min_support=MIN_SUPPORT)
print(f'number of frequent itemstes: {len(a.frequent_itemsets)}')
arules = a.get_arules(min_confidence=MIN_CONFIDENCE)
print(f'number of association rules: {len(arules)}\n')
for rule in arules:
    print('%s -> %s\t\t\t:::::::\t%s' % rule)


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
