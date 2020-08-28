Name = []
Money = []

def Start_Game():
  print("\nWELCOME TO GUESSING GAME")
  while 1:
    print("\n1 - ERASE ALL PLAYERS")
    print("2 - PRINT PLAYERS")
    print("3 - ADD PLAYER")
    print("4 - RULES")
    print("5 - PLAY GAME")
    print("6 - EXIT")
    Option = int(input("OPTION: "))

    if Option == 1:
      Erase()
    elif Option == 2:
      Print()
    elif Option == 3:
      Add_Players()
    elif Option == 4:
      Rules()
    elif Option == 5:
      Game()
    elif Option == 6:
      print("\nGAME OVER")
      break
    else:
      print("\nINVALID OPTION")

from time import sleep

def Rules():
  sleep(1.5)
  print("\nRULES :-")
  sleep(1.5)
  print("1. PAY 500 TO PLAY THE GAME")
  sleep(1)
  print("2. SELECT A LEVEL")
  sleep(1)
  print("3. SELECT A COLOUR")
  sleep(1)
  print("4. IF YOU FINISH ALL YOUR MONEY, YOU LOSE")
  sleep(1)
  print("6. THE COLOUR YOU CHOOSE WILL GENERATE GUESSES")
  sleep(1)
  print("7. IF THE GUESSE IS CORRECT YOU EARN SOME AMOUNT")
  sleep(1)
  print("8. IF THE GUESS IS INCORRECT THEN YOU LOSE MONEY")
  sleep(1)
  print("9. 100 WILL BE DEDUCTED FOR EVERY INCORRECT ANSWER")
  sleep(1)
  print("10. PLAY AND HAVE FUN !!\n")
  sleep(1)

def Player_Details():
  global Money
  global player
  ABC = 0
  N = input("\nPLAYER NAME: ")
  if N in Name:
    player = int((Name.index(N)))
    if Money[player] >= 500:
      Money[player] -= 500
      print("\nHELLO", N)
      ABC = 1
    else:
      print("\nNOT SUFFECIENT MONEY")
  else:
    print("\nINVALID NAME")
  return ABC

def Erase():
  global Money
  global Name
  Password = str(input("\nENTER PASSWORD: "))
  if Password == '#*@&^!?/<$>%' or Password == "I Don't Know The Password":
    print("\nPASSWORD ACCEPTED")
    print("\nPLAYERS ERASED")
    Money = []
    Name = []
  else:
    print("\nPASSWORD DENIED")

def Add_Players():
  global Money
  global Name
  name = input("\nENTER YOUR NAME: ")
  if name not in Name:
    Money.append(1000)
    Name.append(name)
    print("\nPLAYER CREATED")
  else:
    print("\nNAME EXISTS")

def money(num):
  global Money
  print("\nNUMBER:", num)
  if num == 1:
    print("\nYOU GOT 500")
    Money[player] += 500
    print("\nBALANCE:", Money[player])
  elif num == 2:
    print("\nYOU LOST ALL YOUR MONEY")
    Money[player] = 0
    print("\nBALANCE:", Money[player])
  elif num == 3:
    print("\nYOU GOT 300")
    Money[player] += 300
    print("\nBALANCE:", Money[player])
  elif num == 4:
    print("\nYOU GOT 400")
    Money[player] += 400
    print("\nBALANCE:", Money[player])
  elif num == 5:
    print("\nYOU GOT 200")
    Money[player] += 200
    print("\nBALANCE:", Money[player])
  else:
    print("\nYOU LOST 100")
    Money[player] -= 100
    print("\nBALANCE:", Money[player])

level = [5, 10, 50, 100, 1000]

def Level():
  global lev
  L = int(input("\nSELECT A LEVEL BETWEEN 1 - 5: ")) - 1
  if L < 5 and L >= 0:
    lev = level[L]

def Colour():
  print('\n1 - BLUE\n2 - RED\n3 - GREEN\n4 - BLACK\n5 - YELLOW\n6 - QUIT')
  col = int(input("SELECT A COLOUR: ")) - 1
  return col

import time

def Time():
  Time_2 = time.time()
  if Time_2 - Time_1 <= 120:
    print(f'\nYOU HAVE {120 - (Time_2 - Time_1)} SECONDS')
    T = Time_2 - Time_1
  else:
    T = 0
  return T

import random

Colours = ['BLUE', 'RED', 'GREEN', 'BLACK', 'YELLOW', 'QUIT']
Colour_Number = [0, 1, 2, 3, 4, 5]

def Game():
  global Time_1
  LEV = Player_Details()
  if LEV == 1:
    Level()
    Time_1 = time.time()
    while 1:
      if Money[player] > 0:
        T = Time()
        if T == 0:
          print("\nTIME UP")
          print("GAME OVER")
          break
        else:
          C = Colour()
          if C in Colour_Number:
            if C == 5:
              print("\nWINNERS NEVER QUIT, QUITTERS NEVER WIN")
              break
            else:
              num = random.randint(1, lev)
              money(num)
          else:
            print("\nINVALID COLOUR")
      else:
        print("\nYOU ARE OUT OF MONEY")
        break

def Print():
  print(f'\nName: {Name}')
  print(f'Balance: {Money}')

Start_Game()