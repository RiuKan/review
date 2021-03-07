import json
with open("review.txt","r") as f:
    logs = json.load(f)

with open("review.txt","w") as f:
    for z in logs["목록"]:
        for i in logs[z].keys():
            logs[z]["log"] = {i:[0,None]}
    
    json.dump(logs,f)
