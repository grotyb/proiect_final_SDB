from UI import UI
from user import user
from validation import validate_user
from service import service
from product import product

def run():
    ui_instance = UI()
    ui_instance.run()

run()
# ser = service()
# usero = user("fifi", "fert", "admin")
# ser.write_new_user(usero)
# prod = product("a", "1", "21", "aqua")
# se = service()
# se.add_product(prod)
# print(se.validate_promotion("100"))
# print(se.validate_promotion("a"))
# print(se.validate_promotion("101"))

#
# # list to store file lines
# lines = []
# # read file
# file = open("products.txt",'r')
# lines = file.readlines()
# print(lines)
#
# file.close()
# file = open("products.txt", 'w')
# del lines[0]
# del lines[1]
#
# for i in range(0, len(lines)):
#     file.write(lines[i])