"""
Simple tests for mailer
"""


from clientmailerproj.clients import create_client_from_dict
from clientmailerproj.mailtemplates import fstring_place_holders, check_emails
from clientmailerproj.mailer import bulk_send

def test_bulk_send():
    email = bulk_send()
    assert email
