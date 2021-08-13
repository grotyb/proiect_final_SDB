from validation import validate_user
from user import user
from product import product
from service import service
class UI:
    def __init__(self):
        self.__service = service()

    def run(self):
        print("1. Login")
        print("2. Create new User")
        try:
            user_input = int(input())
            if user_input > 2 or user_input <= 0:
                raise Exception
        except:
            print("Please enter a valid key")
            self.run()
        if user_input == 1:
            self.display_login_menu()
        else:
            self.create_user()

    def create_user(self):
        print("Enter the name of the new account")
        user_name = input()
        print("Enter the password for the new account")
        user_password = input()
        if validate_user('', '').validate_new_user(user_name):
            self.__service.add_user(user(user_name, user_password, 'user'))
            self.display_login_menu()
        else:
            self.run()


    def get_user_type(self):
        if self.__user.get_user_type() == 'Admin':
            return self.display_menu_admin()
        elif self.__user.get_user_type() == 'User':
            return self.display_menu_user()

    def display_menu_admin(self):
        print("Select the action that you would like to perform: ")
        print("0. Exit")
        print("1. Add a product to the product list")
        print("2. Delete an product from the product list")
        print("3. Update the characteristics of a product")
        print("4. Display the full list of products")
        print("5. Display products from a specific company")
        print("6. Add a promotion to a product group")
        try:
            key = int(input())
        except Exception as e:
            print(e)
            print("please enter a valid key")
            self.display_menu_admin()
        self.handle_admin_action(key)

    def handle_admin_action(self, key):
        if key == 0:
            return
        if key == 1:
            print("Please enter the name of the product that you would like to add: ")
            product_name = input()
            print("Please enter the price of the product")
            product_price = input()
            print("Please enter the company that makes the product")
            product_company = input()
            print("Please enter the barcode of the product you would like to add ")
            product_barcode = input()
            print("Please enter the ammount of items in stock ")
            product_stock = input()
            product_instance = product(product_name, product_price, product_barcode, product_company, 0, product_stock)
            if product_instance.validate_product_features():
                try:
                    self.__service.add_product(product_instance)
                except Exception as e:
                    print(e)
            else:
                pass
        if key == 2:
            print("Enter the barcode of the product you want to delete")
            barcode_to_delete = input()
            self.__service.delete_element(barcode_to_delete)

        if key == 3:
            print("Please enter the barcode of the product that you would like to update")
            barcode_to_update = input()
            if self.__service.barcode_exists(barcode_to_update) == False:
                print("Please enter a valid barcode")
            else:
                print("1. Update the name of the product")
                print("2. Update the price of the product")
                print("3. Update the company name")
                print("4. Update the promotion of the product")
                print("5. Update the stock for the product")
                try:
                    update_key = int(input())
                    if update_key > 5 or update_key < 0:
                        raise Exception("Enter a valid key")
                except:
                    print("Enter a valid key")
                if update_key == 1:
                    print("please enter the new name of the product")
                    new_value = input()
                elif update_key == 2:
                    print("Please enter the new price of the product")
                    try:
                        new_value = int(input())
                    except:
                        print("Please enter a valid price")
                elif update_key == 3:
                    print("Please enter the new name of the company")
                    new_value = input()
                elif update_key == 4:
                    print("Please add the value of the promotion as a number from 1 to 100: ")
                    new_value = input()
                    if not self.__service.validate_promotion(new_value):
                        self.display_menu_admin()
                elif update_key == 5:
                    try:
                        new_value = int(input())
                    except:
                        print("Please enter a valid stock number")
                self.__service.update_product(barcode_to_update, update_key, new_value)

        if key == 4:
            self.__service.display_all_elements()

        if key == 5:
            print("Please enter the name of the company that you would like to see the products of: ")
            company_name = input()
            self.__service.display_elements_from_company(company_name)

        if key == 6:
            list_of_barcodes = []
            print("Please add the value of the promotion as a number from 1 to 100:")
            value_of_promotion = input()
            if self.__service.validate_promotion(value_of_promotion):
                while True:
                    print("1. Add another barcode of an element you would like to apply a promotion to")
                    print("0. Exit")
                    key_value = input()
                    if key_value == '0':
                        break
                    if key_value == '1':
                        print("Please enter the barcode of the prduct you would like to add to the promotion")
                        barcode_of_element = input()
                        if not self.__service.validate_barcode(barcode_of_element) or self.__service.find_product_index_by_barcode(barcode_of_element) == -1:
                            print("Please enter a valid barocde")
                        else:
                            list_of_barcodes.append(barcode_of_element)
                for barcode in list_of_barcodes:
                    self.__service.update_product(barcode, 4, value_of_promotion)
                else:
                    self.display_menu_admin()
        self.display_menu_admin()

    def display_user_menu(self):
        print("0. Exit")
        print("1. Buy a product")
        print("2. See the list of products")
        print("3. See products under a specific price")
        print("4. See products that are part of a promotion")
        try:
            key = int(input())
            if key > 4 or key < -1:
                raise Exception("please Enter a key value between 1 and 4")
        except:
            print("Please enter a valid key")
            self.display_user_menu()
        self.handle_user_action(key)


    def handle_user_action(self, key):
        if key == 0:
            return
        if key == 1:
            print("Please enter the barcode of the product you would like to buy")
            barcode = input()

            if self.__service.find_product_index_by_barcode(barcode) == -1 :
                print("Please enter a valid barcode")
                self.display_user_menu()
            print("How many would you like to buy: ")
            try:
                quantity = int(input())
            except:
                print("please enter a valid quantity")
            self.__service.user_buy(barcode, quantity)
        if key == 2:
            self.__service.display_all_elements()
        if key == 3:
            print("Please enter the maximum price of a product: ")
            try:
                max_price = int(input())
            except:
                print("Please enter a valid price")
            self.__service.display_elements_under_set_price(max_price)
        if key == 4:
            self.__service.display_discounted_items()
        self.display_user_menu()

    def display_login_menu(self):
        print("Please enter the userID: ")
        user_id = input()
        print("Please enter the password for the specified userID: ")
        user_password = input()
        validator = validate_user(user_id, user_password)
        validation_response = validator.validate_passed_user()
        if validation_response == False:
            print("Inavid login credentials")
            self.display_login_menu()
        else:
                self.__user = user(user_id, user_password, validation_response)
                if validation_response == 'admin':
                    self.display_menu_admin()
                if validation_response == 'user':
                    self.display_user_menu()
