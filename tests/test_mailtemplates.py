"""
Tests for mail templates
"""
import os
import pytest

from clientmailerproj.mailtemplates import check_emails, random_email_generator, \
    open_email_file, fstring_place_holders


@pytest.fixture
def email_templates():
    path = r'/Users/christopherbacon/Documents/Python Scripts/ClientMailer/emails'
    list_of_emails = os.listdir(path)
    try:
        list_of_emails.remove('.DS_Store')
    except:
        list_of_emails

    return list_of_emails

def test_check_emails(email_templates):
    assert check_emails() == email_templates

def test_random_email_generator(email_templates):
    assert random_email_generator() in email_templates

def test_open_email_file():
    actual = open_email_file(r'./emails/test_mail.txt')

    email_content = """Hi,

This is the test email.

Best,
administrator"""

    assert print(actual) == print(email_content)

def test_fstring_place_holders():
    email = r'./emails/test_mail.txt'
    actual = fstring_place_holders(email)
    test_copy = """Hi {first},

This is the test email.

Best,
administrator"""
    assert print(actual) == print(test_copy)