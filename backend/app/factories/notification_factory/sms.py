from __future__ import print_function
import os
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException
from dotenv import load_dotenv
load_dotenv()
class SMSClient:

# Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = os.getenv("CLICKSEND_USERNAME")
    configuration.password = os.getenv("CLICKSEND_PASSWORD")

# create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    def send_message(self, to, message):
    # If you want to explictly set from, add the key _from to the message.
        sms_message = SmsMessage(source="python",
                                body=message,
                                to=to,
                                )

        sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

        try:
            # Send sms message(s)
            api_response = self.api_instance.sms_send_post(sms_messages)
            print(api_response)
        except ApiException as e:
            print("Exception when calling SMSApi->sms_send_post: %s\n" % e)