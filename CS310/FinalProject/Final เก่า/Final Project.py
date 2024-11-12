# Unit Converter Program with Logging and Additional Conversions

def log_conversion(conversion_type, input_value, output_value, units):
    """Log the conversion details to a TXT file."""
    with open("conversion_history.txt", "a") as file:
        file.write(f"{conversion_type}: {input_value} -> {output_value} {units}\n")
    print("Conversion logged successfully.")

def view_conversion_history():
    """Display the conversion history from the TXT file."""
    try:
        with open("conversion_history.txt", "r") as file:
            history = file.readlines()
            if history:
                print("\nConversion History:")
                for line in history:
                    print(line.strip())
            else:
                print("\nNo conversion history available.")
    except FileNotFoundError:
        print("\nNo conversion history available. The file does not exist yet.")

def convert_length():
    print("Length Conversion")
    print("1: Meters to Kilometers")
    print("2: Meters to Feet")
    print("3: Meters to Inches")
    choice = input("Choose a conversion option (1-3): ")

    if choice == "1":
        meters = float(input("Enter meters: "))
        kilometers = meters / 1000
        print(f"{meters} meters is {kilometers} kilometers.")
        log_conversion("Length", meters, kilometers, "kilometers")
    elif choice == "2":
        meters = float(input("Enter meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is {feet} feet.")
        log_conversion("Length", meters, feet, "feet")
    elif choice == "3":
        meters = float(input("Enter meters: "))
        inches = meters * 39.3701
        print(f"{meters} meters is {inches} inches.")
        log_conversion("Length", meters, inches, "inches")
    else:
        print("Invalid choice.")

def convert_weight():
    print("Weight Conversion")
    print("1: Grams to Kilograms")
    print("2: Grams to Pounds")
    choice = input("Choose a conversion option (1-2): ")

    if choice == "1":
        grams = float(input("Enter grams: "))
        kilograms = grams / 1000
        print(f"{grams} grams is {kilograms} kilograms.")
        log_conversion("Weight", grams, kilograms, "kilograms")
    elif choice == "2":
        grams = float(input("Enter grams: "))
        pounds = grams * 0.00220462
        print(f"{grams} grams is {pounds} pounds.")
        log_conversion("Weight", grams, pounds, "pounds")
    else:
        print("Invalid choice.")

def convert_temperature():
    print("Temperature Conversion")
    print("1: Celsius to Fahrenheit")
    print("2: Celsius to Kelvin")
    choice = input("Choose a conversion option (1-2): ")

    if choice == "1":
        celsius = float(input("Enter Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")
        log_conversion("Temperature", celsius, fahrenheit, "Fahrenheit")
    elif choice == "2":
        celsius = float(input("Enter Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} Celsius is {kelvin} Kelvin.")
        log_conversion("Temperature", celsius, kelvin, "Kelvin")
    else:
        print("Invalid choice.")

def convert_speed():
    print("Speed Conversion")
    print("1: Kilometers per hour to Meters per second")
    print("2: Meters per second to Kilometers per hour")
    choice = input("Choose a conversion option (1-2): ")

    if choice == "1":
        kmph = float(input("Enter speed in km/h: "))
        mps = kmph * (1000 / 3600)
        print(f"{kmph} km/h is {mps} m/s.")
        log_conversion("Speed", kmph, mps, "m/s")
    elif choice == "2":
        mps = float(input("Enter speed in m/s: "))
        kmph = mps * (3600 / 1000)
        print(f"{mps} m/s is {kmph} km/h.")
        log_conversion("Speed", mps, kmph, "km/h")
    else:
        print("Invalid choice.")

def convert_area():
    print("Area Conversion")
    print("1: Square meters to Square centimeters")
    print("2: Square meters to Square feet")
    choice = input("Choose a conversion option (1-2): ")

    if choice == "1":
        sq_meters = float(input("Enter area in square meters: "))
        sq_centimeters = sq_meters * 10000
        print(f"{sq_meters} m² is {sq_centimeters} cm².")
        log_conversion("Area", sq_meters, sq_centimeters, "cm²")
    elif choice == "2":
        sq_meters = float(input("Enter area in square meters: "))
        sq_feet = sq_meters * 10.7639
        print(f"{sq_meters} m² is {sq_feet} ft².")
        log_conversion("Area", sq_meters, sq_feet, "ft²")
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\nUnit Converter")
        print("1: Length Conversion")
        print("2: Weight Conversion")
        print("3: Temperature Conversion")
        print("4: Speed Conversion")
        print("5: Area Conversion")
        print("6: View Conversion History")
        print("7: Exit")
        option = input("Choose an option (1-7): ")

        if option == "1":
            convert_length()
        elif option == "2":
            convert_weight()
        elif option == "3":
            convert_temperature()
        elif option == "4":
            convert_speed()
        elif option == "5":
            convert_area()
        elif option == "6":
            view_conversion_history()
        elif option == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the main function
main()