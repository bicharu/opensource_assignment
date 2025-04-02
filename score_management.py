# 성적관리 프로그램
# 2022041033 박성웅

Subject = ["영어","C언어","파이썬"] # input시 과목명 출력 편의를 위한 리스트
Output = [] # 최종 출력을 위한 리스트

def is_already_StdNum(a, b):
    index = len(a)
    while True:
        if index >= 1:
            count = 0
            for i in range(index):
                if int(a[i][0]) == int(b):
                    b = input("이미 존재하는 학번입니다. 다시 입력해주세요 >> ")
                    b = is_correct_StdNum(b)
                    break
                count += 1
            if count == index:
                return b
        else: return b

def is_correct_StdNum(a):
    while True:
        if a.isdigit() == True:
            if len(a) == 10:
                return a
            else:
                a = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 >> ")
        else :
            a = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 >> ")

def is_correct_score(a): # 범위를 초과하거나 자료형이 안맞는 예외 처리 함수
    while True:
        if a.isdigit() == True:
            Int = int(a)
            if Int>=0 and Int<=100:
                return Int
            else:
                a = input("잘못된 값입니다. 100미만의 양수를 입력해주세요 >> ")
        else:
            a = input("잘못된 값입니다. 100미만의 양수를 입력해주세요 >> ")

def ScoreSum (a): # 3과목의 합을 구하는 함수
    scoresum = 0
    for i in range(len(a)):
        scoresum += a[i]
    return scoresum

def ScoreAvg (a): # 3과목의 평균을 구하는 함수
    return a/3

def ScoreGrd (a): # 학생의 학점을 구하는 함수
    if a>=95:
        return 'A+'
    elif a>=90:
        return 'A'
    elif a>=85:
        return 'B+'
    elif a>=80:
        return 'B'
    elif a>=75:
        return 'C+'
    elif a>=70:
        return 'C'
    elif a>=65:
        return 'D+'
    elif a>=60:
        return 'D'
    else:
        return 'F'

def ScoreRnk (a): # 학생의 등수를 구하는 함수
    list = []
    rank = []

    for i in range(len(a)):
        list.append(a[i][6])
    sortedlist = sorted(list, reverse=True) 

    for i in list:
        rank.append(sortedlist.index(i)+1)

    return rank

def PrintScore(a, b): # 출력 함수
    print("="*76)
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("="*76)
    for i in range(len(a)):
        print( a[i][0] + "\t" + a[i][1] + "\t" + str(a[i][2]) + "\t" + str(a[i][3])+ "\t" + str(a[i][4]) + "\t" + str(a[i][5]) + "\t" + str(round(a[i][6], 1)) + "\t" + a[i][7] + "\t" + str(b[i]) + "\n")

def InputScore():
    Score = [] #[학번, 이름, 영어, C, 파이썬, 총점, 평균, 학점]
    tmp_Score = []

    StdNum = input("학번 >> ")
    StdNum = is_correct_StdNum(StdNum)
    StdNum = is_already_StdNum(Output, StdNum)
    Score.append(StdNum)

    Score.append(input("학생 이름 >> "))

    for j in range(len(Subject)): 
        Input = input(Subject[j] +"점수 >> ")
        Input = is_correct_score(Input)
        Score.append(Input)
        tmp_Score.append(Input)

    Sum = ScoreSum(tmp_Score)
    Avg = ScoreAvg(Sum)
    Grd = ScoreGrd(Avg)

    Score.append(Sum)
    Score.append(Avg)
    Score.append(Grd)

    Output.append(Score)

def SearchForStdNum(a, b):
    
    while True:
        Num = input("찾고자 하는 학생의 학번을 입력해주세요 >> ")
        Num = is_correct_StdNum(Num)
        for i in range(len(a)):
            if a[i][0] == Num:
                print("="*76)
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("="*76)
                print( a[i][0] + "\t" + a[i][1] + "\t" + str(a[i][2]) + "\t" + str(a[i][3])+ "\t" + str(a[i][4]) + "\t" + str(a[i][5]) + "\t" + str(round(a[i][6], 1)) + "\t" + a[i][7] + "\t" + str(b[i]) + "\n")
                return i
        print("해당 학번을 찾을 수 없습니다.")

def SearchForStdName(a, b):
    
    while True:    
        Name = input("찾고자 하는 학생의 이름을 입력해주세요 >> ")
        for i in range(len(a)):
            if a[i][1] == Name:
                print("="*76)
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("="*76)
                print( a[i][0] + "\t" + a[i][1] + "\t" + str(a[i][2]) + "\t" + str(a[i][3])+ "\t" + str(a[i][4]) + "\t" + str(a[i][5]) + "\t" + str(round(a[i][6], 1)) + "\t" + a[i][7] + "\t" + str(b[i]) + "\n")
                return i
        print("해당 이름을 찾을 수 없습니다.")

