from time import sleep as slp
import os
from winsound import Beep
import random
from buckshotpictures import *
def bp():
  Beep(100, 350)
def shot():
  Beep(900, 500)
def die(a):
  Beep(1250, a)
def cls():
  os.system("cls")
cls()
bp()
ans = input("Press enter to start game, type skip to skip cutscene: ")

#Opening Cutscene
if ans != "skip":
  cls()
  print(img1)
  print("This is a shotgun.")
  bp()
  slp(5)
  cls()
  print(img2)
  print("This is a buckshot.")
  bp()
  slp(2)
  print("\nThey can be live or blank..")
  bp()
  slp(5)
  cls()
  print(img3)
  print("Every round, few Blanks and few Lives will be chosen.")
  bp()
  slp(4)
  print("\nfor example, 2 Blanks and 3 Lives..")
  bp()
  slp(5)
  cls()
  print(imgReload)
  print("They will be then loaded in a random order, which is known by none.")
  bp()
  slp(7)
  cls()
  print(img5)
  print("A Toss will decide who gets their hands on the shotgun first")
  bp()
  slp(6)
  print("\nThey can choose to shoot their opponent")
  bp()
  slp(6)
  cls()
  print(img6)
  print("Obviously if the buckshot is a live, the opponent will lose a 'life'.")
  shot()
  slp(5)
  print("\nAnd if it turns out to be a blank, the opponent gets the next turn..")
  bp()
  slp(5)
  cls()
  print(img7)
  print("However, they can also shoot themself.")
  shot()
  slp(4)
  print("\nAnd if the buckshot turns out to be blank, they get to shoot again")
  bp()
  slp(4)
  print("\nBut they can lose a 'life' too, if its a live shot..")
  bp()
  slp(5)
  cls()
  print(imgEmpty)
  print("Every player starts with 4 'lives', not to be confused with 'live buckshots'.")
  bp()
  slp(6)
  cls()
  print(imgMachine)
  print("And their 'lives' are recorded automatically by this machine..")
  bp()
  slp(5)
  print("\nHowever if any one loses all of their 'lives'...")
  bp()
  slp(5)
  print("\nIt means they don't have a 'life' anymore...")
  bp()
  slp(5)
  cls()
  print(imgMachineSnapL)
  print("And so the machine snaps off their life support.")
  shot()
  slp(4)
  print("\nTo make sure they really lose their 'life'...")
  bp()
  slp(5)
  print("\nIn other words.....")
  bp()
  slp(5)
  cls()
  print("They die.")
  die(3000)
  cls()
  print(imgNormal)
  print("Understood?")
  bp()
  slp(3)
  input("Welcome to Pythonshot Roulette\nInpired by 'Buckshot Roulette' by Mike Klubnika\n\nPress Enter to start game..")
else:
  cls()
  bp()
  print(imgNormal)
  input("Welcome to Pythonshot Roulette\nInpired by 'Buckshot Roulette' by Mike Klubnika\n\nPress Enter to start game..")

  
def yourDeath():
  cls()
  print(end1)
  slp(2)
  cls()
  print(end2)
  slp(2)
  cls()
  print(end3)
  slp(2)
  cls()
  print(end4)
  slp(2)
  cls()
  print(end5)
  slp(4)
  print("Please give your name.")
  Beep(200, 350)
  slp(3)
  cls()
  slp(3)
  print("Thank you, you may now proceed.")
  Beep(200, 350)
  slp(2)
  print("\nWhere am I?")
  slp(1.5)
  print("Where do i proceed???")
  slp(3)
  print("\nThe gate behind me.")
  Beep(200, 350)
  slp(2)
  print("\nWhere does the gate take me to?")
  slp(3)
  print("\nHell.")
  Beep(200, 350)
  slp(2)
  print("\nHell?? What am i doing in hell?")
  slp(3)
  print("\nOh you must have forgotten.")
  Beep(200, 350)
  slp(3)
  cls()
  print(imgMachine)
  print("You lost.")
  Beep(200, 350)
  slp(4)
  cls()
  print(imgMachineSnapL)
  die(5000)
  print(f"""
        GAME OVER
          Stats:
Rounds Played: {Round}
Total buckshots Fired = {shotsFired}
Blank buckshots Fired = {blshotsFired}
Live buckshots Fired = {shotsFired - blshotsFired}
Remaining Lives of Opponent = {hisLives}""")
  input("Press Enter To Exit...")
  exit()
