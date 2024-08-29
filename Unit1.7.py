#To read a card as input and output if the card is lucky or not

Lucky_cards = ["HEART ACE","SPADE ACE","CLUB ACE","DIAMOND ACE"]
Choice = input("Enter The Card Name You Want From The List : ").upper()

for i in Lucky_cards:
  
    if (i == Choice):
         print("Card Is Lucky :")
         break
else:
    print("Card Is Unlucky :")
    
