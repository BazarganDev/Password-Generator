# Secure Password Generator
# Usable for security purposes and cryptography

# Import modules
import secrets
import string

# Define data
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation
SEQUENCE = LETTERS + NUMBERS + PUNCTUATIONS

def Generate_Password():
	"""Generate secure password"""
    # Password info
	password = ""

	# Check the data given to "password_length"
	while True:
		password_length = input("\n* Password length => ")
		if password_length.isdigit():
			break
		else:
			ERROR_MSG = "Please enter a number for length\n"
			print(ERROR_MSG)

	password += "".join(secrets.choice(SEQUENCE) for character in range(int(password_length)))
	# Generate
	print(f"Your password => {password}")
	input("\nPress any key to quit...")

# Start programmer
print(" _____________________________________ ")
print("| Welcome to                          |")
print("| Secure Password Generator           |")
print("|__________________  _________________|")
print("                   \ \                 ")
print("                    ^_ _^              ")
print("                    (o o)\_________    ")
print("                    (_ _)\         )/\/")
print("                      U   ||----W||    ")

def main():
    Generate_Password()

main()