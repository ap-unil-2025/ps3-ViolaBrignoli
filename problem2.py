"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return(celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    print("Temperature Converter")
    print("-" * 30)
    temp_input = input("Give me a temperature: ").strip()
    try:
        temp = float(temp_input)
    except ValueError:
        print("Invalid temperature value. Please enter a numeric value.")
        return
    unit = input("What is the current unit? (C/F or Celsius/Fahrenheit): ").strip().lower()
    if unit in ("c", "celsius"):
        new_temp = celsius_to_fahrenheit(temp)
        print(f"The temperature you inserted was {temp:.2f}°C and we converted it to {new_temp:.2f}°F")
    elif unit in ("f", "fahrenheit"):
        new_temp = fahrenheit_to_celsius(temp)
        print(f"The temperature you inserted was {temp:.2f}°F and we converted it to {new_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' (Celsius) or 'F' (Fahrenheit).")
        return

    
    #TODO: Implement the interactive converter
    #Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    pass 


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()