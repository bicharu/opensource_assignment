# 틱택토 게임!
# 2022041033 박성웅

from random import *
from time import *

def SelectMenu():
    print('''
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡿⡿⡿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣶⡎⣲⣵⣷⣰⣽⣿⣿⣿⣿⣿⣿⣿⣷⡦⡣⣮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣕⢱⣮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⣺⣿⣿⠨⣿⠝⣬⣪⣹⣿⣿⣿⣿⡯⡪⣿⡏⣇⣵⡹⢸⣿⢹⣨⣪⣻⣿⣿⣿⣿⡧⣹⣿⢻⣨⣪⡙⣿⡟⣕⣥⡙⢿⣿⣿
    ⣿⣿⣿⣿⡇⣺⣿⣿⠨⣿⠸⣿⣿⢿⣬⣪⣺⣿⡯⡪⣿⡪⢺⣿⡿⢸⣇⢳⣿⡿⣿⣬⣪⣺⣿⡗⢼⣿⡐⣿⣿⠇⣾⡪⣲⣦⡧⣷⣿⣿
    ⣿⣿⣿⣿⣧⣺⣿⣿⣬⣿⣷⣬⣢⣿⣿⣿⣿⣿⣯⣮⣿⣷⣥⣣⣷⣕⣿⣶⣬⣪⣾⣿⣿⣿⣿⣯⣺⣿⣷⣦⣵⣵⣿⣷⣦⣣⣵⣽⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    \n''')
    
    menu = input("Tic-Tac-Toe 게임에 오신걸 환영합니다! 게임을 시작하시겠습니까?(Y/N) >> ")
    while True:
        if menu == 'Y' or menu == 'N':
            return menu
        else: menu = input("잘못된 값입니다. 다시 입력해주세요(Y/N) >> ")

def SelectTurn():

    r_s_p = {0 : "가위", 1 : "바위", 2 : "보"}

    print("순서 결정을 위한 가위바위보를 시작합니다.")
    sleep(1)

    while True:
        sleep(1)
        print("가위...")
        sleep(1)
        print("바위...")
        sleep(1)
        p_turn = input("보! >> ")
        cpu_turn = randint(0,2)
        if p_turn == r_s_p[cpu_turn]:
            print("비겼습니다! 한판 더 진행합니다!")
        elif p_turn == "가위":
            if r_s_p[cpu_turn] == "바위":
                print("컴퓨터의 승리! 컴퓨터가 선공으로 진행합니다.")
                return False
            if r_s_p[cpu_turn] == "보":
                print("플레이어의 승리! 플레이어의 선공으로 진행합니다.")
                return True
        elif p_turn == "바위":
            if r_s_p[cpu_turn] == "가위":
                print("플레이어의 승리! 플레이어의 선공으로 진행합니다.")
                return True
            if r_s_p[cpu_turn] == "보":
                print("컴퓨터의 승리! 컴퓨터가 선공으로 진행합니다.")
                return False
        elif p_turn == "보":
            if r_s_p[cpu_turn] == "가위":
                print("컴퓨터의 승리! 컴퓨터가 선공으로 진행합니다.")
                return False
            if r_s_p[cpu_turn] == "바위":
                print("플레이어의 승리! 플레이어의 선공으로 진행합니다.")
                return True
        else: print('반칙이에요! "가위", "바위", "보" 3가지 중에서 하나를 입력해주세요')

def PrintGameBoard(a):

    o_or_x = {0 : " ", 1 : 'O', 2 : 'X'}
    print('''
              |         |          
         {0}    |    {1}    |    {2}
              |         |
     ---------|---------|---------
              |         |
         {3}    |    {4}    |    {5}
              |         |
     ---------|---------|---------
              |         |
         {6}    |    {7}    |    {8}
              |         |
    '''.format(*[o_or_x[a[i][j]] for i in range(len(a)) for j in range(len(a[0]))]))


