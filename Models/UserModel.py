import re, datetime
class Usuarios():

    __Clientes = {
        "Identification": [],
        "Name": [],
        "Email": [],
        "Phone": [],
        "DateRegister": []
    }

    def validar_Identificacion(self, FormUsuario):
        try:
            if FormUsuario[0] in self.__Clientes["Identification"]:
                raise Exception();
            else:
                return self.Validacion_Campos(FormUsuario)

        except Exception():
            return (False, "ERROR: El usuario ha sido repetido")

    def Validacion_Campos(self,FormUsuario):
        try:
            Message = ""
            Acum = 0
            
            for x in FormUsuario:
                if x is None or x == "":
                    Message = "Error: Se ha enviado un campo vacío"
                    raise Exception()

                elif Acum == 0 and (len(x) != 10 or not re.match(r"^\d{10}$", x)):
                    Message = "Error: Identificación no válida, debe tener 10 cifras numéricas"
                    raise Exception()

                elif Acum == 2 and not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", x):
                    Message = "Error: Formato de correo no válido"
                    raise Exception()

                elif Acum == 3 and not re.match(r"^3\d{9}$", x):
                    Message = "Error: Número no válido, debe tener 10 cifras y comenzar por 3"
                    raise Exception()

                Acum += 1
            
            if FormUsuario[4] == "Update":
                return self.___UpdateData(FormUsuario)
            elif FormUsuario[4] == "Register":
                return self.___Insertion(FormUsuario)
            else:
                Mensaje = "Error: Identificador de solicitud no reconocido"
                raise Exception()

        except Exception:
            return (False, Message)
    
    def ___Insertion(self,FormUsuario):
        
        self.__Clientes["Identification"].append(FormUsuario[0])
        self.__Clientes["Name"].append(FormUsuario[1])
        self.__Clientes["Email"].append(FormUsuario[2])
        self.__Clientes["Phone"].append(FormUsuario[3])
        self.__Clientes["DateRegister"].append(datetime.datetime.now)
        return (True, "Usuario registrado correctamente")

    def SearchUser(self,Identification):
        try:
            Message = ""
            if Identification is None or Identification == "":
                Message = "Error: Se ha enviado la identificacion vacia"
                raise Exception()
            elif (len(Identification) != 10 or not re.match(r"^\d{10}$", Identification)):
                    Message = "Error: Identificación no válida, debe tener 10 cifras numéricas"
                    raise Exception()
            else:
                if Identification in self.__Clientes["Identification"]:
                    Posicion = self.__Clientes["Identification"].index(Identification)
                    
                    return [
                            self.__Clientes["Identification"][Posicion],
                            self.__Clientes["Name"][Posicion],
                            self.__Clientes["Email"][Posicion],
                            self.__Clientes["Phone"][Posicion]
                            ]
                else:
                    Message = "Error: El usuario buscado no se encuentra en nuestra base de datos."
                    raise Exception()
            
        except Exception:
            return (False,Message)

    def ___UpdateData(self,Data):
        try:
            Message = ""

            if Data[0] in self.__Clientes["Identification"]:
                Posicion = self.__Clientes["Identification"].index(Data[0])
                        
                self.__Clientes["Name"][Posicion] = Data[1]
                self.__Clientes["Email"][Posicion] = Data[2]
                self.__Clientes["Phone"][Posicion] = Data[3]
    
                return (True, "Registro modificado exitosamente")
 
            else:
                Message = "Error: Al usuario se le ha alterado su Identificacion"
                raise Exception()
                
        except Exception:
            return (False,Message)

    @classmethod
    def GetID(cls, ID):
        try:
            if ID in cls.__Clientes["Identification"]:
                return (True, "")
            else:
                return (False, "Error: El Usuario no se encuentra Registrado En el Sistema")
        except Exception:
            return (False, "Error: Identificacion no Valida")

