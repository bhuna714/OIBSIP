def calculate_bmi():
    print("Welcome to the BMI Calculator!")
    
    # Get user input for weight and height
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"
    
    # Display the result
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

# Call the function
calculate_bmi()