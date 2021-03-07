import time, json
import random
import re
import os
# 디자인, collocation 시험 구현
# 함수나 변수로 수정 필요한 것 혹은 중복되는 것 빼서 코드 정리 (수정이 쉬움)
# 복습 여부 기록 (+ 알고 모르는 것 기록해서 따로 관리) , 이어하기,새로하기 
# UI 개선 os.system('cls') 위치
# 추가후 삭제시 날짜 남는거 수정
# 수정기능 

# 지우기 아무것도 입력 안했을 때(돌아가지도록)
# 빈 영단어 혹은 범위 입력시 메시지
# Index 1 부터 시작하도록 바꾸기
# 아무것도 입력 안하면, 다시 묻기 (날짜)


# 당일거 학습
# 날라감 방지로 주기적 복사 기능 넣기

# 중복 실행 방지

# invalid syntax 에러도 나오게 하려면 어떻게하지?

# 영어는 데이터 공부 기능도 넣기 (공부한 거 복습)

# 복습 안한거 모아서 볼 수 있도록 하기
# 암기 내용들도 입력하기

def save(logs):
    with open("review.txt","w") as f:
            json.dump(logs,f)
def three_stack(li_st):
    t = 0
    
    if li_st:
        length = len(li_st)
        
        while t<length:
                print("\n"+"\t".join([f"({t+i}) "+ z for i,z in enumerate(li_st[t:t+3])]))
                t += 3
    

try:
    with open("review.txt") as f:
        if not f.readlines():
            logs = {"목록":["영어"],"영어":{"log":{}}}
        else:
            f.seek(0)
            logs = json.load(f)
            
except FileNotFoundError:
    logs = {"목록":["영어"],"영어":{}}
except UnicodeDecodeError:
    file_error = input("파일 내용이 json 형태가 아닙니다,\n\n 수정해주세요.(파일을 초기화 하려면 n 을 누르세요.)")  
    if file_error == "n":
        with open("review.txt","w") as f:
            logs = {"목록":["영어"],"영어":{"log":{}}}
            json.dump(logs,f)
    else:
        exit()
def start():
    while True:
        os.system('cls')
        intro = input(f"""복습 프로그램 입니다.

(a.추가 d.삭제 p. 백업)



{" ".join([f'{i+1}'+'.'+x for i,x in enumerate(logs["목록"])])}


어떤 것을 복습하시겠습니까? """)

        if intro == "a" or intro == "A":
            new = input("""


                         추가할 과목을 적어주세요 | """)
            if new == "":
                pass
            else:
                logs["목록"].append(new)
                logs[new] = {"log":{}}
                save(logs)
        elif intro == "d" or intro == "D":
            while True:
                try:
                    delete = int(input(f"""

                    {" ".join([f'{i+1}'+'.'+x for i,x in enumerate(logs["목록"])])}

                    삭제할 과목 번호를 적어주세요 | """))
                    if delete == "":
                        pass
                    else:
                        try:
                            del logs[logs["목록"][delete-1]]
                            logs["목록"] = logs["목록"][:delete-1]+logs["목록"][delete:]
                            save(logs)
                            break
                        except IndexError:
                            print("범위를 벗어났습니다")
                            time.sleep(0.2)
                        
                        
                    
                except ValueError:
                    print("숫자를 적어주세요")
                    time.sleep(0.2)
        
        else:
            try:
                intro = int(intro)
                if len(logs["목록"])>0 and intro > 0 and len(logs["목록"])>=intro:
                    return intro
                else:
                    print("목록에 없습니다.")
                    time.sleep(0.2)
            except ValueError:
                
                print("잘못 입력하셨습니다")
                time.sleep(0.2)
