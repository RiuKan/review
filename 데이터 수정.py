import json
import os
import time
import copy

with open("review.txt","r") as f:
    logs = json.load(f)

##while True:
##    os.system("cls")
##    a = input("과목,날짜(3.1),범위(-) : ")
##    a = a.split(",")
##    b = a[2].split("-")
##    try:
##        logs[a[0]][a[1]].append(b)
##    except KeyError:
##        logs[a[0]][a[1]] = b
### with open 안에서 위 코드 넣으면 왜 날라가는거임?
##    with open("review.txt","w") as f:
##        json.dump(logs,f)
##    print("수정 완료")
##    time.sleep(0.2)    
    
