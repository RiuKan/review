import time, json
import random
import re
import os
# 기초 도구가 탄탄해야 효율적으로 코드를 짬. 효율 차이가 스위치 수준으로 수 배 차이 날 때가 많음.
# 올해만 작동하게 되어있음
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
# At this hour ?
# informative (유익하다고)

# 암기 내용 추가도 괜찮을 듯.
review_list = (86400*30, 86400*14, 86400*7, 86400*4, 86400)
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
    
def on_press(key):
    
    
    
    return key
    
def start():
    global logs
    while True:
        os.system('cls')
        intro = input(f"""복습 프로그램 입니다.

(a.추가 d.삭제 p. 백업 h. 복구)



{" ".join([f'{i+1}'+'.'+x for i,x in enumerate(logs["목록"])])}


어떤 것을 복습하시겠습니까? """)
        


        
            

        if intro == "a" or intro == "A":
            new = input("""


                         추가할 과목을 적어주세요 | """)
            if new == "":
                pass
            else:
                if new in logs:
                        print("해당 과목이 이미 존재합니다.")
                        time.sleep(0.2)
                else: 
                        logs["목록"].append(new)
                        logs[new] = {"review":{},"delayed":{}}
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
        elif intro == "p" or intro == "P":
            with open("backup.txt","w") as f:
                json.dump(logs,f)
            print("백업이 완료되었습니다.")
            time.sleep(0.2)
        elif intro == "h" or intro == "H":
            with open("backup.txt","r") as f:
                logs = json.load(f)
            print("복구가 완료되었습니다")
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
def delayed_cal(title):
    
    lt = time.localtime
    n = time.time()
    y = n-86400
    yesterday = f"{lt(y)[1]}.{lt(y)[2]}"
    today = f"{lt()[1]}.{lt()[2]}"
    review_terms = (1,4,7,14,30)
    review_dates = logs[title]["review"].keys()
    data_days = {}
    
    
    if today in review_dates: # 오늘 복습 했으면 1회 넣기
        # 각각 학습날짜 와 현재날짜 차이 계산해서, 복습 필수 횟수  넣기
        for i in logs[title].keys():
            if i == "review" or i == "delayed": # 키목록에 날짜 마지막에 review 키가 있어서, 제외
                continue
            data_days[i] = []
            day_diff = (n-time.mktime(time.strptime(f"{lt()[0]}."+i,"%Y.%m.%d")))//86400
            for l,t in enumerate(review_terms):
                l += 1
                if t == day_diff: # 아래랑 여기만 차이 있음
                    data_days[i].append(l)
                    if l == 5: # 앞으로 예정 복습까지 남은 일수 계산
                        data_days[i].append(None)
                    else:
                        data_days[i].append(review_terms[l+1]-t)# 복습 했으면, 복습 검사 할때 오늘꺼 빼주게 됨.
                    break
                elif t > day_diff:
                    data_days[i].append(l-1)
                    # l이 5라도, 똑같은 결과
                    data_days[i].append(review_terms[l]-day_diff)
                    break
                else:
                    if l==5:
                        data_days[i].append(5)
                        data_days[i].append(None)
                    continue
                
            # 복습한 횟수 빼내기
            count = 0 
            for k in range(data_days[i][0]):
                z = review_list[-k-1]
                tmp_time = time.mktime(time.strptime(f"{lt()[0]}."+i,"%Y.%m.%d"))+z
                
                tmp_day = time.localtime(tmp_time) 
            # 날짜 변환 함수 만들기
                day_string = f"{tmp_day[1]}.{tmp_day[2]}"
                 # 첫번째 걸린 날짜 가 최근 복습 일자라서 
                if day_string in review_dates:
                    data_days[i][0] -= 1
                    if count == 0:
                        data_days[i].append(day_string)
                    count += 1
            if count == 0:
                data_days[i].append(None)
               
                    
                    
    else:   # 안했으면 1회 빼기
        for i in logs[title].keys():
            if i == "review" or i == "delayed": 
                continue
            data_days[i] = []
            day_diff = (n-time.mktime(time.strptime(f"{lt()[0]}."+i,"%Y.%m.%d")))//86400
            for l,t in enumerate(review_terms):
                l += 1
                if t >= day_diff:
                    
                    data_days[i].append(l-1)
                    data_days[i].append(review_terms[l]-day_diff)
                    break
                else:
                    if l==5:
                        data_days[i].append(5)
                        data_days[i].append(None)
                    continue
                
            count = 0
            for k in range(data_days[i][0]):
                z = review_list[-k-1]
                tmp_time = time.mktime(time.strptime(f"{lt()[0]}."+i,"%Y.%m.%d"))+z
                
                tmp_day = time.localtime(tmp_time) 
            # 날짜 변환 함수 만들기
                day_string = f"{tmp_day[1]}.{tmp_day[2]}"
                
                if day_string in data_days:
                    data_days[i][0] -= 1
                    if count == 0:
                        data_days[i].append(day_string)
                    count += 1
            if count == 0:
                data_days[i].append(None)

        
    
    for key,value in data_days.items():
            
        if value[0] != 0:
            logs[title]["delayed"][key] = value

    # 5회 밀린 회차는, 당일 학습으로 넣기(5번 안한건 오늘 한걸로 다시 넣기),               
    delete = []
    for key,value in logs[title]["delayed"].items():
        if key == "did":
            continue
        try:
            delayed_count = value[0] - logs[title]["delayed"]["did"][key][0]
        except KeyError:
            delayed_count = value[0]# 5번 이면 
        if delayed_count == 5:
            if not logs[title].get(today):
                logs[title][today] = []
            for i in logs[title][key]:
                for index,z in enumerate(i):
                    i[index] = z+f" *{key}"
                logs[title][today].append(i)
                delete.append(key)
                del logs[title][key]
    for i in delete:
        del logs[title]["delayed"][i]

    with open("review.txt","w") as f:
        json.dump(logs,f)