def delyed_cal(title):
    
    l = time.localtime
    n = time.time()-86400 if logs[title][log]["{l()[1]}.{l()[2]}"] # 오늘꺼 복습 했는지 여부에 따라 오늘기준 어제기준 나뉘는데
    yesterday = f"{l(n)[1]}.{l(n)[2]}"
    review_terms = {1,4,7,14,30]
    
    for i in logs[title][log].keys():
          objt = time.mktime(time.strptime({f"{l()[0]}."+i,"%Y.%m.%d"))
          logs[title][log][i]      
def word():
    delayed = []
    while True:
        os.system('cls')
        try:
            word_menu = input("\n영어 복습 입니다.\n\n1. 복습하기  2. 추가하기 3. 오늘 기록보기 4. 전체 기록보기 b. 이전 ")
            n = time.time()
            l = time.localtime   # 계산된 시간 변환용
            if word_menu == "1":
                
                review_list = [86400, 86400*4, 86400*7, 86400*14, 86400*30]
                review_date = []
                word_list = []
                for i in review_list:
                    try:
                        temp = f"{l(n-i)[1]}.{l(n-i)[2]}" 
                        review_date.append[temp] # 아래 루프에서 쓸 데이터 미리 처리
                        for i in logs["영어"][temp]:
                            
                            word_list.append(i) # 복습으로 뽑아낼 word_list 만들기
                    except KeyError: # 존재하는 날짜만 뽑아오기
                        pass
                
                    
                    
                
                if word_list:
                    print("복습을 시작합니다.\n\n 복습은 랜덤하게 제공됩니다.(b. 취소)")
                    while word_list: 
                        eng_kor_choice = random.randrange(0,2)
                        word_choiced = random.choice(word_list) # 랜덤한 문장과 뜻 순서, input으로 물어보기
                        first = input(word_choiced[eng_kor_choice])
                        if first == "b":
                           break
                        else:
                            
                            second = input(word_choiced[eng_kor_choice == 0])
                            if second == "b":
                                break
                            else:
                                del word_list[word_list.index(word_choiced)]
                                
                    for i in review_date: # log에 복습 횟수 갱신
                        try:
                            logs["영어"]["log"][review_date][0] += 1
                            logs["영어"]["log"][review_date][1] = n # time.time()을 저장하여 계산 용이하도록 
                        except KeyError:
                            pass
                                
                
                else:
                    print("복습할 것이 없습니다.")
                    time.sleep(0.2)
                    
                
            elif word_menu == "2":
                while True:
                
                    eng_add = input("추가할 영문을 입력하세요 | ")
                    if eng_add == "":
                        break
                    else:
                        kor_add = input("그 뜻을 입력하세요 | ")
                        if kor_add == "":
                            pass
                        else:
                            try:
                                logs["영어"][f"{l()[1]}.{l()[2]}"].append([eng_add,kor_add])
                                
                            except KeyError:
                                logs["영어"][f"{l()[1]}.{l()[2]}"] =[[eng_add,kor_add]]
                                logs["영어"]["log"][f"{l()[1]}.{l()[2]}"] = [0,None]
            
                            save(logs)
                            break
            elif word_menu == "3":
                try:
                    date = f"{l()[1]}.{l()[2]}"
                    
                    print("\n"+"\n\n".join([" || ".join(i) for i in logs["영어"][date]]))
                    logs["영어"][date][0] # 오늘 기록 없는지 확인용 (추가후 지우면 빈리스트 남아서)
                    today_menu = input("\n메뉴로 돌아가려면 아무키나 입력하십시오. d. 삭제 | ")
                    if today_menu == "d":
                        while logs["영어"][date]:
                            print("\n\n".join([f"({a}) " + z for a,z in enumerate([" || ".join(i) for i in logs["영어"][date]])]))
                            
                            choiced_date = input("지우고자 하는 번호를 입력해주세요 | ")
                            if choiced_date == "":
                                break
                            else:
                                try:
                                    del logs["영어"][date][int(choiced_date)]
                                    save(logs)
                                    
                                    
                                except IndexError:
                                    print("해당 번호가 없습니다")
                                    time.sleep(0.2)
                                except ValueError:
                                    print("숫자를 입력해주세요")
                                    time.sleep(0.2)
                        
                except:
                    print("오늘 기록이 없습니다.")
                    time.sleep(0.2)
            elif word_menu == "4":
                entire_menu = input("1. 검색 2. 날짜별 보기 ")
                if entire_menu == "1":
                    search = input("찾고자 하는 영어 혹은 한글을 적으세요. | ")
                    if search == "":
                        break
                    else:
                        for i in logs["영어"].keys():
                            for z in logs["영어"][i]:
                                if search in z[0] or search in z[1]:
                                    print("\n"+" || ".join(z))
                        print("\n\n모두 찾았습니다")
                        input("\n돌아가시려면 아무 키나 입력하십시오")
                    
                elif entire_menu == "2":
                    
                    t = 0
                    sort_keys = sorted(list(logs["영어"].keys()))
                    all_list = [f"{i} [{len(logs['영어'][i])}개]" for i in sort_keys]
                    three_stack(all_list)
                    while True:
                        try:
                            date = input("해당 날짜 및 번호를 입력하세요. | ")
                            if date == "":
                                break
                            else:
                                date = sort_keys[int(date)]
                                print("\n" + "\n\n".join([f"({i}) "+" || ".join(x) for i,x in enumerate(logs["영어"][date])]))
                        except ValueError:
                            
                            
                            try:
                                print("\n" + "\n\n".join([f"({i}) "+" || ".join(x) for i,x in enumerate(logs["영어"][date])]))
                                
                                
                    
                            except KeyError:
                                print("존재하지 않는 날짜입니다.")
                                time.sleep(0.2)
                        except IndexError:
                            print("존재하지 않는 번호입니다.")
                            time.sleep(0.2)
                            
                        date_delete = input("\n메뉴로 돌아가려면 아무키나 입력하십시오. d. 삭제 | ")
                        if date_delete == "d":
                                    while True:
                                        print("\n" + "\n\n".join([f"({i}) "+" || ".join(x) for i,x in enumerate(logs["영어"][date])]))
                                        
                                        choiced_date = input("지우고자 하는 번호를 입력해주세요 | ")
                                        if choiced_date == "":
                                            break
                                        else:
                                            try:
                                                del logs["영어"][date][int(choiced_date)]
                                                save(logs)
                                                
                                            except IndexError:
                                                print("해당 번호가 없습니다")
                                                time.sleep(0.2)
                                            except ValueError:
                                                print("숫자를 입력해주세요")
                                                time.sleep(0.2)
                                            
                                        
                                        
                                            

                        break
                            
                                
                                
                        
                    else:
                         print("기록이 없습니다")
                         time.sleep(0.2)
                elif entire_menu == "":
                    pass
                else:
                    print("잘못 입력하셨습니다")
                    time.sleep(0.2)
            elif word_menu == "b":
                break
                    

                
                    
                    
                
        
        except :
            print("에러")
            time.sleep(0.2)
    

##def collocation():
def anything(menu):
    title = logs['목록'][menu-1]
    while True:
        os.system('cls')
        try:
            word_menu = input(f"\n{title} 복습 입니다.\n\n1. 복습하기  2. 추가하기 3. 오늘 기록보기 4. 전체 기록보기 b. 이전 ")
            n = time.time()
            l = time.localtime
            if word_menu == "1":
                
                review_list = [86400*30, 86400*14, 86400*7, 86400*4, 86400 ]
                
                word_list = []
                review_date = []
                for i in review_list:
                    try:
                        temp = f"{l(n-i)[1]}.{l(n-i)[2]}"
                        review_date.append(temp)
                        for z in logs[title][temp]:
                            
                            word_list.append(["-".join(z)]) 
                    except KeyError:
                        pass
                if word_list:
                    print("\n복습할 진도들입니다. ")
                        
                        
                        
                            
                            
                    print("\n"+"\n".join(["\n".join(i) for i in word_list]))
                    input("\n돌아가시려면 아무 키나 입력하십시오")
                    
                    for i in review_date: # log에 복습 횟수 갱신
                        try:
                            logs[title]["log"][review_date][0] += 1
                            logs[title]["log"][review_date][1] = n # time.time()을 저장하여 계산 용이하도록 
                        except KeyError:
                            pass
                       
                        
                else:
                    print("복습할 것이 없습니다.")
                    time.sleep(0.2)
            elif word_menu == "2":
                while True:                
                    today_range = input("\n추가할 진도를 입력하세요 (ex) 124, 124-200, 124~300 ... | ")
                    if today_range == "":
                        break
                    else:
                        numbers = re.findall("\d+",today_range)
                        if not numbers:
                            print("입력되지 않았습니다.")
                            time.sleep(0.2)
                        elif len(numbers) > 2:
                            print("한 장이나 둘 사이의 범위를 입력해주세요")
                            time.sleep(0.2)
                        elif len(numbers) == 2 and int(numbers[0])>int(numbers[1]):
                            print("범위가 유효하지 않습니다")
                            time.sleep(0.2)
                        else:
                            try:
                                logs[title][f"{l()[1]}.{l()[2]}"].append(numbers)
                            except KeyError:
                                logs[title][f"{l()[1]}.{l()[2]}"] = [numbers]
                                logs[title]["log"][f"{l()[1]}.{l()[2]}"] = [0,None]
                            save(logs)
                            break
            elif word_menu == "3":
                
                try:
                    date = f"{l()[1]}.{l()[2]}"
                    three_stack(["-".join(i) for i in logs[title][date]])
                    logs[title][f"{l()[1]}.{l()[2]}"][0]
                    today_delete = input("\n돌아가시려면 아무 키나 입력하십시오 d. 삭제 | ")
                    if today_delete == "d":
                            while logs[title][date]:
                                three_stack(["-".join(x) for i,x in enumerate(logs[title][date])])
                                
                                any_choiced_date = input("\n지우고자 하는 번호를 입력해주세요 | ")
                                if any_choiced_date == "":
                                    break
                                else:
                                    try:
                                        del logs[title][date][int(any_choiced_date)]
                                        save(logs)
                                        
                                    except IndexError:
                                        print("해당 번호가 없습니다")
                                        time.sleep(0.2)
                                    except ValueError:
                                        print("숫자를 입력해주세요")
                                        time.sleep(0.2)
                except:
                    print("오늘 기록이 없습니다.")
                    time.sleep(0.2)
            elif word_menu == "4":
                entire_menu = input("\n1. 검색 2. 날짜별 보기 ")
                if entire_menu == "1":
                    while True:
                        try:
                            search = input("\n찾고자 하는 페이지를 적으세요. (ex) 124, 426 | ")
                            if search == "":
                                break
                            else:
                                stack_list = []
                                
                                if not search:       
                                    print("값을 입력해주세요")
                                    time.sleep(0.2)
                                    
                                else:
                                    for i in logs[title].keys():
                                        for z in logs[title][i]:
                                                
                                                if search in z:
                                                    stack_list.append("-".join(z) + f" ({i})")
        
                                                elif len(z) == 2 and int(search)>int(z[0]) and int(search)<int(z[1]):
                                                        stack_list.append("-".join(z) + f" ({i})")
                                    three_stack(stack_list)
                                                
                                            
                                                
                                    print("\n\n모두 찾았습니다")
                                    input("\n돌아가시려면 아무 키나 입력하십시오")
                                    break
                        except ValueError:
                            print("단일 페이지 숫자를 입력하세요")
                            time.sleep(0.2)
                                
                        
                                
                            
                        
                            
                    
                elif entire_menu == "2":
                    
                    t = 0
                    sort_keys = sorted(list(logs[title].keys()))
                    all_list = [f"{i} [{len(logs[title][i])}개]" for i in sort_keys]
                    three_stack(all_list)
                    
                    while True:
                        try:
                            date = input("\n해당 날짜 및 번호를 입력하세요. | ")
                            if date == "":
                                break
                            else:
                                date = sort_keys[int(date)]
                                three_stack([ "-".join(x) for x in logs[title][date]])
                        except ValueError:
                            
                            
                            try:
                                three_stack([ "-".join(x) for x in logs[title][date]])
                                
                                
                    
                            except KeyError:
                                print("존재하지 않는 날짜입니다.")
                                time.sleep(0.2)
                        except IndexError:
                            print("존재하지 않는 번호입니다.")
                            time.sleep(0.2)
                        
                        
                        any_date_delete = input("메뉴로 돌아가려면 아무키나 입력하십시오. d. 삭제 | ")
                        if any_date_delete == "d":
                            while logs[title][date]:
                                three_stack(["-".join(x) for i,x in enumerate(logs[title][date])])
                                
                                any_choiced_date = input("\n지우고자 하는 번호를 입력해주세요 | ")
                                if any_choiced_date == "":
                                    break
                                else:
                                    try:
                                        del logs[title][date][int(any_choiced_date)]
                                        save(logs)
                                        
                                    except IndexError:
                                        print("해당 번호가 없습니다")
                                        time.sleep(0.2)
                                    except ValueError:
                                        print("숫자를 입력해주세요")
                                        time.sleep(0.2)
                        break
                
                        
                            
                                
                                
                        
                    else:
                         print("기록이 없습니다")
                         time.sleep(0.2)
                elif entire_menu == "b":
                    pass
                else:
                    print("잘못 입력하셨습니다")
                    time.sleep(0.2)
            elif word_menu == "b":
                break
            else:
                print("잘못 입력하셨습니다")
                time.sleep(0.2)
                    

                
                    
                    
                
        
        except ValueError:
            print("숫자를 입력해주세요")
            time.sleep(0.2)
            
    
                

            
while True:
    
    menu = start()
    if logs["목록"][menu-1] == "영어":
        word()
    elif logs["목록"][menu-1] == "콜로케이션":
        pass
        
    else: 
        anything(menu)
        
    
    
