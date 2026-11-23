import webview
from Models.UserModel import Usuarios
from Services.ConsultingServices import ConsultingServices
from Services.RoomRental import RoomRental
from Services.EquipmentRental import EquipmentRental
from Services.Data.DataConsultingServices import DataConsultingServices
from Services.Data.DataRoomRental import DataRoomRental
from Services.Data.DataEquipmentRental import DataEquimentRental
from Service_Management.Reservation import Reservation
from Models.Api import Api
DataConsultingServices()
DataRoomRental()
DataEquimentRental()
Equipment= EquipmentRental()
Room = RoomRental()
consult = ConsultingServices()
objectUser = Usuarios()
reservation = Reservation()
Connection = Api(objectUser, consult, Room, Equipment, reservation)

webview.create_window(
    "Mi aplicación",
    "Assets/index.html",
    js_api= Connection,
    fullscreen=True
)

webview.start()