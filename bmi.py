## 👤  Original BMI Calculator

def compute_body_mass_index(weight_kg: float, height_meters: float) -> float | str:
    """
    Calculates the Body Mass Index (BMI) using the standard formula.

    The formula is: weight (kg) / [height (m)]^2.

    Args:
        weight_kg: The user's weight in kilograms.
        height_meters: The user's height in meters.

    Returns:
        The calculated BMI as a float, or an error message as a string
        if the height input is invalid.
    """
    if height_meters <= 0:
        # Raise an exception for better error handling flow instead of returning a string.
        raise ValueError("Height must be a positive number to calculate BMI.")

    # Calculate BMI: weight / (height squared)
    bmi_score = weight_kg / (height_meters ** 2)
    return bmi_score

def determine_bmi_classification(bmi_value: float) -> str:
    """
    Classifies a person's weight status based on their calculated BMI score.
    Uses standard World Health Organization (WHO) adult categories.


[Image of WHO BMI chart]

    Args:
        bmi_value: The calculated Body Mass Index (BMI).

    Returns:
        A string representing the BMI classification (e.g., 'Normal Weight').
    """
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 25.0:
        return "Normal Weight"
    elif 25.0 <= bmi_value < 30.0:
        return "Overweight"
    else:
        # Handles BMI 30.0 and above
        return "Obese"

def run_bmi_analyzer():
    """
    A user-friendly function to collect input, calculate BMI, and display the result.
    It includes robust input validation.
    """
    print("\n--- ⚖️ Body Mass Index (BMI) Calculator ---")
    try:
        # Use descriptive input prompts
        user_weight = float(input("Please enter your weight in kilograms (e.g., 70.5): "))
        user_height = float(input("Please enter your height in meters (e.g., 1.75): "))

        # Compute the BMI, letting ValueError handle invalid height input
        final_bmi_score = compute_body_mass_index(user_weight, user_height)

        # Determine the category
        weight_status = determine_bmi_classification(final_bmi_score)

        # Display the results
        print("\n--- Results ---")
        print(f"Your calculated BMI is: **{final_bmi_score:.2f}**")
        print(f"Based on this score, your classification is: **{weight_status}**")
        print("-" * 15)

    except ValueError as e:
        # Catch errors from both float() conversion and compute_body_mass_index()
        print(f"\n❌ Error: Invalid input detected.")
        # 'e' contains the error message from the raised exception (if applicable)
        print(f"Details: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred: {e}")

# Call the analyzer directly for execution in Colab
run_bmi_analyzer()
