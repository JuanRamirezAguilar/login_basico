class Usuario:
    def __init__(self, id_user: int, correo: str, password: str, nombre: str) -> None:
        self.__id_user = id_user if id_user is not None else 0
        self.__correo = correo
        self.__password = password
        self.__nombre = nombre
        
    def set_id_user(self, new_id: int) -> None:
        self.__id_user = new_id
        
    def set_correo(self, new_correo: str) -> None:
        self.__correo = new_correo
        
    def set_password(self, new_password: str) -> None:
        self.__password = new_password
        
    def set_nombre(self, new_nombre: str) -> None:
        self.__nombre = new_nombre
        
    def get_id(self) -> int:
        return self.__id_user
        
    def get_correo(self) -> str:
        return self.__correo
        
    def get_password(self) -> str:
        return self.__password
        
    def get_nombre(self) -> str:
        return self.__nombre
