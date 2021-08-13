class product:
    def __init__(self, name, price, barcode, company, promotion, stock):
        self.__product_name = name
        self.__product_price = price
        self.__barcode = barcode
        self.__company = company
        self.__promotion = promotion
        self.__stock = stock

    def get_name(self):
        return self.__product_name
    def set_name(self, new_name):
        self.__product_name = new_name
    def get_product_price(self):
        return self.__product_price
    def set_product_price(self, new_price):
        self.__product_price = new_price
    def get_barcode(self):
        return self.__barcode
    def set_barcode(self, new_barcode):
        self.__barcode = new_barcode
    def get_company(self):
        return self.__company
    def set_company(self, new_company):
        self.__company = new_company
    def get_promotion(self):
        return self.__promotion
    def set_promotion(self, promotion):
        self.__promotion = promotion
    def get_stock(self):
        return self.__stock
    def set_stock(self, new_stock):
        self.__stock = new_stock

    def validate_product_features(self):
        if len(self.__barcode) > 10:
            print("Product barcode invalid please enter a 10 digit string")
            return False
        try:
            validate_price = int(self.__product_price)
        except Exception as e:
            print("Please enter a valid price")
            return False
        try:
            validate_stock = int(self.__stock)
        except Exception as e:
            print("Please enter atock amount")
            return False
        return True

    def __eq__(self, other):
        if self.__product_name == other.get_name() and self.__product_name == other.get_product_name and self.__barcode == other.get_barcode:
            return True
        return False