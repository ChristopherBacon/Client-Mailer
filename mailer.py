"""
Emailer: Send emails on mass from email templates. Drawing clients from ClientMailer
"""

import smtplib
import re

from ClientMailer import create_client_from_dict

#Opens a txt file to use for the email, need to work on and test format for this.
def open_email_file():
    """ Open email template """
    with open(r'emails/intro email.txt', "r") as file:
        email_copy = file.read()
        file.close()
    return email_copy

def fstring_place_holders():
    """ Insert f string formatting into template, first name"""
    email_content = open_email_file()
    first_name_space = r'[HhIi]+\s,'
    first_placeholder = r'Hi {first},'
    insert_first = re.sub(first_name_space, first_placeholder, email_content)
    return insert_first


def bulk_send():
    client_data = create_client_from_dict()
    port = 1025  # For SSL
    smtp_server = 'localhost'
    sender_email = "my@gmail.com"  # Enter your address

    for x in client_data:
        print(client_data['First'])

    msg = print(open_email_file())

    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(sender_email, receiver_email, msg)
    server.quit()





        #server.sendmail(
            #from_address,
            #email,
            #message.format(name=name, grade=grade),
        #)


    port = 1025  # For SSL
    smtp_server = 'localhost'
    sender_email = "my@gmail.com"  # Enter your address
    receiver_email = "your@gmail.com"  # Enter receiver address
    #password = input("Type your password and press enter: ")

    msg = print(open_email_file())

    server = smtplib.SMTP(smtp_server, port)
    server.sendmail(sender_email, receiver_email, msg)
    server.quit()

def main():
    print(open_email_file())
    print(open_client_file())
    print(place_holders())

if __name__ == '__main__':
    main()




