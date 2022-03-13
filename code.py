import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def deal_cards():
  user.append(cards[random.randint(0, 12)])
  user.append(cards[random.randint(0, 12)])
  computer.append(cards[random.randint(0, 12)])
  computer.append(cards[random.randint(0, 12)])

def total(card):
  return sum(card)

def final_hand():
  print(f"Your final hand: {user}, final score: {total(user)}")
  print(f"Computer's final hand: {computer}, final score: {total(computer)}")

print(logo)
deal_cards()
print(f"Your cards: {user}, current score: {total(user)}")
print(f"Computer's first card: {computer[0]}")

deal = True

while deal == True:
  if total(user) == 21:
    final_hand()
    print("You win 😁")
    deal = False
  else:
    choice = input("Type 'y' to get another card, type 'n' to pass: ")

    if total(computer) < 17:
      computer.append(cards[random.randint(0, 12)])
      total(computer)
    if total(user) == 21:
      final_hand()
      print("You win 😁")
      deal = False


    if choice == "y":
      user.append(cards[random.randint(0, 12)])
      total(user)
      if total(user) > 21:
        final_hand()
        print("You went over. Computer Win 🙁")
        deal = False
      else:
        print(f"Your cards: {user}, current score: {total(user)}")
        print(f"Computer's first card: {computer[0]}")
    elif choice == "n":
      if total(computer) > 21:
        final_hand()
        print("Computer went over. You win 😁")
      elif total(user) > total(computer):
        final_hand()
        print("You win 😁")
      elif total(computer) > total(user):
        final_hand()
        print("Computer win 🙁")
      else:
        final_hand()
        print("Draw")
      deal = False
