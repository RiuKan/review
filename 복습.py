import time, json
import random
import re
# 이전 구현, 디자인, collocation 시험 구현
# 함수나 변수로 수정 필요한 것 혹은 중복되는 것 빼서 코드 정리 (수정이 쉬움)
# 복습 여부 기록 (+ 알고 모르는 것 기록해서 따로 관리)

def save(logs):
    with open("review.txt","w") as f:
            json.dump(logs,f)
now = None

with open("review.txt") as f:
    if not f.readlines():
        logs = {"목록":["영어"],"영어":{}}
    else:
        f.seek(0)
        logs = json.load(f)
def start():
    while True:
        intro = input(f"""복습 프로그램 입니다.

(a.추가 d.삭제)



{" ".join([f'{i+1}'+'.'+x for i,x in enumerate(logs["목록"])])}


어떤 것을 복습하시겠습니까? """)

        if intro == "a" or intro == "A":
            new = input("""


                         추가할 과목을 적어주세요 """)
            logs["목록"].append(new)
            logs[new] = {}
            save(logs)
        elif intro == "d" or intro == "D":
            while True:
                try:
                    delete = int(input(f"""

                    {" ".join([f'{i+1}'+'.'+x for i,x in enumerate(logs["목록"])])}

                    삭제할 과목 번호를 적어주세요 """))
                    if delete > 1 and delete <= len(logs["목록"]):
                        del logs[logs["목록"][delete-1]]
                        logs["목록"] = logs["목록"][:delete-1]+logs["목록"][delete:]
                        save(logs)
                        break
                    elif delete == 1:
                        print("영어는 삭제할 수 없습니다.")
                        time.sleep(0.2)
                    else:
                        print("삭제할 과목이 없습니다.")
                        time.sleep(0.2)
                    
                except ValueError:
                    print("숫자를 적어주세요")
        
        else:
            try:
                intro = int(intro)
                if len(logs["목록"])>0 and intro > 0 and len(logs["목록"])>=intro:
                    return intro
                else:
                    print("목록에 없습니다.")
            except ValueError:
                
                print("잘못 입력하셨습니다")
                
def word():
    while True:
        try:
            word_menu = int(input("영어 복습 입니다.\n\n1. 복습하기  2. 추가하기 3.오늘 기록보기 4.전체 기록보기 "))
            n = time.time()
            l = time.localtime
            if word_menu == 1:
                
                review_list = [86400, 86400*4, 86400*7, 86400*14, 86400*30]
                
                word_list = []
                for i in review_list:
                    try:
                        for i in logs["영어"][f"{l(n-i)[1]}.{l(n-i)[2]}"]:
                            
                            word_list.append(i) 
                    except KeyError:
                        pass
                if word_list:
                    print("복습을 시작합니다.\n\n 복습은 랜덤하게 제공됩니다.")
                    while word_list:
                        eng_kor_choice = random.randrange(0,2)
                        word_choiced = random.choice(word_list)
                        input(word_choiced[eng_kor_choice])
                        input(word_choiced[eng_kor_choice == 0])
                        del word_list[word_list.index(word_choiced)]
                else:
                    print("복습할 것이 없습니다.")
            elif word_menu == 2:
                
                eng_add = input("추가할 영문을 입력하세요 ")
                kor_add = input("그 뜻을 입력하세요 ")
                try:
                    logs["영어"][f"{l()[1]}.{l()[2]}"].append([eng_add,kor_add])
                except KeyError:
                    logs["영어"][f"{l()[1]}.{l()[2]}"] =[[eng_add,kor_add]]
                save(logs)
            elif word_menu == 3:
                try:
                    print("\n\n".join([" ".join(i) for i in logs["영어"][f"{l()[1]}.{l()[2]}"]]))
                except:
                    print("오늘 기록이 없습니다.")
            elif word_menu == 4:
                entire_menu = input("1. 검색 2. 날짜별 보기 b. 이전 ")
                if entire_menu == "1":
                    search = input("찾고자 하는 영어 혹은 한글을 적으세요. ")
                    for i in logs["영어"].keys():
                        for z in logs["영어"][i]:
                            if search in z[0] or search in z[1]:
                                print("\n"+"\t".join(z))
                    print("\n\n모두 찾았습니다")
                    input("\n돌아가시려면 아무 키나 입력하십시오")
                    
                elif entire_menu == "2":
                    
                    t = 0
                    sort_keys = sorted(list(logs["영어"].keys()))
                    all_list = [f"{i} ({len(logs['영어'][i])})" for i in sort_keys]
                    if all_list:
                        length = len(all_list)
                        while t<length:
                            
                                
                                print("\t".join(all_list[t:t+3]))
                                t += 3
                        while True:
                            date = input("해당 날짜를 입력하세요. ")
                            try:
                                print("\n".join([" ".join(i) for i in logs["영어"][date]]))
                                input("메뉴로 돌아가려면 아무키나 입력하십시오.")
                                break
                    
                            except KeyError:
                                print("존재하지 않는 날짜입니다.")
                            
                                
                                
                        
                    else:
                         print("기록이 없습니다")
                elif entire_menu == "b":
                    pass
                else:
                    print("잘못 입력하셨습니다")
                    

                
                    
                    
                
        
        except ValueError:
            print("숫자를 입력해주세요")
    

