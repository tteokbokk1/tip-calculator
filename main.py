#collect info about the bill
initial_bill = input("Welcome to Henry's tip calculator!\nWhat was your total bill?\n")
tip_amount = input("Got it. Now what percentage tip would you like to give?\n10, 12, 15, 20, or 25?\n")

#calculate payment amount
tip_multiplier = 1 + (int(tip_amount)/100)
payment = float(initial_bill) * tip_multiplier

#split the bill among party
party_size = input("Cool. Now how many people do you want to split the bill across?\n")
cost_per_person = round(payment / int(party_size), 2)

#print output
final_message = f"Alrighty. Each person should pay ${cost_per_person}"
print(final_message)