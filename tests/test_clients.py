"""
Simple Tests for client management system
"""

import pytest

from clientmailerproj.clients import Client, open_client_file_to_dict, create_client_from_dict, search_for_clients, \
print_clients

test_clients = [
    ("Jane", "Doe", "Producer", "NENT", "jane.doe@nent.com", 4, 2),
    ("John", "Baker", "ITV", "john.baker@itv.com", "Producer", 1),
    ("Isabelle", "Smith", "ITV",	"isabelle.smith@itv.com", "Promo Producer", 0, 3)
]

@pytest.fixture
def client():
    c1 = Client("Jane", "Doe", "Producer", "NENT", "jane.doe@nent.com", 4, 2)
    c2 = Client("John",	"Baker","ITV", "john.baker@itv.com", "Producer", 1)
    c3 = Client("Isabelle",	"Smith", "ITV",	"isabelle.smith@itv.com", "Promo Producer", 0, 3)
    return [c1,c2,c3]

@pytest.fixture
def client_list():
    client_list = [{'First': 'Steve', 'Last': 'Winner', 'Company': 'BBC', 'Email': 'steve.winner@bbc.co.uk', 'Job': 'Editor'},
                   {'First': 'Isabelle', 'Last': 'Smith', 'Company': 'ITV', 'Email': 'isabelle.smith@itv.com', 'Job': 'Promo Producer'}]
    return client_list

def test_client_jane(client):
    jane = client[0]
    jane.first == "Jane"
    jane.last == "Doe"
    jane.job == "Producer"
    jane.company == "NENT"
    jane.email == "jane.doe@nent.com"
    jane.searches == 2
    assert (jane.first, jane.last, jane.searches) == ("Jane", "Doe", 2)

def test_client_john(client):
    john = client[1]
    assert john.replies == 1

def test_client_isabelle(client):
    isabelle = client[2]
    isabelle.replies == 0
    isabelle.searches == 3
    assert (isabelle.replies, isabelle.searches) == (0,3)

def test_open_client_file():
    clients_dict = open_client_file_to_dict()
    steve = clients_dict[0]['First']
    steve_job = clients_dict[0]['Job']
    assert (steve, steve_job) == ('Steve', 'Editor')

def test_create_client_from_dict():
    test_client = create_client_from_dict()
    test_client = test_client[1]
    assert test_client.first == 'John'

def test_search_for_clients(client):
    isabelle_search = search_for_clients(client, "Isabelle")
    print(isabelle_search[0])
    assert isabelle_search[0].first == "Isabelle"


def test_print_clients_fail():
    empty_clients = []
    empty_print = print_clients(empty_clients)
    assert empty_print == None

