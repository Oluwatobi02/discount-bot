from app.user_activity import UserActivity
import ipaddress
class UserActivityBuilder:
    def __init__(self):
        self.user_activity = UserActivity()

    def add_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            self.user_activity.set_ip(ip)
            return self
        except ValueError:
            return None
    def add_action(self, action):
        self.user_activity.set_action(action)
        return self
    def add_metadata(self, metadata):
        self.user_activity.set_metadata(metadata)
        return self
    def add_user(self, user):
        self.user_activity.set_user(user)
        return self
    def add_device(self, device):
        self.user_activity.set_device(device)
        return self
    def add_timestamp(self, timestamp):
        self.user_activity.set_timestamp(timestamp)
        return self
    def build(self):
        return self.user_activity
    