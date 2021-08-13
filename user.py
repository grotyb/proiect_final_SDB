from product import product
class user:
    def __init__(self, name, password, type):
        self.__name = name
        self.__password = password
        self.__type = type
    def get_user_name(self):
        return self.__name
    def set_user_name(self, new_name):
        self.__name = new_name
    def get_user_password(self):
        return self.__password
    def set_user_password(self, new_password):
        self.__password = new_password
    def get_user_type(self):
        return self.__type

    # def add_element(self, barcode):
