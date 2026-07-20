print("DAY 5") #lets dive into if-else logic
print("Begineer fitness and Health calculator")
weight =float(input("Enter your weight in kg: "))
height_cm =float(input ("Enter your height in cm:"))
height_m= height_cm / 100
bmi = weight / (height_m * height_m   """ bmi=body mass index(estimates a person's body fat
                                          based on their height and weight)
print("your bmi is:")
print(bmi)
if bmi < 18.5:
    print("Result: Underweight")
    print("Tip: Eat more nutrient-dense food.")

elif bmi < 24.9:
    print("Result: Normal weight")
    print("Tip: Keep up the great work!")

elif bmi < 29.9:
    print("Result: Overweight")
    print("Tip: Try to exercise more and watch portions.")

else:
    print("Result: Obese")
    print("Tip: Talk to a doctor for advice.")
