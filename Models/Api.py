import webview
from Utilities.logs import info, error, warning

class Api:

    def __init__(self,Usuarios,Consulting,RoomRental, Equipment, Reservation):
        self.User = Usuarios
        self.Consulting = Consulting
        self.Room = RoomRental
        self.Equipment = Equipment
        self.Reservation = Reservation

    def Register(self, data):
        response = self.User.validar_Identificacion(data)
        if response[0]:
            info(response[1])
        else:
            error(response[1])
        return response


    def SeachUser(self,Identification):
        response = self.User.SearchUser(Identification)
        if (len(response) > 2):
            info("Se ha realizado una consulta de manera exitosa")
        else:
            error(response[1])
        return response

    def UpdateData(self, Data):
        response = self.User.Validacion_Campos(Data)
        if (response[0]):
            warning(response[1])
        else:
            error(response[1])
        return response

    def ConsultingService(self):
        return self.Consulting.describe_service()

    def Bd_RoomRental(self):
        return self.Room.describe_service()

    def Bd_Equipment(self):
        return self.Equipment.describe_service()

    def GenerateReservation(self, User, ID_service, Service, Date):
        response = self.Reservation.VerificationData(User,ID_service, Service, Date)
        if (response[0]):
            warning(response[1])
        else:
            error(response[1])
        return response

    def GetReservation(self):
        return self.Reservation.GetReservation()