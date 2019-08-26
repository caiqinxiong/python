dic1 = {'k1':'v1'}
dic2 = {'k2':'v2'}
import json
import pickle
# with open('file','w') as f:
#     # '{"k1": "v1"}' + '\n'
#     json.dump(dic1,f)
#     json.dump(dic2,f)

# with open('file','rb') as f:
#     ret1 = pickle.load(f)
#     ret2 = pickle.load(f)
#     print(ret1)
#     print(ret2)

with open('file','w') as f:
    ret = json.dumps(dic1)
    f.write(ret+'\n')
    ret = json.dumps(dic2)
    f.write(ret + '\n')

with open('file','r') as f:
    for line in f:
        line = line.strip()
        if line:
            dic = json.loads(line)
            print(dic)