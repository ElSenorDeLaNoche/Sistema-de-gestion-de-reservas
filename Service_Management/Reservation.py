from Services.ConsultingServices import ConsultingServices
from Services.EquipmentRental import EquipmentRental
from Services.RoomRental import RoomRental
from Models.UserModel import Usuarios
from datetime import datetime, timedelta
class Reservation(RoomRental,EquipmentRental,ConsultingServices,Usuarios):
     __Reservation ={
          "ID_Reservation":[],
          "User":[],
          "IDService":[],
          "Name":[],
          "Service":[],
          "Duration":[],
          "TimeService":[],
          "State":[],
          "Total":[]
     }


     def VerificationData(self,User,ID_service, Service, Date):
          UserData = Usuarios.GetID(User)
          if UserData[0]:
               if Service == "RoomRental":
                    Rental = RoomRental.GetServiceID(User,ID_service,Date)
                              
               elif Service == "EquipmentRental":
                              pass
               elif Service == "ConsultingServices":
                              pass
               else:
                    return (False,"Error: El servicio no pudo ser hallado")
               
               if len(Rental) == 2:
                    return Rental
               else:
                    return self.__AddService(Rental)
               
          else:
               return UserData

     def __AddService(self,Rental):
          try:
               self.__Reservation["ID_Reservation"].append(max(self.__Reservation["ID_Reservation"],default=0) + 1)
               self.__Reservation["User"].append(Rental[0])
               self.__Reservation["IDService"].append(Rental[1])
               self.__Reservation["Name"].append(Rental[2])
               self.__Reservation["Service"].append(Rental[3])
               self.__Reservation["Duration"].append(Rental[4])
               self.__Reservation["TimeService"].append(Rental[5])
               self.__Reservation["State"].append(Rental[6])
               self.__Reservation["Total"].append(Rental[7])
               return (True,"Se Ha registrado su reserva de manera exitosa")
          except Exception:
                 return (False, "Error: Se produjo un error al intentar registrar el servicio")

     def RemoveService():
          pass


     def  SearchService():
          pass


     def GetReservation(self):
          Reservation = self.__Reservation

          for Key, Values in Reservation.items():
               Reservation[Key] = [
                    str(Value) if isinstance(Value, (datetime, timedelta))
                    else tuple(str(Element) for Element in Value) if isinstance(Value, tuple) else Value for Value in Values
               ]

          return Reservation