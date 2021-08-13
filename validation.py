class validate_user:
    def __init__(self, user_id, user_password):
        self.__passed_user_id = self.remove_spaces(user_id)
        self.__passed_user_password = self.remove_spaces(user_password)
        self.__users_file = open("users.txt", "r")
        self.__text_file_content = self.__users_file.read()
        self.__user_id_list = []
        self.__user_pass_list = []
        self.__user_account_type = []
        self.extract_user_characteristics()

    def extract_user_characteristics(self):
        self.__user_id_list = self.extract_feature("userID: ")
        self.__user_pass_list = self.extract_feature("userPass: ")
        self.__user_account_type = self.extract_feature("userType: ")

    def get_user_list(self):
        return self.__user_id_list, self.__user_pass_list, self.__user_account_type
    def remove_spaces(self, string):
        string = string.replace(' ', '')
        return string
    def extract_feature(self, feature):
        # We start searching for the userID at the start of the string
        current_poz = 0
        self.__user_feature_list = []
        while self.__text_file_content.find(feature, current_poz) != -1:
            user_feature_starting_index = self.__text_file_content.find(feature, current_poz) + len(feature)
            current_poz = user_feature_starting_index
            self.__user_feature_list.append("")
            while self.__text_file_content[user_feature_starting_index] != '\n' and user_feature_starting_index < len(self.__text_file_content):
                self.__user_feature_list[len(self.__user_feature_list) - 1] = self.__user_feature_list[len(self.__user_feature_list)-1]+ self.__text_file_content[user_feature_starting_index]
                user_feature_starting_index += 1
                if(user_feature_starting_index == len(self.__text_file_content)):
                    break
        return self.__user_feature_list

    def validate_passed_user(self):
        #first we check if the userID is found in the list, afer we check that the passwords match
        for i in range(0,len(self.__user_id_list)):
            if self.__user_id_list[i] == self.__passed_user_id.lower() and self.__user_pass_list[i] == self.__passed_user_password:
                return self.__user_account_type[i]
        return False

    def validate_new_user(self, other_user_id):
        for i in range(0, len(self.__user_id_list)):
            if self.__user_id_list[i] == other_user_id.lower():
                print("Please enter a new name, this one is already taken")
                return False
        return True