def delayed_play(title):
    delayed_cal(title)
    recommend = []
    delay_dict = logs[title]["delayed"] # {학습날짜:[밀린 횟수,예정 복습까지 남은 일수,최근 복습일],did:{학습날짜:[복습횟수,최근 복습일]}}
    try:
        delay_did = logs[title]["delayed"]["did"]
    except KeyError:
        delay_did = {}
    key_list = []
    for i in delay_dict.keys():
        try:
            if delay_dict[i][0] == delay_did[i][0] or i == "did":
                continue
            else:
                key_list.append(i)
        except KeyError:
            if i == "did":
                continue
            key_list.append(i)
                
    delay_dict_keys = sorted(key_list)
    if key_list:
    
        for index, key in enumerate(delay_dict_keys):
            
            numbers_1, next_review, recent_review_1 = delay_dict[key][0],delay_dict[key][1],(delay_dict[key][2] if delay_dict[key][2] else None)
            try:
                numbers_2, recent_review_2 = delay_did[key][0], delay_did[key][1]
                
            except KeyError:
                
                numbers_2, recent_review_2 = 0,None
            
            if not recent_review_1 or recent_review_2:
                time_diff = None
            elif recent_review_1 and recent_review_2:
                time_diff = (time.time() - time.mktime(time.strptime(f"{time.localtime()[0]}."+ (recent_review_1 if recent_review_1>=recent_review_2 else recent_review_2) ,"%Y.%m.%d")))//86400
            else:
                time_diff = (time.time() - time.mktime(time.strptime(f"{time.localtime()[0]}."+ (recent_review_1 if recent_review_1 else recent_review_2) ,"%Y.%m.%d")))//86400 # 올해만 작동하게 되어있음
            print (f"\n\n({index}) {key} 일자 :: {str(time_diff) + ' 일 전 복습' if time_diff else '이전 복습 없음' } | {numbers_1-numbers_2} 회 미복습 | {str(int(next_review))+'일 후 복습 예정' if next_review else '예정 없음'}")
            
            
            if (next_review == None or next_review > 3) and (time_diff == None or time_diff > 3):
                
                recommend.append(index)
        print("\n\n추천 복습 : ", " , ".join([f"({i})"for i in recommend]))
        while True:
            choiced_review = input("\n하고자 하는 복습 일자 및 번호를 입력하세요 (b. 이전) : ")
            if choiced_review == "b" or choiced_review == "":
                print("취소 되었습니다")
                time.sleep(0.2)
                break
            try:
                key_choiced = delay_dict_keys[int(choiced_review)]
                contents = logs[title][key_choiced]
                
            except ValueError:
                try:
                    key_choiced = choiced_review
                    contents = logs[title][key_choiced]
                    
                except KeyError:
                    print("날짜를 잘못 입력하셨습니다.")
                    time.sleep(0.2)
                    continue
            except IndexError:
                print("번호가 범위를 초과하였습니다.")
                time.sleep(0.2)
                continue
        
        
            if title == "영어":
                word_list = []
                for i in contents:
                        
                        word_list.append(i)
                print("\n복습을 시작합니다.\n\n 복습은 랜덤하게 제공됩니다.(b. 취소)")
                while word_list: 
                    eng_kor_choice = random.randrange(0,2)
                    word_choiced = random.choice(word_list) # 랜덤한 문장과 뜻 순서, input으로 물어보기
                    first = input("\n"+word_choiced[eng_kor_choice])
                    if first == "b":
                       confirm = "n" 
                       break
                    else:
                        
                        second = input(word_choiced[eng_kor_choice == 0])
                        if second == "b":
                            confirm = "n" 
                            break
                        else:
                            del word_list[word_list.index(word_choiced)]
                try:
                    if confirm:
                        pass
                except NameError:
                    confirm = input("\n복습 체크 하시겠습니까? Y/n | ")
                    
                        
            else:
                word_list = []
                            
                
                    
                        
                print(contents)
                for z in contents:
                            
                            word_list.append(["-".join(z)]) 
                if word_list:
                    print("\n복습할 진도들입니다. ")
                    print("\n"+"\n".join(["\n".join(i) for i in word_list]))
                
                confirm = input("\n복습 체크 하시겠습니까? Y/n | ")
            if confirm == "Y" or confirm == "y" or confirm == "":
                try:
                    delay_did[key_choiced][0] += 1
                    delay_did[key_choiced][1] = f"{time.localtime()[1]}.{time.localtime()[2]}"
                    if delay_dict[key_choiced][0] == delay_did[key_choiced][0] and delay_dict[key_choiced][1] == None: # 소멸 되는 조건, 횟수를 채울 때 예정 복습일이 없어야 함.안그러면 추후 밀렸을 시 최근 복습 일자를 잃게 됨
                        del logs[title]["delayed"][key_choiced], logs[title]["delayed"]["did"][key_choiced]
                        del delay_did[key_choiced], delay_dict[key_choiced]
                except KeyError:
                    delay_did[key_choiced] = []
                    delay_did[key_choiced].append(1) 
                    delay_did[key_choiced].append(f"{time.localtime()[1]}.{time.localtime()[2]}")
                    if delay_dict[key_choiced][0] == delay_did[key_choiced][0] and delay_dict[key_choiced][1] == None:
                        del logs[title]["delayed"][key_choiced], logs[title]["delayed"]["did"][key_choiced]
                        del delay_did[key_choiced], delay_dict[key_choiced]
                
                logs[title]["delayed"]["did"] = delay_did
                print("체크 완료")
                time.sleep(0.2)
                break
            else:
                print("취소되었습니다")
                time.sleep(0.2)
                break
    else:
        print("\n밀린 복습이 없습니다")
        time.sleep(0.2)
        
            
        
    
                    
                        
            
    
    
    # 최근 복습일, 추후 복습일 넣기
    # 아니면 오늘 하면 가장 좋은 빠진 복습일자 추천하기
    # 가장 오래됐고, 앞으로 예정일자도 가장 많이 남은 일자 복습
    # 4일 기준으로 잡기
    
    
                    
                
                
                                               
            
            

    
            
