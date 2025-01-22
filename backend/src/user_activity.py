from src.lib.ip_addr import get_ip_info

class UserActivity:
    def __init__(self):
        self.ip = None
        self.city = None
        self.device = None
        self.country = None
        self.type = None
        self.zip = None
        self.user = None
        self.action = None
        self.timestamp = None
        self.metadata = {}

    def __str__(self):
        return f"UserActivity(ip={self.ip}, city={self.city}, country={self.country}, zip={self.zip}, type={self.type}, user={self.user}, action={self.action}, timestamp={self.timestamp})"
    def __repr__(self):
        return self.__str__()
    
    def set_user(self, user):
        self.user = user

    def set_ip(self, ip):
        self.ip = ip
        ip_info = get_ip_info(self.ip)
        self.city = ip_info.get("city")
        self.country = ip_info.get("country")
        self.zip = ip_info.get("zip")
        self.type = ip_info.get("type")

    def set_device(self, device):
        self.device = device
    def set_metadata(self, metadata={}):
        self.metadata = metadata
        return self

    def set_action(self, action):
        self.action = action
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
    def to_dict(self):
        return {
            "ip": self.ip,
            "city": self.city,
            "country": self.country,
            "zip": self.zip,
            "type": self.type,
            "device": self.device,
            "user": self.user,
            "action": self.action,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }