#A card is drawn at random from a deck of well-shuffled cards. Find the probability of it being neither a king nor a spade

Total_cards=52
Spade_cards=13
Kings=4
Spade_king=1

Total_spade=Spade_cards+Kings-Spade_king

Probability=(Total_cards-Total_spade)/Total_cards

print("Your Probability Is : ",Probability)
