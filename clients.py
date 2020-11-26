"""
Create clients
"""

"""
TO DO:
include email history that have been sent to Clients

"""

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


def open_client_file():
    """ Opens csv of clients, converts to dictionary by csv fields. """
    clients_dict = []
    file = open('clients.csv', encoding='utf-8-sig')
    client_ordered_dict = csv.DictReader(file)

    for row in client_ordered_dict:
        clients_dict.append({
            'First': row['First Name'],
            'Last': row['Last Name'],
            'Company': row['Account Name'],
            'Email': row['Email'],
            'Job': row['Job']
        })
    return clients_dict

def create_client_from_dict():
    """ Creates Client class from the dictionary of clients"""
    client_data = []
    for row in open_client_file():
        client_data.append(Client(row['First'], row['Last'], row['Job'], row['Company'], row['Email']))
    return client_data

def search_for_clients(client_list, search_term):
    """ Search for clients from client_list"""
    matched_clients = []
    for client in client_list:
        if client.first == search_term or client.last == search_term or \
                client.job == search_term or client.company == search_term:
            matched_clients.append(client)
    return matched_clients

def print_clients(client_list):
    """ Print clients in client_list"""
    if len(client_list) == 0:
        print("Please try again, your list has no clients.")
    else:
        for client in client_list:
            print(client)


def main():
    clients_from_itv = search_for_clients(create_client_from_dict(), "ITV")
    print_clients(clients_from_itv)
    print(open_client_file())
    print(create_client_from_dict())


if __name__ == "__main__":
    main()