def PlayerTurn(a):

    x = input("x좌표를 입력해주세요(0~2) >> ")
    while True:
        if x.isdigit():
            x = int(x)
            if not(x >= 0 and x <= 2):
                x = input("잘못된 값입니다. 0에서 2사이의 값을 입력해주세요 >> ")
            elif x >= 0 and x <= 2:
                break
        else: x = input("잘못된 값입니다. 0데서 2사이의 값을 입력해주세요 >> ")
    y = input("y좌표를 입력해주세요 >> ")
    while True:  
        if y.isdigit():
            y = int(y)
            if not(y >= 0 and y <= 2):
                y = input("잘못된 값입니다. 0에서 2사이의 값을 입력해주세요 >> ")
            elif y >= 0 and y <= 2:
                break
        else: y = input("잘못된 값입니다. 0에서 2사이의 값을 입력해주세요 >> ")
    CheckInput(a, x, y)

def CpuTrun(a):
    while True:
        x = randint(0,2)
        y = randint(0,2)
        if a[y][x] == 0:
            a[y][x] = 2
            break

def CheckInput(a, x, y):

    if a[y][x] == 0:
        a[y][x] = 1
    else:
        print("이미 해당 좌표에 값이 존재합니다.")
        PlayerTurn(a)


def CheckWinCon(a):
    positions = []
    if all(a[i][0] == a[i][j] for i in range(len(a)) for j in range(1, len(a[0]))):
        positions += [(i, j) for i in range(len(a)) for j in range(len(a[0]))]
        if a[positions[0][0]][positions[0][1]] == 2:
            return False
        elif a[positions[0][0]][positions[0][1]] == 1:
            return True
    elif all(a[0][i] == a[j][i] for i in range(len(a)) for j in range(1, len(a[0]))):
        positions += [(j, i) for i in range(len(a)) for j in range(len(a[0]))]
        if a[positions[0][0]][positions[0][1]] == 2:
            return False
        elif a[positions[0][0]][positions[0][1]] == 1:
            return True
    elif a[0][0] == a[1][1] == a[2][2]:
        positions += [(0, 0), (1, 1), (2, 2)]
        if a[0][0] == 2:
            return False
        elif a[0][0] == 1:
            return True
    elif a[2][0] == a[1][1] == a[0][2]:
        positions += [(2, 0), (1, 1), (0, 2)]
        if a[2][0] == 2:
            return False
        elif a[2][0] == 1:
            return True
    if all(a[i][j] != 0 for i in range(len(a)) for j in range(len(a[0]))):
        return None

def main():

    menu_value = SelectMenu()

    while True:
        Output = []
        for i in range(3):
            Output.append([0, 0, 0])
        
        if menu_value == 'Y':
            turn = SelectTurn()
            PrintGameBoard(Output)
            if turn == True:
                while True:
                    print("플레이어의 차례입니다.")
                    PlayerTurn(Output)
                    PrintGameBoard(Output)
                    condition = CheckWinCon(Output)
                    if condition == True:
                        print("플레이어의 승리!")
                        break
                    elif condition == False:
                        print("컴퓨터의 승리!")
                        break
                    elif condition == None:
                        print("무승부!")
                        break
                    print("컴퓨터의 차례입니다.")
                    CpuTrun(Output)
                    PrintGameBoard(Output)
                    condition = CheckWinCon(Output)
                    if condition == True:
                        print("플레이어의 승리!")
                        break
                    elif condition == False:
                        print("컴퓨터의 승리!")
                        break
                    elif condition == None:
                        print("무승부!")
                        break
            elif turn == False:
                while True:
                    print("컴퓨터의 차례입니다.")
                    CpuTrun(Output)
                    PrintGameBoard(Output)
                    condition = CheckWinCon(Output)
                    if condition == True:
                        print("플레이어의 승리!")
                        break
                    elif condition == False:
                        print("컴퓨터의 승리!")
                        break
                    elif condition == None:
                        print("무승부!")
                        break
                    print("플레이어의 차례입니다.")
                    PlayerTurn(Output)
                    PrintGameBoard(Output)
                    condition = CheckWinCon(Output)
                    if condition == True:
                        print("플레이어의 승리!")
                        break
                    elif condition == False:
                        print("컴퓨터의 승리!")
                        break
                    elif condition == None:
                        print("무승부!")
                        break

        elif menu_value == 'N':
            print("프로그램을 성공적으로 종료하였습니다.")
            break
        replay_value = input("한판 더 하시겠습니까?(Y/N) >> ")
        if replay_value == 'N':
            break

main()