def hisDeath():
  cls()
  print(imgMachine)
  print("NO")
  bp()
  print("NO")
  bp()
  print("NO")
  bp()
  print("NO")
  bp()
  print("NONO")
  bp()
  print("NONONONONO#%#^%")
  bp()
  print("NONONO24782()*$%&()&*&@IHJASL@#)(*?<>?OOOOON@(*&$*@&*(@$&*@$(*&)))")
  Beep(100, 1500)
  cls()
  print(imgMachineSnapR)
  shot()
  slp(5)
  print(f"""
        YOU WON
         Stats:
Rounds Played: {Round}
Total buckshots Fired = {shotsFired}
Blank buckshots Fired = {blshotsFired}
Live buckshots Fired = {shotsFired - blshotsFired}
Remaining Lives = {urLives}""")
  input("Press Enter To Exit...")
  exit()
#actual game start
cls()
bp()
print("""

                                            
                                            
                                            
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @. .@ #  @@@@@  .@ @.@@.@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @@@@ @@ @ @@. @ @@@@@@@@@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @          @:##.:.::.  @@@         
         @@@.@...@-..-@:+.-:+@.@@@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @@-:-.=+.:%*:.@+@:@@@@@@@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @@:.:...:.*@+..:.*:@.-.@@@         
         @@%@%##%#*@@=@+##+#@=*#@@@         
         @@@@@@@@@@@@@@@@@@@@@@@@@@         
         @@@@@@@@@@.:@==%@.@@@@@@@@         
         @@@@@@@@@@:@@@@@@@@@@@@@@@         
         @@@@@@@@@@:@@@*@@@@@@@@ @@         
         @@@.=+==-@:*@@@@@@@@@.@@@@         
                                            
                                            
                                            

""")
print("You signed the contract, your life support is now connected to the machine.")
input("\nPress enter to continue...")
cls()
print("""

                                            
                                            
                                            
                  ...                       
               .----:-:                     
              .:-+=-=:-+:                   
               :+--+:--:-:...               
               .-:-:+:-:-%*:.               
               .=::-:-:-::%#=               
                .::=::--:::#+:              
                 ::-:::-:-::#:.             
                  -::::::--::#.             
                   :::::=-=--:..            
                    .=:+---=--*.            
                     .-:--:---::            
                       .-*+-*-:.            
                        ...--:..            
                                            
                                            
                                            
                                            
                                            
                                            
                                            

""")
print("He flips a coin....")
urTurn = random.choice([True, False])
urLives = 4
hisLives = 4
Round = 0
bShots = []
fTimeDie = True
angered = False
shotsFired = 0
blshotsFired = 0
slp(3)
print("It lands.")
slp(3)
cls()
print(imgNormal)
if urTurn:
  print("Looks like you are starting first.")
else:
  print("Looks like I will be starting first.")
