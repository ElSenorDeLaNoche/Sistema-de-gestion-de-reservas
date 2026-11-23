from Models.ServicesModel import Services
import datetime, random


class EquipmentRental(Services):

    __EquipmentRental = {
        "Equipment_id": [],
        "Name": [],
        "Stock": [],
        "Description": [],
        "TypeEquipment": [],
        "Brand": [],
        "Condition": [],
        "Availability": [],
        "tax": [],
        "TypeService": [],
        "PriceHour": [],
        "Discount": []
    }

    __tax = 9

    def __init__(self,Name=None,PriceHour=None,Availability=None,Description=None,TypeService=None,Date=None,Brand=None,Stock=None,Condition=None,TypeEquipment=None,Discount=None):
        super().__init__(Name,PriceHour,Availability,Description,TypeService,Date)

        if Name == None:
            return

        self.validate_parameters(Name,PriceHour,Availability,Description,TypeService,Date,Brand,Stock,Condition,TypeEquipment,Discount)

    def calculate_cost(self):
        pass

    def describe_service(self):
        return self.__EquipmentRental

    def validate_parameters(self,Name,PriceHour,Availability,Description,TypeService,Date,Brand,Stock,Condition,TypeEquipment,Discount):
        Message = ""

        try:

            # Validar Stock
            if not isinstance(Stock, int) or Stock < 0:
                Message = "La cantidad de equipos no debe ser un número entero menor a 0."
                raise Exception()

            # Validar Name
            if not isinstance(Name, str) or not Name.strip():
                Message = "El nombre debe contener información y ser un texto."
                raise Exception()

            # Validar PriceHour
            if not isinstance(PriceHour, (int, float)) or PriceHour <= 0:
                Message = "El precio por hora debe ser un valor numérico mayor a 0."
                raise Exception()

            # Validar Availability
            if not isinstance(Availability, bool):
                Message = "La disponibilidad debe ser True o False."
                raise Exception()

            # Validar Description
            if not isinstance(Description, str) or not Description.strip():
                Message = "La descripción debe contener información y debe ser un texto."
                raise Exception()

            # Validar TypeService
            if not isinstance(TypeService, str) or not TypeService.strip():
                Message = "El tipo de servicio debe contener información y debe ser un texto."
                raise Exception()

            # Validar Brand
            if not isinstance(Brand, str) or not Brand.strip():
                Message = "La marca debe contener información y debe ser un texto."
                raise Exception()

            # Validar Condition
            if not isinstance(Condition, str) or not Condition.strip():
                Message = "La condición debe contener información y debe ser un texto."
                raise Exception()

            if Condition not in ["Excelente", "Bueno", "Regular", "Malo"]:
                Message = "La condición debe ser Excelente, Bueno, Regular o Malo."
                raise Exception()
            
            # Validar TypeEquipment
            if not isinstance(TypeEquipment, str) or not TypeEquipment.strip():
                Message = "El tipo de equipo debe contener información y debe ser un texto."
                raise Exception()

            # Validar Discount

            if not isinstance(Discount, (int, float)) or Discount < 0:
                Message = "El descuento debe ser un valor numérico mayor o igual a 0."
                raise Exception()

            self.__Insertion(Name,PriceHour,Availability,Description,TypeService,Brand,Stock,Condition,TypeEquipment,Discount)

        except Exception:
            return (False, Message)

    def __Insertion(self,Name,PriceHour,Availability,Description,TypeService,Brand,Stock,Condition,TypeEquipment,Discount):
        try:

            ID_service = str(random.randint(10000, 999999999)) + TypeService

            while ID_service in self.__EquipmentRental["Equipment_id"]:
                ID_service = str(random.randint(10000, 999999999)) + TypeService

            self.__EquipmentRental["Equipment_id"].append(ID_service)
            self.__EquipmentRental["Name"].append(Name)
            self.__EquipmentRental["Description"].append(Description)
            self.__EquipmentRental["Availability"].append(Availability)

            PriceCondition = self.calculate_condition_price(PriceHour, Condition)
            PriceFinal = PriceCondition + (PriceCondition * (self.__tax / 100))
            
            self.__EquipmentRental["PriceHour"].append(PriceFinal)
            self.__EquipmentRental["Discount"].append(Discount)
            self.__EquipmentRental["tax"].append(self.__tax)
            self.__EquipmentRental["Stock"].append(Stock)
            self.__EquipmentRental["TypeService"] = "Renta Equipos"
            self.__EquipmentRental["Brand"].append(Brand)
            self.__EquipmentRental["Condition"].append(Condition)
            self.__EquipmentRental["TypeEquipment"].append(TypeEquipment)

            return(True, "Equipo creado correctamente")

        except ValueError:
            return (False, "Error: Hubo un error al momento de registrar el equipo")


    def calculate_condition_price(self, PriceHour, Condition):
        if Condition == "Excelente":
            return PriceHour

        elif Condition == "Bueno":
            return PriceHour * 0.90

        elif Condition == "Regular":
            return PriceHour * 0.75

        elif Condition == "Malo":
            return PriceHour * 0.50

        return PriceHour