"""
PROJECT
Client Mailer
Small CRM
emailer
"""


'''
JOBS
1. Get Client Data
2. create client class
3. test send email
4. create library of email messages
5. create scheduler to determine mail send.

'''
import csv


class Client():
    """ Client class, create clients."""

    def __init__(self, first, last, job, company, email, replies=0, searches=0):
        self.first = first
        self.last = last
        self.job = job
        self.company = company
        self.email = email
        self.replies = replies
        self.searches = searches

    def __str__(self):
        """ Returns client object as client detail """
        return f"Name: {self.first} {self.last} \
            Job: {self.job} \
            Company: {self.company} \
            email: {self.email}"


def search_for_clients(client_list, search_term):
    matched_clients = []
    for client in client_list:
        if client.first == search_term or client.last == search_term or \
                client.job == search_term or client.company == search_term:
            matched_clients.append(client)
    return matched_clients


clients_dict = []
def open_client_file():

    file = open('clients.csv', encoding='utf-8-sig')
    client_ordered_dict = csv.DictReader(file)

    for row in client_ordered_dict:
        clients_dict.append({
            'First' : row['First Name'],
            'Last' : row['Last Name'],
            'Company' : row['Account Name'],
            'Email' : row['Email'],
            'Job' : row['Job']
        })

def create_class_from_dict():
    for row in clients_dict:


def get_client_data():
    c1 = Client("Steve", "Winner", "Editor", "BBC", "steve.winner@bbc.co.uk")
    c2 = Client("John", "Baker", "Producer", "ITV", "john.baker@itv.com", 1, 0)
    c3 = Client("Isabelle", "Smith", "Promo Producer", "ITV", "isabelle.smith@itv.com")
    return [c1, c2, c3]


def print_clients(client_list):
    if len(client_list) == 0:
        print("Please try again, your search has returned no results.")
    else:
        for client in client_list:
            print(client)

def main():
    clients = get_client_data()
    clients_from_itv = search_for_clients(clients, "ITV")
    print_clients(clients_from_itv)
    open_client_file()
    print(clients_dict)



if __name__ == "__main__":
    main()
