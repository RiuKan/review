import json
input("데이터를 수정합니다 작업 전 백업 해놓으세요.")
with open("review.txt","r") as f:
    logs = json.load(f)
logs["빅데이터"]["3.17"] = [["41","51"]]
# with open 안에서 위 코드 넣으면 왜 날라가는거임?
with open("review.txt","w") as f:
    json.dump(logs,f)
