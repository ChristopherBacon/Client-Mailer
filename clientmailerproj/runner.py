"""
Run the mail program from start to finish
"""

from clientmailerproj.clients import *
from clientmailerproj.mailtemplates import *
from clientmailerproj.mailer import *



def main():
    print('Loading client csv')
    open_client_file_to_dict()
    create_client_from_dict()
    print('csv loaded')
    print(clients_list)
    #print(search_for_clients(clients_list, 'BBC'))


    clients_to_email = []
    selected_template = []

    ans = True
    while ans:
        print('Please select option:')
        print("""
        1. Add client(s)
        2. Select client(s)
        3. Select mail template
        4. Send Mail
        5. Quit
        """)
        ans = input('Please select an option [1-5]:')

        if ans == "1":
            print('Please enter client details:')
            first = input('first:')
            last = input('last:')
            job = input('job:')
            company = input('company:')
            email = input('email:')
            clients_list.append(Client(first, last, job, company, email))

        # elif ans == "2":
        #     # input search terms for clients
        #     search_clients = input('Search for a client group:')
        #     # function from clients.py returns list
        #     searched_clients = search_for_clients(clients_list, search_clients)
        #     clients_to_email = searched_clients
        #     print(clients_to_email)
        #     if len(searched_clients) > 0:
        #         break
        #     else:
        #     # if search is 0, repeat search
        #         while len(clients_to_email) == 0:
        #             print('sorry no clients matched, try again')
        #             search_clients = input('Search for a client group:')
        #             searched_clients = search_for_clients(clients_list, search_clients)
        #
        #     print('clients to email:')
        #     #email list of clients to sent out
        #     clients_to_email = searched_clients
        #     for x in clients_to_email:
        #         print(x)
        #     continue

        # elif ans == "2":
        #     # input search terms for clients
        #     search_clients = input('Search for a client group:')
        #     # function from clients.py returns list
        #     searched_clients = search_for_clients(clients_list, search_clients)
        #     print(searched_clients)
        #     # if search is 0, repeat search
        #     while len(searched_clients) == 0:
        #         print('sorry no clients matched, try again')
        #         search_clients = input('Search for a client group:')
        #         searched_clients = search_for_clients(clients_list, search_clients)
        #     else:
        #         print('clients to email:')
        #         #email list of clients to sent out
        #         clients_to_email = searched_clients
        #         for x in clients_to_email:
        #             print(x)

        elif ans == '2':
            client_select = input('Enter search term to select clients:')
            print(search_for_clients(clients_list, client_select))
            break

        elif ans == "3":
            email_choice = input("Do you wish to choose an email or create random emails for clients? [1 or 2]")
            if email_choice == "1":
                email_selection = []
                email_list = check_emails()
                for i, email in enumerate(email_list, start=1):
                    email_selection.append((i, email))
                print(email_selection)
                template_selection = input('Choose a template to send: ')
                # Chosen email for mail send
                selected_template = email_selection[1-int(template_selection)][1]
                print(email_selection[1-int(template_selection)])
            elif email_choice == "2":
                selected_template = random_email_generator()
                print(selected_template)
            else:
                break

        elif ans == "4":
        # remember to ensure the debug server is running
            print('chosen clients:')
            print(clients_to_email)
            print('email template sending:')
            print(selected_template)
            clients = clients_to_email
            email_temp = selected_template
            bulk_send(clients, email_temp)
            clients_to_email.clear()
            selected_template = []
            print(selected_template)
            print(clients_to_email)


        elif ans == "5":
            print('Exiting')
            break
        else:
            break

if __name__ =="__main__":
    main()