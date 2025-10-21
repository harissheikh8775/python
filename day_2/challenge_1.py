# BMI Calculator
"""The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. 
This is the formula used to calculate it:
bmi is equal to the person's weight divided by the person's height squared.
Convert this sentence into code on line 6."""

height=float(input("Please enter your height:\n"))
weight=int(input("Please enter your weight:\n"))

bmi=weight//(height**2)
print(bmi)