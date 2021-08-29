#!/usr/bin/python3
from etherscan.contracts import Contract
import json,os,sys

api = Contract(address=sys.argv[1], api_key=os.environ.get("ETHERSCAN_API_KEY"))
call = api.get_sourcecode()

def write(content,file):
    file_path = os.path.join(os.getcwd(),file)
    file_dir = file_path.rsplit('/',1)[0]
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(file_path,'w+') as f:
        f.write(content)
    f.close()

for each in call:
    for i,j in each.items():
        jj = json.loads(j[1:-1])
        for filename,code in jj['sources'].items():
            print(filename)
            content = code['content']
            write(content,filename)
        break
