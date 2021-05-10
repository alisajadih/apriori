class Arules:
    def __init__(self):
        pass

    def get_frequent_item_sets(self, transactions=None, min_support=None, min_confidence=None):
        ans = []
        d = dict()
        min_num = len(transactions) * min_support
        for trans_index, trans in enumerate(transactions):
            for item in trans:
                if item == '':
                    break
                d[(item,)] = d.get((item,), set())
                d[(item,)].add(trans_index)
        
        for k, v in d.copy().items():
            if len(v) < min_num:
                del d[k]
            else:
                ans.append(k)
        
        list_of_last_dicts = [d]
        num = len(d)
        while(num > 0):
            num = 0
            list_of_cur_dicts = []
            for dic in list_of_last_dicts:
                for i1, k1 in enumerate(dic.keys()):
                    dd = dict()
                    for k2 in list(dic)[i1+1:]:
                        new_key = k1+(k2[-1],)
                        rep_trans = dic[k1].intersection(dic[k2])
                        if len(rep_trans) > min_num:
                            dd[new_key] = rep_trans
                            ans.append(new_key)
                    list_of_cur_dicts.append(dd)
                    num+=len(dd)
            list_of_last_dicts = list_of_cur_dicts
        return ans
            

    def get_arules(self, min_support=None, min_confidence=None, min_lift=None, sort_by='lift'):
        pass
    # sort_by: lift , confidence, support


    # def get_details(self, transactions=None, min_support=None, min_confidence=None):
    #     d = dict()
    #     n = list()
    #     num = len(transactions)
    #     for i, r in enumerate(transactions):
    #         s = 0
    #         for w in r:
    #             if w == '':
    #                 break
    #             d[w] = d.get(w, {"number": 0, "trans": []})
    #             d[w]['trans'].append(i)
    #             d[w]['number'] += 1
    #             # print(d[w])

    #             s+=1
    #         if s>0:
    #             n.append(s)
    #     w = num * min_support
    #     for k, v in d.copy().items():
    #         if(v['number']<w):
    #             del d[k]
    #     # print(d)
    #     return d,n