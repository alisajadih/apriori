from pandas.core.frame import DataFrame
from apriori import Arules
import pandas as pd

MAIN_FILE_NAME = 'Project1 - groceries.csv'
TEST_FILE_NAME = 'Project1 - groceries copy.csv'
MIN_SUPPORT = 0.005
MIN_CONFIDENCE = 0.2

df:DataFrame = pd.read_csv(MAIN_FILE_NAME, header = None, squeeze = True, keep_default_na=False)
a = Arules()
res=a.get_frequent_item_sets(transactions=df.values, min_support=MIN_SUPPORT, min_confidence=MIN_CONFIDENCE)
print(res)




# print(res[-1])
# min_num = len(df.values) * MIN_SUPPORT
# for r in res:
#     num = 0
#     for v in df.values:
#         if len(set(v).intersection(set(r))) == len(r):
#             num+=1
#     print(num)


# res = a.get_details(df.values, min_support=0.005, min_confidence=0.2)
# d = res[0] # dict of objects and a object of number and trans id of occurunces
# n = res[1] # list of number of elements for each transaction
# # print(n)
# print(f"number of transactions are: {len(df.values)}")
# print(f"number of distinct objects are: {len(d)}")
# print(f"number of all objects are: {sum(obj['number'] for obj in d.values())}")
# print(f"max number of transactions that an object occurs: {max(len(obj['trans']) for obj in d.values())}")
# print(f"sum of binary search cost for finding an object in transactions: {sum(np.log(n))}")


# df:DataFrame = pd.read_csv('Project1 - groceries.csv', header=None, keep_default_na=False)
# r = df.shape[0]
# print(df.values)
# all = df.to_records(col)
# print(all[0])
# print(df[:][:1])
# print(df.unique())
# k1 = []
# for i in range(1,10):
#     print(df[:][[i]])
    # print(df[:][:1])
    # k1 += list(df[col].unique())
# print(len(k1))
# print(df.count())
# for a in df.head():
#     print(a)
# print(df.head())
# print(df)