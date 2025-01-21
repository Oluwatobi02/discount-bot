from app.factories.notification_factory.email import EmailClient
from app.factories.notification_factory.sms import SMSClient

class NotificationFactory:
    @staticmethod
    def get_notification_client(noti_client):
        """
        ONLY TWO TYPES OF clients
        PASS IN "email" or "sms"
        """
        if noti_client == "email":
            return EmailClient()
        if noti_client == "sms":
            return SMSClient()
        else:
            raise ValueError("Unknown notification type")