def word():
    delayed = []
    
    while True:
        
        os.system('cls')
##        try:
            
        n = time.time()
        l = time.localtime   # 계산된 시간 변환용
        try:
            check = "오늘 복습 완료" if logs["영어"]["review"][f"{l(n)[1]}.{l(n)[2]}"] else ""
        except KeyError:
            check = "복습을 아직 안했습니다."
        word_menu = input(f"\n영어 복습 입니다.\n\n{check}\n\n1. 복습하기  2. 추가하기 3. 오늘 기록보기 4. 전체 기록보기 | b. 이전 | ")
        if word_menu == "1":
            
            
            review_choice = input("\n1. 밀린 복습하기 2. 복습하기 ")
            if review_choice == "1":
                delayed_play("영어")
                save(logs)
        
            elif review_choice == "2":
            
            
                word_list = []
                for i in review_list:
                    try:
                        
                        
                        for i in logs["영어"][f"{l(n-i)[1]}.{l(n-i)[2]}"]:
                            
                            word_list.append(i) # 복습으로 뽑아낼 word_list 만들기
                    except KeyError: # 존재하는 날짜만 뽑아오기
                        pass
            
                
                    
                    
                
                if word_list:
                    print("복습을 시작합니다.\n\n 복습은 랜덤하게 제공됩니다.(b. 취소)")
                    while word_list: 
                        eng_kor_choice = random.randrange(0,2)
                        word_choiced = random.choice(word_list) # 랜덤한 문장과 뜻 순서, input으로 물어보기
                        first = input("\n"+ word_choiced[eng_kor_choice])
                        if first == "b":
                           break
                        else:
                            
                            second = input(word_choiced[eng_kor_choice == 0])
                            if second == "b":
                                break
                            else:
                                del word_list[word_list.index(word_choiced)]
                                
                    
                    
                    logs["영어"]["review"][f"{l(n)[1]}.{l(n)[2]}"] = True
                    save(logs)
                     
                
                    
                
                            
                    
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
                                if not logs["영어"][date]:
                                    del logs["영어"][date]
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
                sort_keys.remove("review");sort_keys.remove("delayed")
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
                                            if not logs["영어"][date]:
                                                del logs["영어"][date]
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
                    

                
                    
                    
                
        
##        except :
##            print("에러")
##            time.sleep(0.2)
    

