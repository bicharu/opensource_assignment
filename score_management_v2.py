########################################################

# 프로그램명 : 성적 관리 프로그램

# 작성자 : 2022041033/박성웅

# 작성일 : 2025.04.12

# 프로그램 설명 : 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를  계산하는 프로그램

#########################################################

class std_score:
    def __init__(self, StdNum, Name, Eng, C, Python):
        self.StdNum = StdNum
        self.Name = Name
        self.Eng = Eng
        self.C = C
        self.Python = Python
        self.Sum = std_score.ScoreSum(Eng, C, Python)
        self.Avg = std_score.ScoreAvg(self.Sum, 3)
        self.Grd = std_score.ScoreGrd(self.Avg)
        

    def ScoreSum(Eng, C, Python):
        return Eng + C + Python
    
    def ScoreAvg(Sum, len):
        return Sum / len
    
    def ScoreGrd(Avg):
        if Avg>=95:
            return 'A+'
        elif Avg>=90:
            return 'A'
        elif Avg>=85:
            return 'B+'
        elif Avg>=80:
            return 'B'
        elif Avg>=75:
            return 'C+'
        elif Avg>=70:
            return 'C'
        elif Avg>=65:
            return 'D+'
        elif Avg>=60:
            return 'D'
        else:
            return 'F'

Subject = ['영어', 'C-언어', '파이썬']
Student = []

def is_already_StdNum(Student, StdNum):
    index = len(Student)
    while True:
        if index >= 1:
            count = 0
            for i in Student:
                if int(i.StdNum) == StdNum:
                    StdNum = input("이미 존재하는 학번입니다. 다시 입력해주세요 >> ")
                    StdNum = is_correct_StdNum(StdNum)
                    break
                count += 1
            if count == index:
                return StdNum
        else: return StdNum

def is_correct_StdNum(StdNum):
    while True:
        if StdNum.isdigit():
            if len(StdNum) == 10:
                return int(StdNum)
            else:
                StdNum = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 >> ")
        else :
            StdNum = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 >> ")

def is_correct_score(score): # 범위를 초과하거나 자료형이 안맞는 예외 처리 함수
    while True:
        if score.isdigit():
            score = int(score)
            if score>=0 and score<=100:
                return score
            else:
                score = input("잘못된 값입니다. 100미만의 양수를 입력해주세요 >> ")
        else:
            score = input("잘못된 값입니다. 100미만의 양수를 입력해주세요 >> ")


def ScoreRnk (Student): # 학생의 등수를 구하는 함수
    Avgs = []
    Ranks = []

    for i in range(len(Student)):
        Avgs.append(Student[i].Avg)
    sortedAvgs = sorted(Avgs, reverse=True) 

    for i in Avgs:
        Ranks.append(sortedAvgs.index(i)+1)

    return Ranks

def PrintScore(Student, Ranks): # 출력 함수
    print("="*76)
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("="*76)
    for i in range(len(Student)):
        print( str(Student[i].StdNum) + "\t" + Student[i].Name + "\t" + str(Student[i].Eng) + "\t" + str(Student[i].C)+ "\t" + str(Student[i].Python) + "\t" \
              + str(Student[i].Sum) + "\t" + str(round(Student[i].Avg, 1)) + "\t" + Student[i].Grd + "\t" + str(Ranks[i]) + "\n")
        
def InputScore():

    SubScore = []

    StdNum = input("학번 >> ")
    StdNum = is_correct_StdNum(StdNum)
    StdNum = is_already_StdNum(Student, StdNum)

    Name = input("학생 이름 >> ")

    for j in range(len(Subject)): 
        sub_score = input(Subject[j] +"점수 >> ")
        sub_score = is_correct_score(sub_score)
        SubScore.append(sub_score)

    student = std_score(StdNum, Name, SubScore[0], SubScore[1], SubScore[2])
    Student.append(student)

def SearchForStdNum(Student, Ranks):
    
    while True:
        StdNum = input("찾고자 하는 학생의 학번을 입력해주세요 >> ")
        StdNum = is_correct_StdNum(StdNum)
        for i in range(len(Student)):
            if Student[i].StdNum == StdNum:
                print("="*76)
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("="*76)
                print( str(Student[i].StdNum) + "\t" + Student[i].Name + "\t" + str(Student[i].Eng) + "\t" + str(Student[i].C)+ "\t" + str(Student[i].Python) + "\t" \
                      + str(Student[i].Sum) + "\t" + str(round(Student[i].Avg, 1)) + "\t" + Student[i].Grd + "\t" + str(Ranks[i]) + "\n")
                return i
        print("해당 학번을 찾을 수 없습니다.")