bp()
input("\nPress enter to continue...")
cls()
while urLives > 0 and hisLives > 0:
  if len(bShots) == 0:
    cls()
    Round += 1
    bShots = ["L", "B"]
    for i in range(0, random.randint(0,3)):
      bShots.append("L")
    for i in range(0, random.randint(0,3)):
      bShots.append("B")
    print(imgReload)
    print(f"Round {Round}: {bShots.count("L")} Live and {bShots.count("B")} Blank Buckshots.")
    bp()
    slp(3)
    print("They are loaded in a random order.")
    bp()
    slp(5)
    cls()
  if urTurn:
    cls()
    print(imgNormal)
    print(f"You have {urLives} Lives.\nHe has {hisLives} lives.")
    print("It's your turn to shoot.")
    ans = input("\nType u to shoot yourself.\nType h to shoot him.\nYour Answer:")
    if ans == "u":
      shotsFired += 1
      cls()
      print(imgUU)
      print("You point the gun towards yourself..")
      slp(3)
      s = random.choice(bShots)
      bShots.remove(s)
      if s == "L":
        urLives -= 1
        cls()
        die(2000)
        if urLives <= 0:
          yourDeath()
        print("Wake up.")
        slp(2)
        cls()
        print(imgNormal)
        if fTimeDie and not angered:
          slp(2)
          print("Hurts doesn't it?")
          bp()
          slp(2)
          print("Too bad you aren't dead yet.")
          bp()
          slp(2)
          print("Wipe off that blood, Let's continue")
          bp()
          slp(4)
          cls()
          print(imgNormal)
          fTimeDie = False
        print(f"You have {urLives} Lives left.")
        if not angered:
          bp()
        slp(5)
        urTurn = False
      elif s == "B":
        blshotsFired += 1
        cls()
        print(imgUU)
        print("(Click)")
        bp()
        slp(3)
        if not angered:
          print("Nice..")
          bp()
          slp(2)
          print("You get another chance.")
          bp()
          slp(4)
    elif ans == "h":
      shotsFired += 1
      cls()
      print(imgUH)
      print("You point the gun towards him.")
      slp(3)
      s = random.choice(bShots)
      bShots.remove(s)
      if s == "L":
        hisLives -=1
        cls()
        print(imgUShot)
        shot()
        slp(3)
        if hisLives <= 0:
          hisDeath()
        cls()
        if not angered:
          print(imgEmpty)
          imgNormal = AimgNormal
          imgHH = AimgHH
          imgUH = AimgUH
          imgUU = AimgUU
          imgHU = AimgHU
          slp(5)
          cls()
          print(imgNormal)
          slp(2)
          print("He's definitely angry now.")
          slp(2)
          print("You can observe changes in his facial expression.")
          slp(3)
          print("And hes more quiet.")
          slp(3)
          cls()
          angered = True
          print(imgNormal)
        else:
          print(imgEmpty)
          slp(3)
          cls()
          print(imgNormal)
        print(f"He has {hisLives} Lives now.")
        slp(5)
        urTurn = False
      elif s == "B":
        blshotsFired += 1
        cls()
        print(imgUH)
        print("(Click)")
        bp()
        slp(3)
        if not angered:
          print("\nWelp.")
          bp()
          slp(2)
          print("Looks like it's my turn now.")
          bp()
          slp(4)
        urTurn = False
  else:
    cls()
    print(imgNormal)
    print(f"You have {urLives} Lives.\nHe has {hisLives} lives.")
    print("It's his turn to shoot.")
    input("\nPress Enter to continue...")
    s = random.choice(bShots)
    if s == "L":
      cls()
      print(imgHU)
      print("He points the gun at you.")
      slp(3)
      cls()
      s = random.choice(bShots)
      bShots.remove(s)
      if s == "L":
        urLives -= 1
        cls()
        die(2000)
        if urLives <= 0:
          yourDeath()
        print("Wake up.")
        slp(2)
        cls()
        print(imgNormal)
        if fTimeDie and not angered:
          slp(2)
          print("Hurts doesn't it?")
          bp()
          slp(2)
          print("Too bad you aren't dead yet.")
          bp()
          slp(2)
          print("Wipe off that blood, Let's continue")
          bp()
          slp(4)
          cls()
          print(imgNormal)
          fTimeDie = False
        print(f"You have {urLives} Lives left.")
        if not angered:
          bp()
        slp(5)
        urTurn = True
      elif s == "B":
        cls()
        print(imgHU)
        print("(Click)")
        bp()
        slp(3)
        if not angered:
          print("\nWelp.")
          bp()
          slp(2)
          print("Looks like it's your turn now.")
          bp()
          slp(4)
        urTurn = True
    elif s == "B":
      cls()
      print(imgHH)
      print("He points the gun towards himself.")
      slp(3)
      cls()
      s = random.choice(bShots)
      bShots.remove(s)
      if s == "L":
        hisLives -=1
        cls()
        print(imgHShot)
        shot()
        slp(3)
        if hisLives <= 0:
          hisDeath()
        cls()
        if not angered:
          print(imgEmpty)
          imgNormal = AimgNormal
          imgHH = AimgHH
          imgUH = AimgUH
          imgUU = AimgUU
          imgHU = AimgHU
          slp(5)
          cls()
          print(imgNormal)
          slp(2)
          print("He's definitely angry now.")
          slp(2)
          print("You can observe changes in his facial expression.")
          slp(3)
          print("And hes more quiet.")
          slp(3)
          cls()
          angered = True
          print(imgNormal)
        else:
          print(imgEmpty)
          slp(3)
          cls()
          print(imgNormal)
        print(f"He has {hisLives} Lives now.")
        slp(5)
        urTurn = True
      elif s == "B":
        cls()
        print(imgHH)
        print("(Click)")
        bp()
        slp(3)