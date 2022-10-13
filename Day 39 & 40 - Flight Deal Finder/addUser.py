from data_manager import DataManager

dataManager = DataManager()

def addUser():
    """Asks users details and add them into google sheet."""
    # asking first name, last name & email
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    email = input('Enter your email: ').lower()

    # basis email vailidation (not using regex)
    if '@' not in email:
        print(f'Invalid email!')
        return False

    # confirming email from user by asking email again
    confirmEmail = input('Enter your email again: ').lower()
    if email != confirmEmail:
        print('Confirm email is not correct!')
        return False

    # adding in google sheet
    added = dataManager.addUserToSheet(firstName=firstName, lastName=lastName, email=email)

    if added:
        print(f'Success! Your email has been added in the list.')


addUser()