def SearchForStdName(Student, Ranks):
    
    while True:    
        Name = input("찾고자 하는 학생의 이름을 입력해주세요 >> ")
        for i in range(len(Student)):
            if Student[i].Name == Name:
                print("="*76)
                print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("="*76)
                print( str(Student[i].StdNum) + "\t" + Student[i].Name + "\t" + str(Student[i].Eng) + "\t" + str(Student[i].C)+ "\t" + str(Student[i].Python) + "\t" \
                      + str(Student[i].Sum) + "\t" + str(round(Student[i].Avg, 1)) + "\t" + Student[i].Grd + "\t" + str(Ranks[i]) + "\n")
                return i
        print("해당 이름을 찾을 수 없습니다.")

def DelValue(Student, index):
    
    del Student[index]

def ModValue(Student, index):

    SubScore = []

    StdNum = input("학번 >> ")
    StdNum = is_correct_StdNum(StdNum)
    if StdNum == Student[index].StdNum:
        # 학번이 같으면 수정하지 않음
        pass
    else:
        # 학번이 다르므로 중복 체크
        StdNum = is_already_StdNum(Student, StdNum)
    Student[index].StdNum = StdNum

    Student[index].Name = input("학생 이름 >> ")

    for j in range(len(Subject)): 
        sub_score = input(Subject[j] +"점수 >> ")
        sub_score = is_correct_score(sub_score)
        SubScore.append(sub_score)
        
    Student[index].Eng = SubScore[0]
    Student[index].C = SubScore[1]
    Student[index].Python = SubScore[2]
    Student[index].Sum = std_score.ScoreSum(SubScore[0], SubScore[1], SubScore[2])
    Student[index].Avg = std_score.ScoreAvg(Student[index].Sum, 3)
    Student[index].Grd = std_score.ScoreGrd(Student[index].Avg)


def SortByTotal(Student, Ranks):

    # Sorted_Student = []
    # for i in Ranks:
    # Sorted_Student.append(Student[i-1])
    # 후에 Soreted_Student를 return해도 무관

    Student[:] = sorted(Student, key=lambda x: x.Sum, reverse=True)

def Count80up(Student, Ranks):

    count_80up = []

    for i in range(len(Student)):
        if Student[i].Avg >= 80:
            count_80up.append(i)
    
    print("평균이 80점 이상인 학생 : {0}명".format(len(count_80up)))
    for i in count_80up:
        print( str(Student[i].StdNum) + "\t" + Student[i].Name + "\t" + str(Student[i].Eng) + "\t" + str(Student[i].C)+ "\t" + str(Student[i].Python) + "\t" \
              + str(Student[i].Sum) + "\t" + str(round(Student[i].Avg, 1)) + "\t" + Student[i].Grd + "\t" + str(Ranks[i]) + "\n")


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
            menu = int(menu)
            if menu > 0 and menu <= 6:
                return menu
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
            menu = int(menu)
            if menu > 0 and menu <=2:
                return menu
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
            menu = int(menu)
            if menu > 0 and menu <=2:
                return menu
            else: 
                menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")
        else:
            menu = input("잘못된 값입니다. 다시 입력해주세요 >> ")

def main(): # 메인 함수

    while True:
        menu_value = SelectMenu()
        if menu_value == 1:
            if len(Student) < 5:
                InputScore()
            elif len(Student) == 5:
                print("입력받을 수 있는 학생의 정원은 5명입니다. 다른 메뉴를 선택해주세요")

        elif menu_value == 2:
            if not Student:
                print("출력할 수 있는 데이터가 없습니다. 먼저 성적을 입력해주세요")
            else:
                PrintScore(Student, ScoreRnk(Student))

        elif menu_value == 3:
            if not Student:
                print("검색할 수 있는 데이터가 없습니다. 먼저 성적을 입력해주세요")
            else:
                menu_value_2 = SelectMenu_2()
                if menu_value_2 == 1:
                    list_index = SearchForStdNum(Student, ScoreRnk(Student))
                    menu_value_3 = SelectMenu_3()
                    if menu_value_3 == 1:
                        DelValue(Student, list_index)
                    elif menu_value_3 == 2:
                        ModValue(Student, list_index)
                elif menu_value_2 == 2:
                    list_index = SearchForStdName(Student, ScoreRnk(Student))
                    menu_value_3 = SelectMenu_3()
                    if menu_value_3 == 1:
                        DelValue(Student, list_index)
                    elif menu_value_3 == 2:
                        ModValue(Student, list_index)

        elif menu_value == 4:
            if not Student:
                print("정렬할 데이터가 없습니다. 먼저 성적을 입력해주세요.")
            else:
                SortByTotal(Student, ScoreRnk(Student))

        elif menu_value == 5:
            Count80up(Student, ScoreRnk(Student))

        elif menu_value == 6:
            print("프로그램을 성공적으로 종료했습니다.")
            break

main()