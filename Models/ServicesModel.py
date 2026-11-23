from abc import ABC, abstractmethod

class Services(ABC):

    def __init__(self, Name, Base_price, Availability, Description,TypeService,Date):
        self.Name = Name
        self.Base_price = Base_price
        self.Availability = Availability
        self.Description = Description
        self.TypeService = TypeService

    @abstractmethod
    def calculate_cost(self):
        pass
    
    @abstractmethod
    def describe_service(self):
        pass

    @abstractmethod
    def validate_parameters(self):
        pass