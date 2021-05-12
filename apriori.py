from operator import itemgetter
from itertools import combinations, chain


class Arules:
    def __init__(self):
        self.frequent_itemsets = list()
        self.num_of_occurrences = dict()
        self.num_of_transactions = 0


    def get_frequent_item_sets(self, transactions=None, min_support=None):
        self.num_of_transactions = len(transactions)
        req_num_of_occurrences = self.num_of_transactions * min_support
        one_itemsets_dict = dict()
        for trans_index, trans in enumerate(transactions):
            for item in trans:
                if item == '':
                    break
                one_itemsets_dict[(item,)] = one_itemsets_dict.get((item,), set())
                one_itemsets_dict[(item,)].add(trans_index)
        
        for k, v in one_itemsets_dict.copy().items():
            if len(v) < req_num_of_occurrences:
                del one_itemsets_dict[k]
            else:
                self.frequent_itemsets.append(k)
                self.num_of_occurrences[k] = len(v)
        
        list_of_last_dicts = [one_itemsets_dict]
        frequent_k_itemsets_num = len(one_itemsets_dict)
        while(frequent_k_itemsets_num > 0):
            frequent_k_itemsets_num = 0
            list_of_cur_dicts = []
            for dic in list_of_last_dicts:
                for i1, k1 in enumerate(dic.keys()):
                    starts_with_dict = dict()
                    for k2 in list(dic)[i1+1:]:
                        new_key = k1+(k2[-1],)
                        repeat_in_transactions = dic[k1].intersection(dic[k2])
                        if len(repeat_in_transactions) > req_num_of_occurrences:
                            starts_with_dict[new_key] = repeat_in_transactions
                            self.frequent_itemsets.append(new_key)
                            self.num_of_occurrences[new_key] = len(repeat_in_transactions)
                    list_of_cur_dicts.append(starts_with_dict)
                    frequent_k_itemsets_num+=len(starts_with_dict)
            list_of_last_dicts = list_of_cur_dicts
        return self.frequent_itemsets
            

    def get_arules(self, min_support=0, min_confidence=0, min_lift=0, sort_by='lift'):
        arules = []
        for itemset in self.frequent_itemsets:
            subsets = list(chain.from_iterable(combinations(itemset, r) for r in range(1, len(itemset))))
            num_of_itemset_repeat = self.num_of_occurrences[itemset]
            support = num_of_itemset_repeat / self.num_of_transactions
            if support < min_support:
                continue
            for index, left_side in enumerate(subsets, start=1):
                right_side = subsets[len(subsets) - index]
                confidence = num_of_itemset_repeat / self.num_of_occurrences[left_side]
                if confidence < min_confidence:
                    continue
                lift = confidence * self.num_of_transactions / self.num_of_occurrences[right_side]
                if lift < min_lift:
                    continue
                arules.append((left_side, right_side, eval(sort_by)))
        arules = sorted(arules, key=itemgetter(2), reverse=True)
        return arules


    # def get_arules_for_diagram(self, min_support=0, min_confidence=0, min_lift=0, sort_by='lift'):
    #     arules = []
    #     for itemset in self.frequent_itemsets:
    #         subsets = list(chain.from_iterable(combinations(itemset, r) for r in range(1, len(itemset))))
    #         num_of_itemset_repeat = self.num_of_occurrences[itemset]
    #         support = num_of_itemset_repeat / self.num_of_transactions
    #         if support < min_support:
    #             continue
    #         for index, left_side in enumerate(subsets, start=1):
    #             right_side = subsets[len(subsets) - index]
    #             confidence = num_of_itemset_repeat / self.num_of_occurrences[left_side]
    #             if confidence < min_confidence:
    #                 continue
    #             lift = confidence * self.num_of_transactions / self.num_of_occurrences[right_side]
    #             if lift < min_lift:
    #                 continue
    #             arules.append({
    #                 "lhs": left_side,
    #                 "rhs": right_side,
    #                 "count_full": num_of_itemset_repeat,
    #                 "count_lhs": self.num_of_occurrences[left_side],
    #                 "count_rhs": self.num_of_occurrences[right_side],
    #                 "num_transactions": self.num_of_transactions,
    #                 "support": support,
    #                 "confidence": confidence,
    #                 "lift": lift
    #             })
    #     arules = sorted(arules, key=lambda obj: obj[sort_by], reverse=True)
    #     return arules


    # def get_details(self, transactions=None, min_support=None, min_confidence=None):
    #     one_itemsets_dict = dict()
    #     n = list()
    #     num = len(transactions)
    #     for i, r in enumerate(transactions):
    #         s = 0
    #         for w in r:
    #             if w == '':
    #                 break
    #             one_itemsets_dict[w] = one_itemsets_dict.get(w, {"number": 0, "trans": []})
    #             one_itemsets_dict[w]['trans'].append(i)
    #             one_itemsets_dict[w]['number'] += 1
    #             # print(one_itemsets_dict[w])

    #             s+=1
    #         if s>0:
    #             n.append(s)
    #     w = num * min_support
    #     for k, v in one_itemsets_dict.copy().items():
    #         if(v['number']<w):
    #             del one_itemsets_dict[k]
    #     # print(one_itemsets_dict)
    #     return one_itemsets_dict,n