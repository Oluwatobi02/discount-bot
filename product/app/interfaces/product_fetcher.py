from abc import ABC, abstractmethod

class IProductFetcher(ABC):
    name = None
    url = None
    headers = None
    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def format_product(self):
        pass