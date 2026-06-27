print("lets go for day 4")

current_stock = 40
delivery = 15
max_capacity = 50

current_stock += delivery
is_overstocked = current_stock > max_capacity
print("'are we overstoked?",is_overstocked)
#the movie discount eligiblity 
is_student=True
is_senior= True
is_weekday=True
Are_eligible=(is_student or is_senior) and is_weekday
print("Is the customer eligible for a discount?", Are_eligible)