def DelValue(a, b):
    
    del a[b]

def ModValue(a, b):

    tmp_Score = []

    tmp_std_num = input("학번 >> ")
    tmp_std_num = is_correct_StdNum(tmp_std_num)
    if a[b][0] != tmp_std_num:
        a[b][0] = is_already_StdNum(Output, a[b][0])
    else:
        a[b][0] == tmp_std_num

    a[b][1] = input("학생 이름 >> ")

    for j in range(len(Subject)): 
        a[b][j + 2] = input(Subject[j] +"점수 >> ")
        a[b][j + 2] = is_correct_score(a[b][j + 2])
        tmp_Score.append(a[b][j + 2])

    Sum = ScoreSum(tmp_Score)
    Avg = ScoreAvg(Sum)
    Grd = ScoreGrd(Avg)

    a[b][len(Subject) + 2] = Sum
    a[b][len(Subject) + 3] = Avg
    a[b][len(Subject) + 4] = Grd

def SortByTotal(a):

    a[:] = sorted(a, key=lambda x: x[5], reverse=True)

def Count80up(a):

    count_80up = []

    for i in range(len(a)):
        if a[i][6] >= 80:
            count_80up.append(i)
    
    print("평균이 80점 이상인 학생 : {0}명".format(len(count_80up)))
    for i in count_80up:
        print(a[i])


def SelectMenu():

    print("="*76)
    print("{0: >36}".format("성적관리 프로그램"))
    print("="*76)
    print("1. 성적 입력")
    print("2. 전체 성적 출력")
    print("3. 검색")
    print("4. 성적 정렬하기(총점 기준)")
    print("5. 80점 이상 학생 출력")
    print("6. 끝내기")
    print("="*76)

    menu = input("메뉴를 선택해주세요 >> ")

    while True:
        if menu.isdigit():
            if int(menu) > 0 and int(menu) <= 6:
                return int(menu)
            else:
                menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")
        else:
            menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")

def SelectMenu_2():

    print("="*76)
    print("{0: >36}".format("메뉴 입력"))
    print("1. 학번 검색")
    print("2. 이름 검색")
    print("="*76)

    menu = input("메뉴를 선택해주세요 >> ")

    while True:
        if menu.isdigit():
            if int(menu) > 0 and int(menu) <=2:
                return int(menu)
            else: 
                menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")
        else:
            menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")

def SelectMenu_3():

    print("="*76)
    print("{0: >36}".format("메뉴 입력"))
    print("1. 해당 자료 삭제")
    print("2. 해당 자료 수정")
    print("="*76)

    menu = input("메뉴를 선택해주세요 >> ")

    while True:
        if menu.isdigit():
            if int(menu) > 0 and int(menu) <=2:
                return int(menu)
            else: 
                menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")
        else:
            menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")

def main(): # 메인 함수


    while True:
        menu_value = SelectMenu()
        if menu_value == 1 and len(Output) < 5:
            InputScore()
        elif menu_value == 1 and len(Output) == 5:
            print("입력받을 수 있는 학생의 정원은 5명입니다. 다른 메뉴를 선택해주세요")
        elif menu_value == 2 and len(Output) == 0:
            print("출력할 수 있는 데이터가 없습니다. 먼저 성적을 입력해주세요")
        elif menu_value == 2:
            PrintScore(Output, ScoreRnk(Output))
        elif menu_value == 3 and len(Output) == 0:
            print("검색할 수 있는 데이터가 없습니다. 먼저 성적을 입력해주세요")
        elif menu_value == 3:
            menu_value_2 = SelectMenu_2()
            if menu_value_2 == 1:
                list_index = SearchForStdNum(Output, ScoreRnk(Output))
                menu_value_3 = SelectMenu_3()
                if menu_value_3 == 1:
                    DelValue(Output, list_index)
                elif menu_value_3 == 2:
                    ModValue(Output, list_index)
            elif menu_value_2 == 2:
                list_index = SearchForStdName(Output, ScoreRnk(Output))
                menu_value_3 = SelectMenu_3()
                if menu_value_3 == 1:
                    DelValue(Output, list_index)
                elif menu_value_3 == 2:
                    ModValue(Output, list_index)
        elif menu_value == 4:
            if len(Output) == 0:
                print("정렬할 데이터가 없습니다. 먼저 성적을 입력해주세요.")
            else:
                SortByTotal(Output)
        elif menu_value == 5:
            Count80up(Output)
        elif menu_value == 6:
            print("프로그램을 성공적으로 종료했습니다.")
            break

main()