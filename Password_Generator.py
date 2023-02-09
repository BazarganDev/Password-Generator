# Password Generator
import random
import string

def GENERATE_PASSWORD():
	NUMBERS = string.digits
	ALPHABET = string.ascii_letters
	PUNCTUATION = string.punctuation
	SEQUENCE = NUMBERS + ALPHABET + PUNCTUATION

	PASSWORD = ""

	for character in range(30):
		character = random.choice(SEQUENCE)
		PASSWORD += character

	print(PASSWORD)

GENERATE_PASSWORD()