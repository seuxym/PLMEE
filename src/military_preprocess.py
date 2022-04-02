import json
from typing import Dict


def index2int(obj):

    if type(obj) == dict:
        res = {}
        for k, v in obj.items():
            if k.endswith("index"):
                assert type(v)==str
                res[k]=int(v)
            else:
                res[k]=index2int(v)
        return res
    if type(obj)==list:
        res=[]
        for e in obj:
            res.append(index2int(e))
        return res
    return obj

if __name__=='__main__':
    f = open("data/military/all_data.jsonl","r")
    js=[]
    for line in f:
        try:
            js.append(json.loads(line))
        except:
            pass
    res=[]
    for j in js:
        res.append(index2int(j))
    f.close()
    f = open("data/military/all_data_processed.jsonl","w")
    for j in res:
        f.write(json.dumps(j,ensure_ascii=False)+"\n")
    f.close()

