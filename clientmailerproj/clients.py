"""
Create clients
"""

"""
TO DO:
include email history for clients

"""

import csv

# clients go here from create client from list func
clients_list = []

class Client:
    """ client class, create clients."""

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
        return f"Name: {self.first} {self.last} Job: {self.job} Company: {self.company} email: {self.email}"

    def __repr__(self):
        """ Returns class object details"""
        return f"Name: {self.first} {self.last} Job: {self.job} Company: {self.company} email: {self.email}"


def open_client_file_to_dict():
    """ Opens csv of clients, converts to dictionary by specified csv fields. """
    clients_dict = []
    file = open(r'../clientmailerproj/client.csv', encoding='utf-8-sig')
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
    for row in open_client_file_to_dict():
        clients_list.append(Client(row['First'], row['Last'], row['Job'], row['Company'], row['Email']))
    return

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
        return
    else:
        for client in client_list:
            print(client)
    return



# open_client_file_to_dict()
# create_client_from_dict()
# print(search_for_clients(clients_list, r'BBC'))
# print(clients_list)