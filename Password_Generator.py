from random import randrange as rand
# randrange generates a random number 
# see more: https://www.geeksforgeeks.org/randrange-in-python/ 
from pyperclip import copy
#importing pyperclip to copy obtained password in clipboard.

#GeneratePassword function takes 5 arguments and returns password.
# Out of 5, 4 are 'True' by default.
def GeneratePassword(length,Uppercase=True,lowercase=True,Numbers=True,Specialchar=True):

	# Checking if all choices are edited to False. 
	if True not in [Uppercase,lowercase,Specialchar,Numbers]:
		print(" -----------------------------------------------------")
		print(" WARNING: ERROR- All choices has been changed to False")
		print(" -----------------------------------------------------")
		raise ValueError(" All choices has been changed to False")

	password = '' # empty password string

	# Defining alphabet, numbers and specialchar
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	numbers = "1234567890"
	specialchar ="!@#$%^&*()_+-=[]:;.><,/"

	while length>0:

		probability = rand(0,10) # probability

		if probability <= 2.5 and lowercase: 
			password += alphabet[rand(0,len(alphabet))]
			length -= 1

		elif probability <= 5 and probability > 2.5 and Uppercase:
			password += alphabet[rand(0,len(alphabet))].upper()
			length -= 1

		elif probability <= 7.5 and probability > 5 and Numbers:
			password += numbers[rand(0,len(numbers))]
			length -= 1

		elif probability <=10 and probability >7.5 and Specialchar:
			password += specialchar[rand(0,len(specialchar))]
			length -= 1

		else: #This line doesn't matter but it look sexy. 
			pass
	
	copy(password)
	return password #returning the final password

# Defining the 'main()' function

def main():

	'''#taking user's input until entered length satisfied criteria. 
	while True:
		l = int(input("\n Enter the Length of the password: "))
		if l<10 :
			print("\n length of the password is small. Re-enter the length.\n")
		else:
			break

	#'choicesBoolean' is list of booleans repective to 'Choice' list
	choicesBoolean = [True,True,True,True] # Default is 'all True'
	Choices = ["Uppercase letters","Lowercase letters","Numbers","Special Characters"]

	print("\n______________________________________________________\n")
	#Asking for user's choice. 
	if input("\n Do you want to customize it? (y/n): ") in 'yY':

		# Editing 'choicesBoolean' w.r.t. user's choice.'
		for i in range(len(Choices)):

			while True:
				choice = input(f" -----> Do you want {Choices[i]} in it? (y/n): ")

				if choice in 'Nn': #if user doesn't want it, updating 'choicesBoolean'
					choicesBoolean[i] = False
					break
				elif choice in 'Yy':
					break
				else:
					print("\n !!! Wrong choice. !!! \n")

		# Raising ValueError if all choices in 'choicesBoolean' has been changed as False.			
		if True not in choicesBoolean:
			print(" -----------------------------------------------------")
			print(" WARNING: ERROR- All choices has been changed to False")
			print(" -----------------------------------------------------")
			raise ValueError("All choices has been changed to False")

	# using defalut 'choicesBoolean'
	else:
		print("\n -------> Using Default settings <------")

	Getpassword = GeneratePassword(l,*choicesBoolean)
	print("\n ____________________________________________________\n")
	print(f" Generated Password : {Getpassword} \n") #printing final password
	print("\n ____________________________________________________")'''
	pass

# checking if __name__ == '__main__'
if __name__ == '__main__':
	main()  # Run main 