from product import product
from validation import validate_user
from user import user

class service:
    def __init__(self):
        self.__product_list = []
        self.__user_list = []
        self.load_items()
        self.load_users()



    def load_users(self):
        get_user_list = validate_user('', '').get_user_list()
        for i in range(0, len(get_user_list)):
            user_instance = user(get_user_list[i][0], get_user_list[i][2], get_user_list[i][2])
            self.__user_list.append(user_instance)

    def add_user(self, user:user):
        self.__user_list.append(user)
        self.reload_user_file()

    def reload_user_file(self):
        user_file = open("users.txt", "w")
        user_file.write('')
        for user in self.__user_list:
            self.write_new_user(user)

    def write_new_user(self, user:user):
        # userID: gigi
        # userPass: 1234
        # userType: admin
        user_file = open("users.txt", "a")
        user_file.write("userID: {0}\n".format(user.get_user_name()))
        user_file.write("userPass: {0}\n".format(user.get_user_password()))
        user_file.write("userType: {0}\n\n".format(user.get_user_type()))

    def load_items(self):
        self.__product_file = open("products.txt", "r")
        self.__product_file_content = self.__product_file.read()
        self.__product_file.close()
        self.__producut_name_list = self.extract_feature('productName: ')
        self.__product_price_list = self.extract_feature('productPrice: ')
        self.__product_company_list = self.extract_feature('productCompany: ')
        self.__product_barcode_lsit = self.extract_feature("productBarcode: ")
        self.__product_stock_list = self.extract_feature("productStock: ")
        self.__product_promotion_list = self.extract_feature('productPromotion: ')
        for i in range(0, len(self.__producut_name_list)):
            product_name = self.__producut_name_list[i]
            product_price = self.__product_price_list[i]
            product_barcode = self.__product_barcode_lsit[i]
            product_company = self.__product_company_list[i]
            product_stock = self.__product_stock_list[i]
            product_promotion = self.__product_promotion_list[i]
            product_instance = product(product_name, product_price, product_barcode, product_company, product_promotion, product_stock)
            self.__product_list.append(product_instance)

    def extract_feature(self, feature):
        # We start searching for the userID at the start of the string
        current_poz = 0
        self.__user_feature_list = []
        while self.__product_file_content.find(feature, current_poz) != -1:
            user_feature_starting_index = self.__product_file_content.find(feature, current_poz) + len(feature)
            current_poz = user_feature_starting_index
            self.__user_feature_list.append("")
            while self.__product_file_content[user_feature_starting_index] != '\n' and user_feature_starting_index < len(self.__product_file_content):
                self.__user_feature_list[len(self.__user_feature_list) - 1] = self.__user_feature_list[len(self.__user_feature_list)-1]+ self.__product_file_content[user_feature_starting_index]
                user_feature_starting_index += 1
                if(user_feature_starting_index == len(self.__product_file_content)):
                    break
        return self.__user_feature_list

    def add_product(self, product_to_add: product):
        product_to_add.set_name(product_to_add.get_name().lower())
        if self.find_product_by_features(product_to_add):
            self.__product_list.append(product_to_add)
            self.write_new_element(product_to_add)
        else:
            pass

    def write_new_element(self, other:product):
        # productName: apa
        # productPrice: 10
        # productCompany: borsec
        # productBarcode: 123
        # productPromotion: 0
        self.__product_file = open("products.txt", "a")
        self.__product_file.write("productName: {0}\n".format(other.get_name()))
        self.__product_file.write("productPrice: {0}\n".format(other.get_product_price()))
        self.__product_file.write("productCompany: {0}\n".format(other.get_company()))
        self.__product_file.write("productBarcode: {0}\n".format(other.get_barcode()))
        self.__product_file.write("productStock: {0}\n".format(other.get_stock()))
        self.__product_file.write("productPromotion: {0}\n\n".format(other.get_promotion()))
        self.__product_file.close()

    def find_product_by_features(self, other: product):
        for i in range(0, len(self.__product_list)):
            if other.get_barcode() == self.__product_list[i].get_barcode():
                print("Please enter a product with a unique barcode")
                return False
            if other.get_name() == self.__product_list[i].get_name():
                print("Please enter a product with a unique name")
                return False
        return True

    def find_product_index_by_barcode(self, barcode_of_searched_product):
        for i in range(0, len(self.__product_list)):
            if self.__product_list[i].get_barcode() == barcode_of_searched_product:
                return i
        return -1

    def user_buy(self, barcode, quantity):
        if int(self.__product_list[self.find_product_index_by_barcode(barcode)].get_stock()) < quantity:
            print("Please enter lower amount, {0} {1} is available".format(self.__product_list[self.find_product_index_by_barcode(barcode)].get_stock(), self.__product_list[self.find_product_index_by_barcode(barcode)].get_name()))
        else:
            self.__product_list[self.find_product_index_by_barcode(barcode)].set_stock(int(self.__product_list[self.find_product_index_by_barcode(barcode)].get_stock()) - quantity)
            self.rewrite_list()

    def display_elements_under_set_price(self, max_price):
        for product in self.__product_list:
            if int(product.get_product_price()) <= max_price:
                self.display_element(product)
    def rewrite_list(self):
        self.__product_file.close()
        self.__product_file = open("products.txt", "w")
        self.__product_file.write("")
        self.__product_file.close()
        for element in self.__product_list:
            self.write_new_element(element)

    def display_discounted_items(self):
        for product in self.__product_list:
            # print(type(product.get_promotion()))
            if product.get_promotion() != '0':
                self.display_element(product)

    def delete_element(self, barcode_of_product_to_delete):
        if self.validate_barcode(barcode_of_product_to_delete):
            try_to_find_product = self.find_product_index_by_barcode(barcode_of_product_to_delete)
            print(try_to_find_product)
            if try_to_find_product != -1:
                del self.__product_list[try_to_find_product]
                self.rewrite_list()

                print("Element removed successfully")
            else:
                print("Please enter a valid element")
        else:
            print("enter a valid barcode")

    def display_all_elements(self):
        for product in self.__product_list:
            self.display_element(product)

    def display_element(self, product_to_display):
        print("Name: ", product_to_display.get_name())
        print("Price: ", product_to_display.get_product_price())
        print("Company: ", product_to_display.get_company())
        print("Barcode: ", product_to_display.get_barcode())
        print("Stock: ", product_to_display.get_stock())
        print("Promotion: ", product_to_display.get_promotion())
        if product_to_display.get_promotion() != '0':
            print("\033[93mDiscounted price\033[0m", ((int(product_to_display.get_product_price()) * (100 - int(product_to_display.get_promotion()))) / 100))
        print('\n')

    def display_elements_from_company(self, company_name):
        ok = 0
        for element in self.__product_list:
            if company_name == element.get_company():
                self.display_element(element)

    def barcode_exists(self, barcode):
        for element in self.__product_list:
            if barcode == element.get_barcode():
                return True
        return False
    def validate_barcode(self, barcode):
        if len(barcode) > 10:
            return False
        return True

    def validate_promotion(self, promotion):
        promotion.replace(' ', '')
        promotion_value = 0
        for i in range(0, len(promotion)):
            try:
                promotion_value = promotion_value*10+int(promotion[i])
            except:
                print("enter a valid promotion")
                return False
        if promotion_value > 100:
            print("enter a valid promotion value(0-100)")
            return False
        return True

    def update_product(self, barcode, update_key, value):
        #name price company promotion
        for element in self.__product_list:
            if element.get_barcode() == barcode:
                if update_key == 1:
                    element.set_name(value)
                if update_key == 2:
                    element.set_product_price(value)
                if update_key == 3:
                    element.set_company(value)
                if update_key == 4:
                    element.set_promotion(value)
                if update_key == 5:
                    element.set_stock(value)
                self.rewrite_list()
                break

