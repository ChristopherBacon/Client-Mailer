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

    ans=True
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
        elif ans == "2":
            search_clients = input('Search for a client group:')
            searched_clients = search_for_clients(clients_list, search_clients)
            for x in searched_clients:
                print(x)
        elif ans == "3":
            email_choice = input("Do you wish to choose an email or create random emails for clients? [1 or 2]")
            if email_choice == "1":
                pass
            elif email_choice == "2":
                pass

            check_emails()
            print(check_emails())
        elif ans == "4":
            pass
        elif ans == "5":
            break
        else:
            break





        break









if __name__ =="__main__":
    main()