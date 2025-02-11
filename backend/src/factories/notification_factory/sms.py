from __future__ import print_function
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException
from dotenv import load_dotenv

import os
import clicksend_client

load_dotenv("shared.env")

class SMSClient:

    configuration = clicksend_client.Configuration()
    configuration.username = os.getenv("CLICKSEND_USERNAME")
    configuration.password = os.getenv("CLICKSEND_PASSWORD")
    sms_api = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    contact_api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
    contact_list_api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))

    def send_message(self, to, message):
        sms_message = SmsMessage(source="python",
                                body=message,
                                to=to,
                                )

        sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

        try:
            # Send sms message(s)
            api_response = self.sms_api.sms_send_post(sms_messages)
            print(api_response)
        except ApiException as e:
            print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
            
            
    def add_new_contact_to_list(self, contact):  
        contact = clicksend_client.Contact(
                phone_number=contact.phone_number,
                first_name=contact.name,
                email=contact.email,
                ) # Contact | Contact model
        list_id = self.list_id # int | List id

        try:
            # Create new contact
            api_response = self.api_instance.lists_contacts_by_list_id_post(contact, list_id)
            print(api_response)
        except ApiException as e:
            print("Exception when calling ContactApi->lists_contacts_by_list_id_post: %s\n" % e)