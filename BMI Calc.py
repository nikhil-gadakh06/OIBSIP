# BMI CALCULATOR PYTHON PROGRAM

the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  

#BMI calculation
the_BMI = the_weight / (the_height/100)**2  

print("Your Body Mass Index is", the_BMI)  

if the_BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif the_BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif the_BMI <= 29.9:  
    print("You are over weight.")  
else:  
    print("You are obese.")  