##def collocation():
def anything(menu):
    title = logs['목록'][menu-1]
    while True:
        try:
            word_menu = int(input(f"{title} 복습 입니다.\n\n1. 복습하기  2. 추가하기 3.오늘 기록보기 4.전체 기록보기 "))
            n = time.time()
            l = time.localtime
            if word_menu == 1:
                
                review_list = [86400, 86400*4, 86400*7, 86400*14, 86400*30]
                
                word_list = []
                for i in review_list:
                    try:
                        for i in logs[title][f"{l(n-i)[1]}.{l(n-i)[2]}"]:
                            
                            word_list.append(i) 
                    except KeyError:
                        pass
                if word_list:
                    print("복습할 진도들입니다.")
                    while word_list:
                        eng_kor_choice = random.randrange(0,2)
                        word_choiced = random.choice(word_list)
                        input(word_choiced[eng_kor_choice])
                        input(word_choiced[eng_kor_choice == 0])
                        del word_list[word_list.index(word_choiced)]
                else:
                    print("복습할 것이 없습니다.")
            elif word_menu == 2:
                                
                today_range = input("추가할 진도를 입력하세요 (ex) 124, 124-200, 124~300 ... ")
                numbers = re.findall("\d+",today_range)
                if not numbers:
                    print("입력되지 않았습니다.")
                elif len(numbers) > 2:
                    print("한 장이나 둘 사이의 범위를 입력해주세요")
                elif len(numbers) == 2 and int(numbers[0])>int(numbers[1]):
                    print("범위가 유효하지 않습니다")
                else:
                    try:
                        logs[title][f"{l()[1]}.{l()[2]}"].append(numbers)
                    except KeyError:
                        logs[title][f"{l()[1]}.{l()[2]}"] = [numbers]
                    save(logs)
            elif word_menu == 3:
                try:
                    print("\n\n".join(logs[title][f"{l()[1]}.{l()[2]}"]))
                except:
                    print("오늘 기록이 없습니다.")
            elif word_menu == 4:
                entire_menu = input("1. 검색 2. 날짜별 보기 b. 이전 ")
                if entire_menu == "1":
                    while True:
                        try:
                            search = int(input("찾고자 하는 페이지를 적으세요. (ex) 124, 426 | "))
                            
                            
                            if not search:       
                                print("값을 입력해주세요")
                                
                            else:
                                for i in logs[title].keys():
                                    for z in logs[title][i]:
                                            
                                            if str(search) in z:
                                                print("\n"+"-".join(z))
    
                                            elif len(z) == 2 and search>int(z[0]) and search<int(z[1]):
                                                    print("\n"+"-".join(z))
                                            
                                        
                                            
                                print("\n\n모두 찾았습니다")
                                input("\n돌아가시려면 아무 키나 입력하십시오")
                                break
                        except ValueError:
                            print("단일 페이지 숫자를 입력하세요")
                                
                        
                                
                            
                        
                            
                    
                elif entire_menu == "2":
                    
                    t = 0
                    sort_keys = sorted(list(logs[title].keys()))
                    all_list = [f"{i} ({len(logs[title][i])})" for i in sort_keys]
                    if all_list:
                        length = len(all_list)
                        while t<length:
                            
                                
                                print("\t".join(all_list[t:t+3]))
                                t += 3
                        while True:
                            date = input("해당 날짜를 입력하세요. ")
                            try:
                                print("\n".join(["-".join(i) for i in logs[title][date]]))
                                input("메뉴로 돌아가려면 아무키나 입력하십시오.")
                                break
                    
                            except KeyError:
                                print("존재하지 않는 날짜입니다.")
                            
                                
                                
                        
                    else:
                         print("기록이 없습니다")
                elif entire_menu == "b":
                    pass
                else:
                    print("잘못 입력하셨습니다")
                    

                
                    
                    
                
        
        except ValueError:
            print("숫자를 입력해주세요")
            
    
                

            
while True:
    
    menu = start()
    if logs["목록"][menu-1] == "영어":
        word()
    elif logs["목록"][menu-1] == "콜로케이션":
        pass
        
    else: 
        anything(menu)
        
    
    
