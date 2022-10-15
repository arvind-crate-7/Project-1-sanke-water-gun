import time
time1=time.time()
def description():
  print("Game description:")
  print("Some rules are there to decide who will win:")
  print("1) If you choose snake")
  print(
    "   a) if the computer chooses a gun, you lose. Because gun kill the snake."
  )
  print(
    "   b) if the computer chooses water, you won. Because snake drink that water."
  )
  print("   c) if the computer chooses snake then draw.")
  print("1)Vice versa is true")


txt = "Welcome to Snake Water Gun game."
print( txt.center(90))
print("Game description:")
print("This is a game between you and the computer.")
print(
  "you had to choose between Snake Water and Gun And then the computer choose any one of them.\n"
)
print("If you want to see rules. then press 1.")
print("\nChoose anyone.")
print("{snake,water,gun}")
import random

timeofgame = 1
you = 0
computer = 0
time = 0

while (timeofgame <=10):
  list = ["snake", "water", "gun"]
  computer1 = random.choice(list)
  print("\n\n", time, ") score:-", end="")
  txt3 = "You    Computer"
  print(txt3.center(125))
  print("                                                                   ",
        you, "     ", computer)
  print("\nChoose:- ", end="")
  input1 = input()
  if input1 == "1":
    description()
    timeofgame = timeofgame - 1

  elif input1 == "snake":
    print("\n\nyou choose :- snake")
    print("And Computer choose:", computer1)

    if computer1 == "snake":
      print("So,Draw")
      you = you + 1
      computer = computer + 1

    elif computer1 == "water":
      print("Congratulation,You Won!")
      you = you + 1

    elif computer1 == "gun":
      print("Oops,You loose")
      computer = computer + 1

  elif input1 == "water":
    print("\n\nyou choose :- water")
    print("And Computer choose:", computer1)

    if computer1 == "snake":
      print("Oops,You loose")
      computer = computer + 1

    elif computer1 == "water":
      print("So,Draw")
      you = you + 1
      computer = computer + 1

    elif computer1 == "gun":
      print("Congratulation,You Won!")
      you = you + 1

  elif input1 == "gun":
    print("\n\nyou choose :- gun")
    print("And Computer choose:", computer1)

    if computer1 == "snake":
      print("Congratulation,You Won!")
      you = you + 1

    elif computer1 == "water":
      print("So,Draw")
      print("Oops,You loose")
      computer = computer + 1

    elif computer1 == "gun":
      print("So,Draw")
      you = you + 1
      computer = computer + 1

  else:
    print("Invalid Input.")
    timeofgame = timeofgame - 1

  if (timeofgame == 9):
    print(
      "                                                                   ",
      you, "     ", computer)

  timeofgame = timeofgame + 1
  time = time + 1

if you > computer:
  print("\n\nCongratulation, You won this game!")

elif you < computer:
  print("Oops,You loose this game!")

else:
  print("Oops, Both score is same so game Draw")
import time
time5=time.time()
total=time5-time1
print(total,"sec")
