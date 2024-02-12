# This program uses if elif and else to show various error messages when user enters his name
# Get the full name from the user and store it in full_name variable
# Perform various checks on full_name and display print error messages accordingly or if user
# enters correctly print Thank you for entering full name message. len method of string is used
# to check length of full_name for displaying error messages

full_name = input("Please enter your full name: ")
if (len(full_name) == 0):
    print("You have not entered anything. Please enter a full name.")
elif(len(full_name) < 4):
    print('''You have entered less than 4 characters. Please make sure that you have entered your name and surname.''')
elif(len(full_name) > 25):
    print("You have entered more than 25 characters. Please make sure you have entered only your full name.")
else:
    print("Thank you for entering your name.")