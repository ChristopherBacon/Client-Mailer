"""
Simple tests for mailer
"""
import pytest
from unittest import mock

from clientmailerproj.clients import create_client_from_dict
from clientmailerproj.mailtemplates import fstring_place_holders, check_emails
from clientmailerproj.mailer import bulk_send
import smtplib

#This needs fixing, unsure how to mock this server? Need to find out return values from SMTP modules
# @mock.patch('clientmailerproj.mailer.quit')
# @mock.patch('clientmailerproj.mailer.smtplib.SMTP.sendmail')
# @mock.patch('clientmailerproj.mailer.smtplib.SMTP')
# def test_bulk_send(mock_smtplib_SMTP, mock_sendmail, mock_quit):
#     client_data = create_client_from_dict()
#     port = 1025  # For debug server
#     smtp_server = 'localhost'
#     sender_email = "my@gmail.com"
#     receiver_email = 'test@receivermail.com'
#     msg = 'hello_world'
#
#     mock_smtplib_SMTP.return_value = [smtp_server, port]
#     mock_sendmail.return_value = [sender_email, receiver_email, msg]
#     mock_quit.return_value = [None]
#
#     server = mock_smtplib_SMTP(smtp_server, port)
#     server.mock_sendmail(sender_email, receiver_email, msg)
#     server.mock_quit()
#
#     assert bulk_send() == test_bulk_send()

