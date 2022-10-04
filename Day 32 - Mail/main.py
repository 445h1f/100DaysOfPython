import smtplib
import os

myEmail = input('Enter your hotmail email: ')

with smtplib.SMTP('smtp.office365.com', port=587) as connection:

    # adds transport layer security
    connection.starttls()
    password = input(f'Enter Password: ')
    os.system('cls')
    print('Logging in...')
    # login to email
    connection.login(user=myEmail, password=password)
    print('Logged in!')


    reciverEmail = input('Enter email address where you want so send E-mail: ')
    subject = input('Enter subject of Email: ')
    body = input('Enter body of Email: ')
    emailMessage = f'Subject:{subject}\n\n{body}'
    print(f'Sending Email...')

    # sending email
    connection.sendmail(
        from_addr=myEmail,
        to_addrs=reciverEmail,
        msg=emailMessage
    )
    print(f'Mail sent to {reciverEmail}')

    input('Press any key to log out...')

print(f'Logged Out!')
