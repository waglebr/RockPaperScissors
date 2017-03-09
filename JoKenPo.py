print("Let's play Rock-Paper-Scissors!")
# Players names
player1 = input("\nPlayer 1, enter your name:\n") 
player2 = input("\nPlayer 2, enter your name:\n")
# Takes player choice and converts it to lower case
hand1 = input("\n%s, please choose Rock, Paper or Scissors:\n"%(player1)).lower()
# Checks if player chose a valid option
while not hand1 in {"rock", "paper", "scissors"}: 
    print("INVALID OPTION!")
    hand1 = input("\n%s, please choose Rock, Paper or Scissors:\n"%(player1)).lower()
hand2 = input("\n%s, please choose Rock, Paper or Scissors:\n"%(player2)).lower()
while not hand2 in {"rock", "paper", "scissors"}:
    print("INVALID OPTION!")
    hand2 = input("\n%s, please choose Rock, Paper or Scissors:\n"%(player2)).lower()
# Checks who's the winner            
if hand1 == hand2:
    print("\nIt's a tie!")
elif (hand1 == "rock" and hand2 == "scissors") or \
(hand1 == "paper" and hand2 == "rock") or \
(hand1 == "scissors" and hand2 == "paper"):
        print("\n%s wins! :D"%(player1))
else: print("\n%s wins! :D"%(player2))