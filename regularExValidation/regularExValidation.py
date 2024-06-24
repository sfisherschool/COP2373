import re

def validate_phone_number(phone_number):
    # Phone number format: (123) 456-7890
    pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    return bool(pattern.fullmatch(phone_number))

def validate_social_security_number(ssn):
    # SSN format: 123-45-6789
    pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
    return bool(pattern.fullmatch(ssn))

def validate_zip_code(zip_code):
    # Zip code format: 12345 or 12345-6789
    pattern = re.compile(r'\d{5}(-\d{4})?')
    return bool(pattern.fullmatch(zip_code))

def main():
    # Get user input for phone number, ssn, and zip
    phone_number = input("Enter a phone number: ")
    ssn = input("Enter a social security number: ")
    zip_code = input("Enter a zip code: ")

    # Call the validation functions and display the correct message to user
    if validate_phone_number(phone_number):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid. Please use the following format: ")
        print("(123) 456-7890")

    if validate_social_security_number(ssn):
        print("The social security number is valid.")
    else:
        print("The social security number is invalid. Please use the following format: ")
        print("123-45-6789")

    if validate_zip_code(zip_code):
        print("The zip code is valid.")
    else:
        print("The zip code is invalid. Please use the following format: ")
        print("12345 or 12345-6789")

main()