##def collocation():
def anything(menu):
    title = logs['목록'][menu-1]
    
    while True:
        
        os.system('cls')
        try:
            n = time.time()
            l = time.localtime
            try:
                check = "오늘 복습 완료" if logs[title]["review"][f"{l(n)[1]}.{l(n)[2]}"] else ""
            except KeyError:
                check = "복습을 아직 안했습니다."
            word_menu = input(f"\n{title} 복습 입니다.\n\n{check}\n\n1. 복습하기  2. 추가하기 3. 오늘 기록보기 4. 전체 기록보기 b. 이전 ")
            if word_menu == "1":
                review_choice = input("\n1. 밀린 복습하기 2. 복습하기 ")
                if review_choice == "1":
                    delayed_play(title)
                    save(logs)
                elif review_choice == "2":
                    
                        
                        
                        
                        word_list = []
                        
                        for i in review_list:
                            try:
                                
                                
                                for z in logs[title][f"{l(n-i)[1]}.{l(n-i)[2]}"]:
                                    
                                    word_list.append(["-".join(z)]) 
                            except KeyError:
                                pass
                        if word_list:
                            print("\n복습할 진도들입니다. ")
                                
                                
                                
                                    
                                    
                            print("\n"+"\n".join(["\n".join(i) for i in word_list]))
                            review_check = input("\n복습 완료 체크 하시겠습니까? Y/n | ")
                            if review_check == "y" or review_check == "Y" or review_check == "":
                                     logs[title]["review"][f"{l(n)[1]}.{l(n)[2]}"] = True
                                     save(logs)
                            else:
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
                                        if not logs["title"][date]:
                                            del logs["title"][date]
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
                    sort_keys.remove("review");sort_keys.remove("delayed")
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
                                        if not logs["title"][date]:
                                            del logs["title"][date]
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
            
    
                

try:
    with open("review.txt") as f:
        if not f.readlines():
            logs = {"목록":["영어"],"영어":{"review":{},"delayed":{}}}
        else:
            f.seek(0)
            logs = json.load(f)            
except FileNotFoundError:
    logs = {"목록":["영어"],"영어":{"review":{},"delayed":{}}}
except UnicodeDecodeError:
    file_error = input("파일 내용이 json 형태가 아닙니다,\n\n 수정해주세요.(파일을 초기화 하려면 n 을 누르세요.)")  
    if file_error == "n":
        with open("review.txt","w") as f:
            logs = {"목록":["영어"],"영어":{"review":{},"delayed":{}}}
            json.dump(logs,f)
    else:
        exit()            
while True:
    
    menu = start()
    if logs["목록"][menu-1] == "영어":
        word()
    elif logs["목록"][menu-1] == "콜로케이션":
        pass
        
    else: 
        anything(menu)
        
    
    
