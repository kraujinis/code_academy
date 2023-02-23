# Create a database (List of privileged users) print a specific 
# message with a personal greeting if the user is a privileged
#  and just "Welcome otherwise"

user = input("Who you are (name) ? ")

privileged_users = ['Darius', 'Laura', 'Dainius', 'Rūta']

if user in privileged_users:
    print("You are in privileged user list! ")
else:
    print("Sorry, go away! ")