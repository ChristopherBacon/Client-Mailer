"""
PROJECT: Client Mailer
mail templates - a collection of emails to randomise and send to clients
clients - Manage a client database, also client stats (stretch)
mailer - Sent bulk mails with different content

Notes: This version is set up with the debug server from smtp
"""

"""
TO DO:
create scheduler to determine mail send times and dates
Pull functions from mailtemplates & clients into main delivery thread
Write tests
"""


import smtplib


from clients import create_client_from_dict
from mailtemplates import fstring_place_holders, check_emails


def bulk_send():
    client_data = create_client_from_dict()
    port = 1025  # For debug server
    smtp_server = 'localhost'
    sender_email = "my@gmail.com"

    for client in client_data:
        receiver_email = client.email
        msg = fstring_place_holders()
        server = smtplib.SMTP(smtp_server, port)
        server.sendmail(sender_email, receiver_email, msg.format(first=client.first))
        server.quit()


def main():
    bulk_send()
    print(check_emails())

if __name__ == '__main__':
    main()




