# Password Generator
import random
import string

def GENERATE_PASSWORD():
	""" Generate a password with combination of numbers, letters(uppercase & lowercase) and punctuations."""
	NUMBERS = string.digits
	ALPHABET = string.ascii_letters
	PUNCTUATION = string.punctuation
	SEQUENCE = NUMBERS + ALPHABET + PUNCTUATION

	PASSWORD = ""
	# Select 30 characters from the combined sequence
	for character in range(30):
		character = random.choice(SEQUENCE)
		PASSWORD += character

	print(PASSWORD)

GENERATE_PASSWORD()
