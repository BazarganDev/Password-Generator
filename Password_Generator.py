# Password Generator
import random
import string

def GENERATE_PASSWORD():
	""" Generate a password with combination of numbers, letters(uppercase & lowercase) and punctuations."""
	NUMBERS = string.digits
	ALPHABET = string.ascii_letters
	PUNCTUATION = string.punctuation
	SEQUENCE = NUMBERS + ALPHABET + PUNCTUATION

	password = ""
	# Select 30 characters from the combined sequence
	for character in range(30):
		character = random.choice(SEQUENCE)
		password += character

	print(password)

GENERATE_PASSWORD()
