import re
import glob
import os
import random

"""
TO DO:
- Expand check_emails() by using folders for specific industry types
- include random email generation across groups, also check to see emails that have been received during a timeframe and 
exclude those templates
- Open email file could be used to check content of email for errors, A safety net before sending
"""



def check_emails():
    """ check emails in file"""
    emails = glob.glob("emails/*.txt")
    email_list = []
    for email in emails:
        email = os.path.basename(email)
        email_list.append(email)
    return email_list


def random_email_generator():
    """ Selects random email from email templates"""
    email_list = check_emails()
    email_selection = []
    for i, email in enumerate(email_list, start=1):
        email_selection.append((i, email))

    random_mail = random.choice(email_selection)
    return random_mail[1]


def open_email_file():
    """ Open email template """
    with open(r'./emails/intro email.txt', "r") as file:
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


def main():
    check_emails()
    print(random_email_generator())


if __name__ == '__main__':
    main()