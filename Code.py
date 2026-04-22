import random

def name_to_nums(name):
  if name == "Rock":
    return 0
  if name == "Spock":
    return 1
  if name == "Paper":
    return 2
  if name == "Lizzard":
    return 3
  if name == "Scizor":
    return 4


def nums_to_names(nums):
  if nums==0:
    return "Rock"
  if nums==1:
    return "Spock"
  if nums==2:
    return "Paper"
  if nums==3:
    return "Lizzard"
  if nums==4:
    return "Scizor"
  else:
   print("out of range")


def rpsls(player_choice):
    print()
    comp_choice = random.randrange(0, 5)
    comp_number = comp_choice
    comp_choice = (nums_to_names(random.randrange(0, 5)))
    print("Player chooses", player_choice)
    player_number = name_to_nums(player_choice)
    print("Computer choose", comp_choice)


    diff = (player_number-comp_number)%5
    if (diff==0):
      print ("Tie!")
    elif(diff==1)or(diff==2):
      print("Computer Wins!")
    else:
       print("player wins")



rpsls("Rock")
rpsls("Spock")
rpsls("Paper")
rpsls("Lizzard")
rpsls("Scizor")
