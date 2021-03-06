"""
PROJECT: Client Mailer
mail templates - a collection of emails to randomise and send to clients
clients - Manage a client database, also client stats (stretch)
mailer - Sent bulk mails with different content

Notes: This version is set up with the debug server from smtp
Set up server: python -m smtpd -c DebuggingServer -n localhost:1025
"""

"""
TO DO:
create scheduler to determine mail send times and dates
Pull functions from mailtemplates & clients into main delivery thread
Write tests
"""
import smtplib


from clientmailerproj.clients import create_client_from_dict
from clientmailerproj.mailtemplates import fstring_place_holders, check_emails

def bulk_send(chosen_clients, chosen_mail_template):
    port = 1025  # For debug server
    smtp_server = 'localhost'
    sender_email = "salesy@gmail.com"

    for client in chosen_clients:
        receiver_email = client.email
        msg = fstring_place_holders(f'../emails/{chosen_mail_template[0]}')
        print(msg)
        server = smtplib.SMTP(smtp_server, port)
        server.sendmail(sender_email, receiver_email, msg.format(first=client.first))
        server.quit()







