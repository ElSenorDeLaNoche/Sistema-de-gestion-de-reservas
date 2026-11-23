from Models.ServicesModel import Services
from datetime import datetime
import random
class RoomRental(Services):
    __RoomRental = {
     "Room_id":[],
     "Name":[],
     "Stock":[],
     "Description":[],
     "Max_capacity":[],
     "Availability":[],
     "tax":[],
     "TypeService":[],
     "PriceHour":[],
     "Discount":[],
     "Furnished":[]
    }
    __tax = 19

    
    
    def __init__(self, Name=None, PriceHour=None, Availability=None, Description=None, TypeService=None, Date=None, Furnished=None, Discount=None, Max_capacity=None, Stock=None):
        super().__init__(Name, PriceHour, Availability, Description, TypeService, Date)
        if Name == None:
            return
        
        self.validate_parameters(Name, PriceHour, Availability, Description, TypeService, Date, Furnished, Discount, Max_capacity, Stock)

         
    @classmethod
    def calculate_cost(cls, Date, Discount, PriceHour):
        try:
            Duration = (Date[1] - Date[0]).total_seconds() / 3600

            Operacion = PriceHour + (PriceHour * (cls.__tax / 100))
            Total = (Operacion - (Operacion * (Discount / 100))) * Duration

            return Total

        except Exception as e:
            return (False, f"Error en el cálculo de costos: {e}")
        

    def describe_service(self):
        
        return self.__RoomRental
    

    def validate_parameters(self, Name, PriceHour, Availability, Description, TypeService, Date, Furnished, Discount, Max_capacity, Stock):
        Message = ""
        try:
            # Validar Stock
            if not isinstance(Stock, int) or Stock < 0:
                Message = "La cantidad de salas no debe ser un número entero Menor a 0."
                raise Exception()
            
            # Validar Name

            if not isinstance(Name, str) or not Name.strip():
                Message = "El nombre debe contener informacion y ser un texto."
                raise Exception()

            # Validar PriceHour

            if not isinstance(PriceHour, (int, float)) or PriceHour <= 0:
                Message = "El precio por hora debe ser un valor numérico Mayor a 0."
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

            if not isinstance(TypeService, str) or not TypeService.strip():
                Message = "El tipo de servicio debe contener informacion y debe ser un texto."
                raise Exception()


            if not isinstance(Furnished, bool):
                Message = "El equipamiento debe ser True o False."
                raise Exception()

            # Validar Discount

            if not isinstance(Discount, (int, float)):
                Message = "El descuento debe ser un valor numérico Mayor o igual a 0."
                raise Exception()

            # Validar Max_capacity

            if not isinstance(Max_capacity, int) or Max_capacity <= 0:
                Message = "La capacidad máxima debe ser un número entero Mayor a 0."
                raise Exception()

            self.__Insertion(Name, PriceHour, Availability, Description, TypeService, Furnished, Discount, Max_capacity, Stock)

        except Exception:
            return(False,Message)



    def __Insertion(self, Name, PriceHour, Availability, Description, TypeService, Furnished, Discount, Max_capacity, Stock):
            
            try:
                ID_service = str(random.randint(10000, 999999999)) + TypeService
                while ID_service in self.__RoomRental["Room_id"]:
                    ID_service = str(random.randint(10000, 999999999)) + TypeService

                self.__RoomRental["Room_id"].append(ID_service)
                self.__RoomRental["Name"].append(Name)
                self.__RoomRental["Description"].append(Description)
                self.__RoomRental["Availability"].append(Availability)
                self.__RoomRental["PriceHour"].append(PriceHour + (PriceHour * (self.__tax/100)))
                self.__RoomRental["Discount"].append(Discount)
                self.__RoomRental["tax"].append(self.__tax)
                self.__RoomRental["Stock"].append(Stock)
                self.__RoomRental["TypeService"].append("Renta Salas")
                self.__RoomRental["Max_capacity"].append(Max_capacity)
                self.__RoomRental["Furnished"].append(Furnished)
                (True, "Servicios creado correctamente")
            except ValueError :
                (False,"Error: Hubo un error al momento de registrar el servicio")
    @classmethod
    def GetServiceID(cls,ID, Date):
        try:
            if (ID in cls.__RoomRental["Room_id"]):
                Consult = cls.__RoomRental["Room_id"].index(ID)
                if cls.__RoomRental["Stock"][Consult] <= 0:
                    Message = "Warning: La cantidad orecida se acaba de agotar para este servicio"
                    raise Exception()
                else:
                    DateStart = datetime.fromisoformat(Date[0])
                    DateEnd = datetime.fromisoformat(Date[1])
                    Date= (DateStart,DateEnd)

                    if not isinstance(Date, tuple):
                        Message = "La fecha debe ser una tupla."
                        raise Exception()
                    if len(Date) != 2:
                        Message = "La tupla debe contener exactamente una fecha/hora de inicio y una fecha/hora de fin."
                        raise Exception()

                    DateStart, DateEnd = Date

                    if not isinstance(DateStart, datetime):
                        Message = "La fecha/hora de inicio debe ser de tipo datetime."
                        raise Exception()

                    if not isinstance(DateEnd, datetime):
                        Message = "La fecha/hora de fin debe ser de tipo datetime."
                        raise Exception()

                    if DateStart >= DateEnd:
                        Message = "La fecha/hora de inicio debe ser anterior a la fecha/hora de fin."
                        raise Exception()

                    Diferencia = DateEnd - DateStart

                    Total = cls.calculate_cost(Date, cls.__RoomRental["Discount"][Consult], cls.__RoomRental["PriceHour"][Consult])

                    cls.__RoomRental["Stock"][Consult] = cls.__RoomRental["Stock"][Consult] - 1
                    return [ID, 
                            cls.__RoomRental["Name"][Consult], 
                            cls.__RoomRental["Stock"][Consult], 
                            cls.__RoomRental["TypeService"][Consult], 
                            Diferencia, 
                            Date, 
                            "Pendiente",
                            Total]

            else:
                Message = "Error: Es servicio seleccionado no pudo ser hallado"
                raise Exception()
        
        except Exception:
            return(False, Message)