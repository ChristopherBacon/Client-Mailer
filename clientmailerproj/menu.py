"""
Run the mail program from start to finish
"""

from clientmailerproj.clients import *
from clientmailerproj.mailtemplates import *
from clientmailerproj.mailer import *


def menu():
    chosen_clients = []
    chosen_mail_template = []

    choice = True
    while choice:

            print('Please select option:')
            print("""
                    1. Add client(s)
                    2. Select client(s)
                    3. Select mail template
                    4. Send mail
                    5. Quit
                    """)

            choice = input("please make a selection:")

            if choice == '1':
                    print('Please enter client details:')
                    first = input('first:')
                    last = input('last:')
                    job = input('job:')
                    company = input('company:')
                    email = input('email:')
                    clients_list.append(Client(first, last, job, company, email))

            if choice == '2':
                client_searched = input('please enter search term:')
                results = search_for_clients(clients_list, client_searched)
                while len(results) == 0:
                    print('please try again, your search returned no results')
                    client_searched = input('please enter search term:')
                    results = search_for_clients(clients_list, client_searched)
                else:
                    for x in results:
                        chosen_clients.append(x)
                    print(results)

            if choice == '3':
                first_email_choice = input('select a mail template or make a random choice [1-2]:')
                if first_email_choice == '1':
                    email_selection = {i: check_emails()[i] for i in range(0, len(check_emails()))}
                    print(email_selection)
                    i = int(input('pick an email number:'))
                    print(email_selection[i])
                    chosen_mail_template.append(email_selection[i])
                if first_email_choice == '2':
                    selected_template = random_email_generator()
                    chosen_mail_template.append(selected_template)
                    print(selected_template)

            if choice == '4':
                print(f'Your email selection: {chosen_mail_template}')
                print(f'Your client selection:{chosen_clients}')
                bulk_send(chosen_clients, chosen_mail_template)




def main():
    open_client_file_to_dict()
    create_client_from_dict()
    menu()

if __name__ =="__main__":
    main()