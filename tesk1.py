# 5명의 학생 이름과 학생당 3과목의 점수를 입력받아 총점, 평균, 학점, 등수를 출력하는 프로그램
# 2022041033 박성웅

Subject = ["영어","C언어","파이썬"] # input시 과목명 출력 편의를 위한 리스트
Student = [] # 총점, 평균, 학점을 계산하기 위해 1차적으로 [학번, 이름, 점수1, 점수2, 점수3]을 저장하는 리스트
Output = [] # 최종 출력을 위해 [총점, 평균, 학점] [등수]를 저장하는 리스트

def is_already_StdNum(a, b):
    index = len(a)
    if index >= 1:
        for i in range(index):
            if b == (a[i][0]):
                b = input("이미 존재하는 학번입니다. 다시 입력해주세요 : ")
                is_already_StdNum(a,b)
    else: return b



def is_correct_StdNum(a):
    while True:
        if a.isdigit() == True:
            if len(a) == 10:

                return a
            else:
                a = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 : ")
        else :
            a = input("잘못된 값입니다. 10자리 숫자를 입력해주세요 : ")

def is_correct_score(a): # 범위를 초과하거나 자료형이 안맞는 예외 처리 함수
    while True:
        if a.isdigit() == True:
            Int = int(a)
            if Int>=0 and Int<=100:
                return Int
            else:
                a = input("잘못된 값입니다. 100미만의 양수를 입력해주세요 : ")
        else:
            a = input("못된 값입니다. 100미만의 양수를 입력해주세요 : ")


def ScoreSum (a): # 3과목의 합을 구하는 함수
    scoresum = 0
    for i in range(2,5):
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

    for i in range(5):
        list.append(a[i][1])
    sortedlist = sorted(list, reverse=True) 

    for i in list:
        rank.append(sortedlist.index(i)+1)

    return rank

def PrintScore(a, b): # 출력 함수
    print("{0: >46}".format("성적관리 프로그램"))
    print("="*76)
    print("학번\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("="*76)
    for i in range(5):
        print( b[i][0] + "\t" + b[i][1] + "\t" + str(b[i][2]) + "\t" + str(b[i][3])+ "\t" + str(b[i][4]) + "\t" + str(a[i][0]) + "\t" + str(round(a[i][1], 1)) + "\t" + a[i][2] + "\t" + str(a[-1][i]) + "\n")

def main(): # 메인 함수수
    for i in range(5): # 이중 리스트

        Score = [] #[학번, 이름, 영어, C, 파이썬]

        for j in range(5):
            if j==0:
                StdNum = input("학번 : ")
                StdNum = is_correct_StdNum(StdNum)
                StdNum = is_already_StdNum(Student, StdNum)
                Score.append(StdNum)
            elif j == 1:
                Score.append(input("학생 이름 : "))
            else:
                Input = input(Subject[j-2] +"점수 : ")
                Input = is_correct_score(Input)
                Score.append(Input)

        Student.append(Score)

        list = [] #[총점, 평균, 학점]
        
        Sum = ScoreSum(Score)
        Avg = ScoreAvg(Sum)
        Grd = ScoreGrd(Avg)
        

        # list라는 리스트에 총점, 평균, 학점을 추가한 후 해당 list라는 리스트를 Output리스트에 추가
        list.append(ScoreSum(Score))
        list.append(ScoreAvg(Sum))
        list.append(ScoreGrd(Avg))
        Output.append(list)


    Output.append(ScoreRnk(Output)) #Output리스트 뒤에 등수list를 따로 추가

    PrintScore(Output, Student) # 출력 함수 호출

main()