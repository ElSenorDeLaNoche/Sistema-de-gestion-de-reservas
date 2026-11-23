from Models.ServicesModel import Services
from datetime import datetime
import random

class ConsultingServices(Services):
    __Consulting = {
     "Service_id":[],
     "Name":[],
     "Description":[],
     "Availability":[],
     "Base_price":[],
     "Discount":[],
     "TypeService":[],
     "Impuesto":[],
     "Specialization_area":[]
    }
    __Impuesto = 5

    def __init__(self, Name=None, Base_price=None, Availability=None, Description=None, Discount=None, TypeService=None, Specialization_area=None):
        super().__init__(Name, Base_price, Availability, Description, TypeService, Date=None)
        if Name == None:
            return
        
        self.validate_parameters(Name, Base_price, Availability, Description, Discount, TypeService, Specialization_area)

    def calculate_cost(self, Time, Discount):
        Subtotal = Time * self.Base_price
        Total = (Subtotal - Subtotal * (Discount/100)) + (Subtotal *(self.__Impuesto/100))
        return Total
    
    
    def describe_service(self):
        return self.__Consulting


    def validate_parameters(self, Name, Base_price, Availability, Description, Discount, TypeService, Specialization_area):

        Message = ""
        try:
            # Validar Descuento

            if not isinstance(Discount, (int, float)):
                Message = "El Descuento base debe ser un valor numérico y Mayor a 0."
                raise Exception()

            # Validar Name

            if not isinstance(Name, str) or not Name.strip():
                Message = "El nombre debe contener informacion y ser un texto."
                raise Exception()

            # Validar Base_price

            if not isinstance(Base_price, (int, float)) or Base_price <= 0:
                Message = "El precio base debe ser un valor numérico Mayor a 0."
                raise Exception()

            # Validar Availability

            if not isinstance(Availability, bool):
                Message = "La disponibilidad debe ser True o False."
                raise Exception()

            # Validar Description

            if not isinstance(Description, str) or not Description.strip():
                Message = "La descripción debe contener informacion y debe ser un texto."
                raise Exception()

            # Validar TypeService

            if not isinstance(TypeService, str):
                Message = "El tipo de servicio debe ser un texto."
                raise Exception()


            # Validar Specialization_area

            if not isinstance(Specialization_area, str) or not Specialization_area.strip():
                Message = "El área de especialización debe Contener informacion y debe ser un texto."
                raise Exception()
            

            self.__Insertion(Name, Availability, Base_price,Discount, Specialization_area, Description, TypeService)

        except Exception:
            return(False,Message)
            
    def __Insertion(self,Name,Availability,Base_price,Discount,Specialization_area, Description,TypeService):
        try:
            ID_service = str(random.randint(10000, 999999999)) + TypeService
            while ID_service in self.__Consulting["Service_id"]:
                ID_service = str(random.randint(10000, 999999999)) + TypeService

            
            self.__Consulting["Service_id"].append(ID_service)
            self.__Consulting["Name"].append(Name)
            self.__Consulting["Description"].append(Description)
            self.__Consulting["Availability"].append(Availability)
            self.__Consulting["Base_price"].append(Base_price + (Base_price* (self.__Impuesto/100)))
            self.__Consulting["Discount"].append(Discount)
            self.__Consulting["TypeService"].append("Asesoria")
            self.__Consulting["Impuesto"].append(self.__Impuesto)
            self.__Consulting["Specialization_area"].append(Specialization_area)
            (True, "Servicios creado correctamente")
        except ValueError :
            (False,"Error: Hubo un error al momento de registrar el servicio")

